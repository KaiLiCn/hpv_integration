import plotly.graph_objects as go
import collections


gene_colors = ['rgb(102,194,165)', 'rgb(252,141,98)', 'rgb(141,160,203)', 'rgb(231,138,195)', 'rgb(166,216,84)',
               'rgb(255,217,47)', 'rgb(229,196,148)', 'rgb(179,179,179)']


def get_hpv_colors(contig_range):
    range_dict = {}
    range_color_dict = {}
    # URR blank
    range_color_dict[range(0, 104)] = "white"
    # E6
    range_color_dict[range(104, 560)] = "Yellow"
    # E7
    range_color_dict[range(560, 858)] = "Purple"
    # E7 E1 blank
    range_color_dict[range(858, 865)] = "white"
    # E1 only
    range_color_dict[range(865, 2756)] = "Green"
    # E1 E2 interaction
    range_color_dict[range(2756, 2815)] = "Green;Blue"
    # E2 only part1
    range_color_dict[range(2815, 3358)] = "Blue"
    # E2 E4 interaction
    range_color_dict[range(3358, 3621)] = "Blue;Purple"
    # E2 only part2
    range_color_dict[range(3621, 3854)] = "Blue"
    # E5
    range_color_dict[range(3854, 4101)] = "LightGreen"
    # E5 L2 blank
    range_color_dict[range(4101, 4237)] = "white"
    # L2 only
    range_color_dict[range(4237, 5639)] = "Yellow"
    # L2 L1 interaction
    range_color_dict[range(5639, 5658)] = "Yellow;Orange"
    # L1 only
    range_color_dict[range(5638, 7157)] = "Orange"
    # Blank
    range_color_dict[range(7157, 7905)] = "white"

    contig_start = contig_range[0]
    contig_stop = contig_range[1]
    for each_range in range_color_dict.keys():
        if contig_start in each_range and contig_stop in each_range:
            range_dict[range(contig_start, contig_stop)] = range_color_dict[each_range]
        elif contig_start in each_range and contig_stop not in each_range:
            range_dict[range(contig_start, each_range.stop)] = range_color_dict[each_range]
            contig_start = each_range.stop

    return range_dict


