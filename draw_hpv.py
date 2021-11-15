import plotly.graph_objects as go


def generate_hpv_plot():
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=[1.5, 4.5],
        y=[0.75, 0.75],
        text=["Unfilled Rectangle", "Filled Rectangle"],
        mode="text",
    ))

    # Update axes properties
    fig.update_xaxes(
        showticklabels=True,
        showgrid=False,
        zeroline=False,
    )

    fig.update_yaxes(
        showticklabels=False,
        showgrid=False,
        zeroline=False,
    )

    fig.add_shape(type="line",
                  x0=0, y0=1, x1=10, y1=1,
                  line=dict(
                      color="LightSeaGreen",
                      width=3,
                  )
                  )

    # Add shapes
    fig.add_shape(type="rect",
                  x0=1, y0=1, x1=2, y1=3,
                  line=dict(color="RoyalBlue"),
                  )
    fig.add_shape(type="rect",
                  x0=3, y0=0.8, x1=6, y1=1,
                  line=dict(
                      color="RoyalBlue",
                      width=1,
                  ),
                  fillcolor="LightSkyBlue",
                  )
    fig.update_shapes(dict(xref='x', yref='y'))

    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })

    return fig
