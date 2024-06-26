import networkx as nx
from matplotlib import pyplot as plt

from H_index import calculate_unified_h
from main import degree_to_np_array, calculate_gini, calculate_gintropy_max, plot_lorenz_curve


def plot_graph(G, size, p, gini):
    degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
    dmax = max(degree_sequence)

    fig = plt.figure("Degree of a random graph", figsize=(8, 8))
    axgrid = fig.add_gridspec(5, 4)

    ax0 = fig.add_subplot(axgrid[0:3, :])
    pos = nx.spring_layout(G, seed=10396953)
    nx.draw_networkx_nodes(G, pos, ax=ax0, node_size=20)
    nx.draw_networkx_edges(G, pos, ax=ax0, alpha=0.4)
    ax0.set_title(f"natural graph with size {size} and p = {p} and and gini {gini}")
    ax0.set_axis_off()


def natural_er(n, p):
    # x_bar = 1
    # arr_natural_dist = np.random.exponential(scale=x_bar, size=n).tolist()
    # G = nx.random_degree_sequence_graph(arr_natural_dist)
    G = nx.erdos_renyi_graph(n, p)
    # G = nx.dense_gnm_random_graph(n, m)
    print(f"is connected {nx.is_connected(G)}")
    degree = G.degree()
    wealth_np = degree_to_np_array(degree)
    gini = calculate_gini(wealth_np)
    print(f"gini natural er: {gini}")
    # plot_graph(G, n, p, gini)
    gintropy = calculate_gintropy_max(wealth_np)
    print(gintropy)
    h = calculate_unified_h(wealth_np, nx.number_of_nodes(G))
    return gini, gintropy, h


avg_gini = 0
avg_gintropy = 0
avg_h = 0
simulation_size = 100

for _ in range(0, simulation_size):
    network_size = 500
    p = 0.4
    # m = network_size*10
    gini, gintropy, h = natural_er(network_size, p)
    avg_gini += gini
    avg_gintropy += gintropy
    avg_h += h

avg_gini /= simulation_size
avg_gintropy /= simulation_size
avg_h /= simulation_size

print(f"avg_gini {avg_gini}")
print(f"avg_gintropy {avg_gintropy}")
print(f"avg_h {avg_h}")