def generate_hpv_plot(select_dff):
    fig = go.Figure()

    # Update axes properties
    fig.update_xaxes(
        showticklabels=False,
        showgrid=False,
        zeroline=False,
    )

    fig.update_yaxes(
        showticklabels=False,
        showgrid=False,
        zeroline=False,
    )

    fig.add_trace(go.Scatter(
        x=[350, 700, 1800, 3000, 3500, 3950, 4900, 6400],
        y=[0.6, 0.6, 0.6, 0.83, 0.6, 0.6, 0.6, 0.83],
        text=["E6", "E7", "E1", "E2", "E4", "E5", "L2", "L1"],
        mode="text",
        textfont=dict(
            color="black",
            size=12,
            family="Arail",
        )
    ))
    fig.add_trace(go.Scatter(
        x=[0],
        y=[1.2],
        text=["HPV-16"],
        mode="text",
        textfont=dict(
            color="black",
            size=15,
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
                  fillcolor="Yellow",
                  )

    # Add E7
    fig.add_shape(type="rect",
                  x0=562, y0=0.8, x1=857, y1=0.98,
                  line=dict(
                      color="Black",
                      width=0.5,
                  ),
                  fillcolor="Purple",
                  )

    # Add E1
    fig.add_shape(type="rect",
                  x0=865, y0=0.8, x1=2814, y1=0.98,
                  line=dict(
                      color="Black",
                      width=0.5,
                  ),
                  fillcolor='Green',
                  )

    # Add E2
    fig.add_shape(type="rect",
                  x0=2756, y0=1.02, x1=3853, y1=1.2,
                  line=dict(
                      color="Black",
                      width=0.5,
                  ),
                  fillcolor="Blue",
                  )

    # Add E4
    fig.add_shape(type="rect",
                  x0=3358, y0=0.8, x1=3620, y1=0.98,
                  line=dict(
                      color="Black",
                      width=0.5,
                  ),
                  fillcolor="Purple",
                  )

    # Add E5
    fig.add_shape(type="rect",
                  x0=3850, y0=0.8, x1=4101, y1=0.98,
                  line=dict(
                      color="Black",
                      width=0.5,
                  ),
                  fillcolor="LightGreen",
                  )

    # Add L2
    fig.add_shape(type="rect",
                  x0=4237, y0=0.8, x1=5658, y1=0.98,
                  line=dict(
                      color="Black",
                      width=0.5,
                  ),
                  fillcolor="Yellow",
                  )

    # Add L1
    fig.add_shape(type="rect",
                  x0=5639, y0=1.02, x1=7156, y1=1.2,
                  line=dict(
                      color="Black",
                      width=0.5,
                  ),
                  fillcolor="Orange",
                  )
    fig.update_yaxes(range=[-0.2, 8.5])

    ### Draw gene:
    # gene_start = select_dff.iloc[0]['geneStart']
    # gene_end = select_dff.iloc[0]['geneEnd']
    # gene_len = gene_end - gene_start
    # len_hpv_ratio = gene_len/7904
    # fig.add_shape(type="line",
    #               x0=0, y0=8, x1=7904, y1=8,
    #               line=dict(
    #                   color="Blue",
    #                   width=3,
    #               )
    #               )
    # fig.add_trace(go.Scatter(
    #     x=[0],
    #     y=[8.2],
    #     text=[select_dff.iloc[0]['gene'], select_dff.iloc[0]['gene']],
    #     mode="text",
    #     textfont=dict(
    #         color="black",
    #         size=15,
    #         family="Arail",
    #     )
    # ))

    ### Draw multi-gene:
    gene_dict = {}
    gene_color_dict = {}
    for index, row in select_dff.iterrows():
        chrome = int(row['name'].split(".")[0])
        start = int(row['geneStart'])
        end = int(row['geneEnd'])
        if chrome not in gene_dict.keys():
            gene_dict[chrome] = {start: [row['gene'], end, end - start]}
        else:
            gene_dict[chrome][start] = [row['gene'], end, end - start]
            gene_dict[chrome] = collections.OrderedDict(sorted(gene_dict[chrome].items()))

    gene_dict = collections.OrderedDict(sorted(gene_dict.items()))

    total_length = 0
    for chrome in gene_dict.keys():
        for gene_start in gene_dict[chrome]:
            total_length += gene_dict[chrome][gene_start][2]

    color_num = 8
    whole_ratio = total_length / 7904
    trans_start = 0
    for chrome in gene_dict.keys():
        for gene_start in gene_dict[chrome]:
            one_gene_color = gene_colors[color_num % 8]
            gene_color_dict[gene_start] = one_gene_color
            gene_len = gene_dict[chrome][gene_start][2] / whole_ratio
            fig.add_shape(type="line",
                          x0=trans_start, y0=8, x1=trans_start + gene_len - 10, y1=8,
                          line=dict(
                              color=one_gene_color,
                              width=3,
                          )
                          )
            fig.add_trace(go.Scatter(
                x=[trans_start],
                y=[8.2],
                text=[gene_dict[chrome][gene_start][0]],
                mode="text",
                textfont=dict(
                    color="black",
                    size=15,
                    family="Arail",
                )
            ))
            gene_dict[chrome][gene_start].append(trans_start)
            trans_start += gene_len
            color_num += 1

    ### Add contig:
    contig_list = dict()
    for index, row in select_dff.iterrows():
        if row['name'] not in contig_list.keys():
            contig_list[row['name']] = [
                [row['ins'], row['hpvSite'], row['fullLength'], row['position'], row['geneStart']],
                [row['type'], row['start'], row['end']]]
        else:
            contig_list[row['name']].append([row['type'], row['start'], row['end']])

    for one_contig in contig_list.keys():
        chrome = int(one_contig.split(".")[0])
        gene_start = int(contig_list[one_contig][0][4])
        hpv_site = contig_list[one_contig][0][1]
        init_hum_y_index = int(contig_list[one_contig][0][3]) + 4
        full_length_contig = contig_list[one_contig][0][2]
        gene_list = gene_dict[chrome][gene_start]

        fig.add_trace(go.Scatter(
            x=[hpv_site],
            y=[init_hum_y_index - 0.2],
            text=[one_contig],
            mode="text",
            textfont=dict(
                color="black",
                size=13,
                family="Arail",
            )
        ))

        for one_list in contig_list[one_contig][1:]:
            read_type = one_list[0]
            read_start = one_list[1]
            read_end = one_list[2]

            hum_ins = ((contig_list[one_contig][0][0] - gene_start) / whole_ratio) + gene_list[3]

            if read_type == "hum":
                if read_start == 0:
                    fig.add_shape(type="rect",
                                  x0=hpv_site - read_end, y0=init_hum_y_index, x1=hpv_site,
                                  y1=init_hum_y_index + 0.2,
                                  line=dict(
                                      color="Black",
                                      width=0.5,
                                  ),
                                  fillcolor=gene_color_dict[gene_start],
                                  )

                    fig.add_shape(type="line",
                                  x0=hpv_site - read_end, y0=init_hum_y_index + 0.2,
                                  x1=hum_ins - read_end / whole_ratio, y1=8,
                                  line=dict(
                                      color="Grey",
                                      width=1,
                                  )
                                  )
                    fig.add_shape(type="line",
                                  x0=hpv_site, y0=init_hum_y_index + 0.2,
                                  x1=hum_ins, y1=8,
                                  line=dict(
                                      color="Grey",
                                      width=1,
                                  )
                                  )

                else:
                    fig.add_shape(type="rect",
                                  x0=hpv_site, y0=init_hum_y_index, x1=hpv_site + (read_end - read_start),
                                  y1=init_hum_y_index + 0.2,
                                  line=dict(
                                      color="Black",
                                      width=0.5,
                                  ),
                                  fillcolor=gene_color_dict[gene_start],
                                  )

                    fig.add_shape(type="line",
                                  x0=hpv_site, y0=init_hum_y_index + 0.2,
                                  x1=hum_ins, y1=8,
                                  line=dict(
                                      color="Grey",
                                      width=1,
                                  )
                                  )
                    fig.add_shape(type="line",
                                  x0=hpv_site + (read_end - read_start), y0=init_hum_y_index + 0.2,
                                  x1=hum_ins + (read_end - read_start) / whole_ratio, y1=8,
                                  line=dict(
                                      color="Grey",
                                      width=1,
                                  )
                                  )
            else:
                if read_start == 0:
                    hpv_contig_colors = get_hpv_colors([hpv_site - read_end, hpv_site])
                    for one_part_range in hpv_contig_colors.keys():
                        one_part_color = hpv_contig_colors[one_part_range]
                        if ";" in one_part_color:
                            fig.add_shape(type="rect",
                                          x0=one_part_range.start, y0=init_hum_y_index, x1=one_part_range.stop,
                                          y1=init_hum_y_index + 0.1,
                                          line=dict(
                                              color="Black",
                                              width=0.25,
                                          ),
                                          fillcolor=one_part_color.split(";")[0],
                                          )
                            fig.add_shape(type="rect",
                                          x0=one_part_range.start, y0=init_hum_y_index+0.1, x1=one_part_range.stop,
                                          y1=init_hum_y_index + 0.2,
                                          line=dict(
                                              color="Black",
                                              width=0.25,
                                          ),
                                          fillcolor=one_part_color.split(";")[1],
                                          )
                        else:
                            fig.add_shape(type="rect",
                                          x0=one_part_range.start, y0=init_hum_y_index, x1=one_part_range.stop,
                                          y1=init_hum_y_index + 0.2,
                                          line=dict(
                                              color="Black",
                                              width=0.5,
                                          ),
                                          fillcolor=one_part_color,
                                          )
                else:
                    hpv_contig_colors = get_hpv_colors([hpv_site, hpv_site + (read_end - read_start)])
                    for one_part_range in hpv_contig_colors.keys():
                        one_part_color = hpv_contig_colors[one_part_range]
                        if ";" in one_part_color:
                            fig.add_shape(type="rect",
                                          x0=one_part_range.start, y0=init_hum_y_index, x1=one_part_range.stop,
                                          y1=init_hum_y_index + 0.1,
                                          line=dict(
                                              color="Black",
                                              width=0.25,
                                          ),
                                          fillcolor=one_part_color.split(";")[0],
                                          )
                            fig.add_shape(type="rect",
                                          x0=one_part_range.start, y0=init_hum_y_index + 0.1, x1=one_part_range.stop,
                                          y1=init_hum_y_index + 0.2,
                                          line=dict(
                                              color="Black",
                                              width=0.25,
                                          ),
                                          fillcolor=one_part_color.split(";")[1],
                                          )
                        else:
                            fig.add_shape(type="rect",
                                          x0=one_part_range.start, y0=init_hum_y_index, x1=one_part_range.stop,
                                          y1=init_hum_y_index + 0.2,
                                          line=dict(
                                              color="Black",
                                              width=0.5,
                                          ),
                                          fillcolor=one_part_color,
                                          )

    fig.update_shapes(dict(opacity=1, xref='x', yref='y'))

    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        'showlegend': False
    })

    # fig.layout.xaxis.fixedrange = True
    # fig.layout.yaxis.fixedrange = True

    return fig
