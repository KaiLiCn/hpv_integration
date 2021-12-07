import pandas as pd
import get_data
import draw_hpv
import dash_bio as dashbio
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, dash_table  # pip install dash (version 2.0.0 or higher)
import dash_bootstrap_components as dbc

app = Dash(__name__)

# -- Import and clean data (importing csv into pandas)

sample_datatable, insertion_table = get_data.inergrate_data(
    "C:/Users/likai/Dropbox (University of Michigan)/Kai Li’s files/Courses/Rotations/Ryan Mills/geneModel/annotation.csv",
    "C:/Users/likai/Dropbox (University of Michigan)/Kai Li’s files/Courses/Rotations/Ryan Mills/geneModel/inserts.csv")

default_insertion = insertion_table[(insertion_table['sample'] == sample_datatable.iloc[0]['sample']) & (
        insertion_table['gene'] == sample_datatable.iloc[0]['gene'])]

position_can = [-2, -1, 0, 1, 2, 3]

default_table_data = default_insertion.copy()
default_table_data['position'] = "0"


def get_insertion_table(data_insertion, data_in_table):
    data_table = dash_table.DataTable(
        id='insertion',
        columns=([
                     {"name": i, "id": i, "deletable": False, "selectable": False, "editable": False} for i in
                     data_insertion.columns
                 ] + [{'id': 'position', 'name': 'position', 'presentation': 'dropdown'}
                      ]),
        data=data_in_table.to_dict('records'),
        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        row_selectable="multi",
        row_deletable=False,
        selected_rows=[0],
        page_action="native",
        page_current=0,
        page_size=10,
        dropdown={
            'position': {
                'options': [
                    {'label': str(i), 'value': i}
                    for i in position_can
                ]
            }

        },
        css=[{
            "selector": ".Select-menu-outer",
            "rule": 'display : block!important'
        }]
    )

    return data_table


# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("HPV integration visualization tool", style={'text-align': 'center'}),
    html.Div([
        html.Div([dash_table.DataTable(
            id='datatable-sample',
            columns=([
                {"name": i, "id": i, "deletable": False, "selectable": False} for i in
                sample_datatable.columns]
            ),
            data=sample_datatable.to_dict('records'),
            editable=False,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            row_selectable="multi",
            row_deletable=False,
            selected_rows=[0],
            page_action="native",
            page_current=0,
            page_size=10,
        )], style={'width': '20%', 'display': 'inline-block', 'padding': 10}),
        html.Div(id='datatable-insertion', children=[get_insertion_table(default_insertion, default_table_data)],
                 style={'width': '60%', 'display': 'inline-block', 'padding': 10}
                 )], style={'display': 'flex', 'flex-direction': 'row'}),

    html.Div(id='gene-integration-container'),

    dcc.Graph(id='draw_hpv',
              config={'displayModeBar': False, },
              style={'width': '80%', 'display': 'inline-block', 'padding': 10, 'height': '60vh'}),

    html.Br(),

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components

@app.callback(
    Output('datatable-insertion', 'children'),
    Input('datatable-sample', 'derived_virtual_selected_rows')
)
def update_insertion_table(derived_virtual_selected_rows):
    if derived_virtual_selected_rows is None or len(derived_virtual_selected_rows) == 0:
        derived_virtual_selected_rows = [0]

    select_dff = sample_datatable.iloc[derived_virtual_selected_rows, :]

    output_data = insertion_table[
        insertion_table['sample'].isin(select_dff['sample']) & insertion_table['gene'].isin(select_dff['gene'])]

    table_data = output_data.copy()
    table_data['position'] = "0"
    return get_insertion_table(output_data, table_data)


# @app.callback(
#     Output('gene-integration-container', 'data'),
#     Input('datatable-annotation', "derived_virtual_data"),
#     Input('datatable-annotation', 'derived_virtual_selected_rows')
# )
# def update_genes(rows, derived_virtual_selected_rows):
#     if derived_virtual_selected_rows is None:
#         derived_virtual_selected_rows = []
#
#     dff = annotation_data if rows is None else pd.DataFrame(rows)
#
#     select_dff = annotation_data.iloc[derived_virtual_selected_rows, :]
#
#     return [
#         dashbio.Ideogram(
#             id=chrom,
#             chromosomes=[chrom],
#             orientation='horizontal',
#             brush=chrom + ':1-10000000',
#             rotatable=False)
#         for chrom in select_dff["chr"]
#     ]

@app.callback(
    Output('draw_hpv', 'figure'),
    [Input('insertion', "derived_virtual_data"),
     Input('insertion', "derived_virtual_selected_rows")]
)
def update_hpv(derived_virtual_data, derived_virtual_selected_rows):
    derived_virtual_data = pd.DataFrame(derived_virtual_data)

    select_dff = derived_virtual_data.iloc[derived_virtual_selected_rows]

    fig = draw_hpv.generate_hpv_plot(select_dff)
    return fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
