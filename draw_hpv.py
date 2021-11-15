import plotly.graph_objects as go


def generate_hpv_plot():
    fig = go.Figure()

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

    fig.add_trace(go.Scatter(
        x=[350, 700, 1800, 3500, 3500, 3950, 4900, 6400],
        y=[0.87, 0.87, 0.87, 1.1, 0.87, 0.87, 0.87, 1.1],
        text=["E6", "E7", "E1", "E2", "E4", "E4", "L2", "L1"],
        mode="text",
        textfont=dict(
            color="black",
            size=13,
            family="Arail",
        )
    ))

    fig.add_shape(type="line",
                  x0=0, y0=1, x1=7904, y1=1,
                  line=dict(
                      color="Black",
                      width=3,
                  )
                  )

    # Add URR
    fig.add_shape(type="line",
                  x0=0, y0=1, x1=103, y1=1,
                  line=dict(
                      color="Blue",
                      width=3,
                  )
                  )

    # Add E6
    fig.add_shape(type="rect",
                  x0=104, y0=0.8, x1=559, y1=0.98,
                  line=dict(
                      color="Black",
                      width=0.5,
                  ),
                  fillcolor="Red",
                  )

    # Add E7
    fig.add_shape(type="rect",
                  x0=562, y0=0.8, x1=857, y1=0.98,
                  line=dict(
                      color="Black",
                      width=0.5,
                  ),
                  fillcolor="Red",
                  )

    # Add E1
    fig.add_shape(type="rect",
                  x0=865, y0=0.8, x1=2814, y1=0.98,
                  line=dict(
                      color="Black",
                      width=0.5,
                  ),
                  fillcolor="Orange",
                  )

    # Add E2
    fig.add_shape(type="rect",
                  x0=2756, y0=1.02, x1=3853, y1=1.2,
                  line=dict(
                      color="Black",
                      width=0.5,
                  ),
                  fillcolor="Orange",
                  )

    # Add E4
    fig.add_shape(type="rect",
                  x0=3358, y0=0.8, x1=3620, y1=0.98,
                  line=dict(
                      color="Black",
                      width=0.5,
                  ),
                  fillcolor="Green",
                  )

    # Add E5
    fig.add_shape(type="rect",
                  x0=3850, y0=0.8, x1=4101, y1=0.98,
                  line=dict(
                      color="Black",
                      width=0.5,
                  ),
                  fillcolor="Orange",
                  )

    # Add L2
    fig.add_shape(type="rect",
                  x0=4237, y0=0.8, x1=5658, y1=0.98,
                  line=dict(
                      color="Black",
                      width=0.5,
                  ),
                  fillcolor="Blue",
                  )

    # Add L1
    fig.add_shape(type="rect",
                  x0=5639, y0=1.02, x1=7156, y1=1.2,
                  line=dict(
                      color="Black",
                      width=0.5,
                  ),
                  fillcolor="Blue",
                  )
    fig.update_yaxes(range=[0, 5])

    fig.update_shapes(dict(opacity=0.6, xref='x', yref='y'))

    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)'
    })

    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True

    return fig
