import networkx as nx
from matplotlib import pyplot as plt

from H_index import calculate_h_index, calculate_unified_h
from main import degree_to_np_array, calculate_gini, calculate_gintropy_max, plot_lorenz_curve


def plot_graph(G, size, degree, gini):
    degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
    dmax = max(degree_sequence)

    fig = plt.figure("Degree of a random graph", figsize=(8, 8))
    axgrid = fig.add_gridspec(5, 4)

    ax0 = fig.add_subplot(axgrid[0:3, :])
    # Gcc = G.subgraph(max(nx.strongly_connected_components(G), key=len))
    pos = nx.spring_layout(G, seed=10396953)
    nx.draw_networkx_nodes(G, pos, ax=ax0, node_size=20)
    nx.draw_networkx_edges(G, pos, ax=ax0, alpha=0.4)
    ax0.set_title(f"communism graph with size {size} and degree = {degree} and and gini {gini}")
    ax0.set_axis_off()


def communism_regular(n, d):
    G = nx.random_regular_graph(d, n)
    degree = G.degree()
    wealth_np = degree_to_np_array(degree)
    gini = calculate_gini(wealth_np)
    print(f"gini regular: {gini}")
    gintropy = calculate_gintropy_max(wealth_np)
    print(gintropy)
    h = calculate_unified_h(wealth_np, network_size)
    # plot_lorenz_curve(wealth_np)
    plot_graph(G,n, d, gini)
    return gini, gintropy, h


avg_gini = 0
avg_gintropy = 0
avg_h = 0
simulation_size = 100

for _ in range(0, simulation_size):
    network_size = 10
    degree = 3
    gini, gintropy, h = communism_regular(network_size, degree)
    avg_gini += gini
    avg_gintropy += gintropy

    print(f"calculate_unified_h {h}")
    print(f"h {h}")

avg_gini /= simulation_size
avg_gintropy /= simulation_size
avg_h /= simulation_size

print(f"avg_gini {avg_gini}")
print(f"avg_gintropy {avg_gintropy}")
print(f"avg_h {avg_h}")