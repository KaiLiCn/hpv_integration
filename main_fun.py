import pandas as pd
import get_data
import draw_hpv
import dash_bio as dashbio
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, dash_table  # pip install dash (version 2.0.0 or higher)

app = Dash(__name__)

# -- Import and clean data (importing csv into pandas)


annotation_data = get_data.inergrate_data(
    "~/Dropbox (University of Michigan)/Kai Li’s files/Courses/Rotations/Ryan Mills/geneModel/annotation.csv",
    "~/Dropbox (University of Michigan)/Kai Li’s files/Courses/Rotations/Ryan Mills/geneModel/inserts.csv")[
    0]

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("HPV integration visualization tool", style={'text-align': 'center'}),

    dash_table.DataTable(
        id='datatable-annotation',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": False} for i in annotation_data.columns
        ],
        data=annotation_data.to_dict('records'),
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        row_selectable="multi",
        row_deletable=False,
        selected_rows=[],
        page_action="native",
        page_current=0,
        page_size=10,
    ),
    html.Div(id='gene-integration-container'),

    dcc.Graph(id='draw_hpv',
              config={'displayModeBar': False}),

    html.Br(),

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components


@app.callback(
    Output('gene-integration-container', 'children'),
    Input('datatable-annotation', "derived_virtual_data"),
    Input('datatable-annotation', 'derived_virtual_selected_rows')
)
def update_genes(rows, derived_virtual_selected_rows):
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = annotation_data if rows is None else pd.DataFrame(rows)

    select_dff = annotation_data.iloc[derived_virtual_selected_rows, :]

    return [
        dashbio.Ideogram(
            id=chrom,
            chromosomes=[chrom],
            orientation='horizontal',
            brush=chrom + ':1-10000000',
            rotatable=False)
        for chrom in select_dff["chr"]
    ]

@app.callback(
    Output('draw_hpv', 'figure'),
    Input('datatable-annotation', "derived_virtual_selected_rows")
)
def update_hpv(derived_virtual_selected_rows):
    select_dff = annotation_data.iloc[derived_virtual_selected_rows, :]

    fig = draw_hpv.generate_hpv_plot()
    return fig

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
