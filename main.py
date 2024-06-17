import networkx as nx
import quantecon as qe
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


# old codes are commented


#
# # ensure your arr is sorted from lowest to highest values first!
# import quantecon as quantecon
#
# arr = np.array([0, 0, 1, 0, 0])
#
#
# def gini(arr):
#     count = arr.size
#     coefficient = 2 / count
#     indexes = np.arange(1, count + 1)
#     weighted_sum = (indexes * arr).sum()
#     total = arr.sum()
#     constant = (count + 1) / count
#     return coefficient * weighted_sum / total - constant
#
#
# def lorenz(arr):
#     # this divides the prefix sum by the total sum
#     # this ensures all the values are between 0 and 1.0
#     scaled_prefix_sum = arr.cumsum() / arr.sum()
#     # this prepends the 0 value (because 0% of all people have 0% of all wealth)
#     return np.insert(scaled_prefix_sum, 0, 0)
#
#
# # show the gini index!
# # print(gini(arr))
# #
# # lorenz_curve = lorenz(arr)
# #
# # print(lorenz_curve)
#
# # we need the X values to be between 0.0 to 1.0
#
#
# def lorenz(arr):
#     # this divides the prefix sum by the total sum
#     # this ensures all the values are between 0 and 1.0
#     scaled_prefix_sum = arr.cumsum() / arr.sum()
#     # this prepends the 0 value (because 0% of all people have 0% of all wealth)
#     return np.insert(scaled_prefix_sum, 0, 0)
#
#
# def communism(n, a):
#     """""
#     args:
#           n: int -> size of the population
#           a: int -> alpha in delta distribution
#
#     output:
#           should get 0
#     """""
#     delta_dist_arr = signal.unit_impulse(n, a)
#     # print(f"communism {communism}")
#     f_val_communism, c_val_communism = qe.lorenz_curve(delta_dist_arr)
#     c_bar = np.heaviside(delta_dist_arr, 0.5)
#     c_bar = np.insert(c_bar, 0, 0)
#     # c_val_communism = lorenz(communism)
#     # print(f_val_communism, c_val_communism)
#     gintropy_communism = c_bar - f_val_communism
#     s_communism = gintropy_communism.sum()
#     print(f"gintropy communism:{gintropy_communism}, s= {s_communism}")
#     gini = gini_c(delta_dist_arr)
#     print(f"gini communism: {gini}")
#
#
# def eco_window_dist(n, a, b):
#     arr = np.random.randint(a, b, size=n)
#     print(arr)
#     # term1 = np.heaviside(b - arr, 0.5)
#     # term2 = np.heaviside(a - arr, 0.5)
#     term1 = general_heaviside(arr, n, b, b, 0.5)
#     term2 = general_heaviside(arr, n, a, a, 0.5)
#
#     n = (term1 - term2)
#     d = b - a
#     r = n / d
#     return r
#
#
# def gini_coefficient(arr):
#     count = arr.size
#     coefficient = 2 / count
#     indexes = np.arange(1, count + 1)
#     weighted_sum = (indexes * arr).sum()
#     total = arr.sum()
#     constant = (count + 1) / count
#     return coefficient * weighted_sum / total - constant
#
#
# def general_heaviside(array, n, a, b, x2):
#     out = np.zeros(n, dtype=np.int32)
#     for idx, x in enumerate(array):
#         if x < a:
#             res = 1
#         elif a <= x <= b:
#             res = x2
#         else:
#             res = 0
#         out[idx] = res
#     return out
#
#
# def eco_c_bar(array, n, a, b):
#     out = np.zeros(n, dtype=np.int32)
#
#     for idx, x in enumerate(array):
#         if x < a:
#             res = 1
#         elif a <= x <= b:
#             res = (b - x) / (b - a)
#         else:
#             res = 0
#         out[idx] = res
#     return out
#
#
# def eco_window(n, a, b):
#     arr_eco_window_dist = eco_window_dist(n, a, b)
#     print(f"arr_eco_window_dist= {arr_eco_window_dist}")
#     term1 = np.heaviside(b - arr_eco_window_dist, 0.5)
#     term2 = np.heaviside(a - arr_eco_window_dist, 0.5)
#     # c_bar = ((b-arr_eco_window_dist)/(b-a)) * term1 - ((a-arr_eco_window_dist)/(b-a)) * term2
#     c_bar = eco_c_bar(arr_eco_window_dist, n, a, b)
#     c_bar = np.insert(c_bar, 0, 0)
#     print(c_bar)
#     gini = calculate_gini(arr_eco_window_dist)
#     print(f"gini eco-window: {gini}")
#     gintropy = 3 * gini * c_bar * (1 - c_bar)
#     print(f"gintropy eco-window= {gintropy}")
#     print("---------------------------qe----------------------------")
#     f_val_communism, c_val_communism = qe.lorenz_curve(arr_eco_window_dist)
#     print(f_val_communism, c_val_communism)
#     print("---------------------------code--------------------------")
#
#     c_code = lorenz(arr_eco_window_dist)
#     print(c_code)
#     return c_bar, f_val_communism
#
#
# def natural_dist(n, x_bar):
#     arr_natural_dist = np.random.default_rng().exponential(scale=x_bar, size=n)
#     print(f"arr_natural_dist {arr_natural_dist}")
#     mean = np.mean(arr_natural_dist)
#     arr_natural_dist = (-1 * arr_natural_dist) / mean
#     # print(f"arr_natural_dist {arr_natural_dist}")
#     c_bar = np.exp(arr_natural_dist)
#     print(f"mean {mean}")
#     f_bar = (c_bar * (arr_natural_dist + x_bar)) / mean
#     # gintropy = f_bar - c_bar
#     gintropy = (-1 * c_bar) * np.log(c_bar)
#     print(f"gintropy natural {gintropy}")
#     gini_index = calculate_gini(gintropy)
#     print(f"gini_index {gini_index}")
#     return c_bar, f_bar


def calculate_gini(array):
    array = array.flatten()
    array = np.sort(array)
    index = np.arange(1, array.shape[0] + 1)
    n = array.shape[0]
    return (np.sum((2 * index - n - 1) * array)) * 1. / (n * np.sum(array)) * 1.


def gini_paper_implementation(array):
    array = array.flatten()
    n = array.shape[0]
    array = np.sort(array)
    index = np.arange(0, n)
    # j = np.arange(0, n + 1)
    x_bar = np.mean(array)
    numerator = 0
    for i in index:
        for j in index:
            numerator += abs(array[i] - array[j])
    denominator = x_bar * 2 * pow(n, 2)
    return numerator / denominator


def calculate_gintropy_max(array):
    array = np.sort(array)
    total_citations = sum(array)
    cum_citations = np.cumsum(array)
    cum_share = cum_citations / total_citations
    diagonal = np.linspace(0, 1, len(array))
    return np.max(diagonal - cum_share)


def plot_lorenz_curve(array):
    array = np.sort(array)
    total_citations = sum(array)
    cum_citations = np.cumsum(array)
    cum_share = cum_citations / total_citations
    diagonal = np.linspace(0, 1, len(array))
    plt.plot(diagonal, diagonal, linestyle='--', color='gray')
    plt.plot(1 - diagonal, 1 - cum_share, marker='o', markersize=3, color='blue')
    plt.fill_between(1 - diagonal, 1 - diagonal, 1 - cum_share, alpha=0.2, color='blue')
    plt.title('Lorenz Curve')
    plt.xlabel('C')
    plt.ylabel('F')


def degree_to_np_array(degree):
    wealth = [i[1] for i in degree]
    wealth_np = np.array(wealth, dtype=np.int32)
    return wealth_np


def plot_graph(G, size, g, l, gini):
    degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
    dmax = max(degree_sequence)

    fig = plt.figure("Degree of a random graph", figsize=(8, 8))
    axgrid = fig.add_gridspec(5, 4)

    ax0 = fig.add_subplot(axgrid[0:3, :])
    # Gcc = G.subgraph(max(nx.strongly_connected_components(G), key=len))
    pos = nx.spring_layout(G, seed=10396953)
    nx.draw_networkx_nodes(G, pos, ax=ax0, node_size=20)
    nx.draw_networkx_edges(G, pos, ax=ax0, alpha=0.4)
    ax0.set_title(f"communism++ graph with size {size} and #hubs = {g} and #leaves = {l} and gini {gini}")
    ax0.set_axis_off()


def natural_er(n, p):
    # x_bar = 1
    # arr_natural_dist = np.random.exponential(scale=x_bar, size=n).tolist()
    # G = nx.random_degree_sequence_graph(arr_natural_dist)
    G = nx.erdos_renyi_graph(n, p)
    print(f"is connected {nx.is_connected(G)}")
    degree = G.degree()
    wealth_np = degree_to_np_array(degree)
    gini_paper = gini_paper_implementation(wealth_np)
    print(f"gini_paper natural er: {gini_paper}")
    gini = calculate_gini(wealth_np)
    print(f"gini natural er: {gini}")
    plot_graph(G, n, p, gini)

    gintropy = calculate_gintropy_max(wealth_np)
    print(gintropy)
    # plot_lorenz_curve(wealth_np)
    return gini, gintropy


def communism_regular(n):
    G = nx.random_regular_graph(3, n)
    degree = G.degree()
    wealth_np = degree_to_np_array(degree)
    gini = calculate_gini(wealth_np)
    print(f"gini regular: {gini}")
    gintropy = calculate_gintropy_max(wealth_np)
    print(gintropy)
    plot_lorenz_curve(wealth_np)
    return gini, gintropy


def eco_window_er(n, a, b):
    sequence = []
    while True:
        sequence = np.random.randint(a, b + 1, n).tolist()
        print(sequence)

        if nx.is_valid_degree_sequence_havel_hakimi(sequence):
            break

    G = nx.random_degree_sequence_graph(sequence)
    degree = G.degree()
    wealth_np = degree_to_np_array(degree)
    gini = calculate_gini(wealth_np)
    print(f"gini eco-window er: {gini}")
    gintropy = calculate_gintropy_max(wealth_np)
    print(gintropy)
    plot_graph(G, n, a, b, gini)
    # plot_lorenz_curve(wealth_np)
    return gini, gintropy


def capitalism_ba(n, m):
    G = nx.barabasi_albert_graph(n, m)
    degree = G.degree()
    wealth_np = degree_to_np_array(degree)
    gini = calculate_gini(wealth_np)
    print(f"gini capitalism_ba: {gini}")
    gintropy = calculate_gintropy_max(wealth_np)
    print(gintropy)
    # plot_lorenz_curve(wealth_np)
    plot_graph(G, n, m, gini)
    return gini, gintropy


def create_connected_star_network(hub, leaf):
    graph = nx.complete_graph(hub)
    l = [i for i in range(hub, (hub*leaf) + hub)]
    graph.add_nodes_from(l)
    z = hub
    for j in range(hub):
        for i in range(z, z+leaf):
            graph.add_edge(j, z)
            z += 1

    return graph


def draw_network(graph):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=500, node_color='skyblue')
    plt.show()


def communism_plus_plus(number_hub_nodes, number_leaf):
    G = create_connected_star_network(number_hub_nodes, number_leaf)
    degree = G.degree()
    wealth_np = degree_to_np_array(degree)
    gini = calculate_gini(wealth_np)
    print(f"gini communism_plus_plus: {gini}")
    gintropy = calculate_gintropy_max(wealth_np)
    print(gintropy)
    # plot_lorenz_curve(wealth_np)
    plot_graph(G, number_hub_nodes + number_leaf, number_hub_nodes, number_leaf, gini)
    # draw_network(G)
    return gini, gintropy


# --------------------------communism-----------------------------------
# avg_gini = 0
# avg_gintropy = 0
# simulation_size = 10
#
# for _ in range(0, simulation_size):
#     network_size = 500
#     gini, gintropy = communism_regular(network_size)
#     avg_gini += gini
#     avg_gintropy += gintropy
#
# avg_gini /= simulation_size
# avg_gintropy /= simulation_size
#
# print(f"avg_gini {avg_gini}")
# print(f"avg_gintropy {avg_gintropy}")

# ------------------------------------communism++------------------------
# avg_gini = 0
# avg_gintropy = 0
# simulation_size = 1
#
# for _ in range(0, simulation_size):
#     # network_size = 500
#     G = 4  # Number of hubs
#     L = 20  # Number of leaf nodes
#     gini, gintropy = communism_plus_plus(G, L)
#     avg_gini += gini
#     avg_gintropy += gintropy
#
# avg_gini /= simulation_size
# avg_gintropy /= simulation_size
#
# print(f"avg_gini {avg_gini}")
# print(f"avg_gintropy {avg_gintropy}")

# ---------------------------eco-window--------------------------
# n = 100

# avg_gini = 0
# avg_gintropy = 0
# simulation_size = 1
#
# for _ in range(0, simulation_size):
#     network_size = 500
#     a = 1
#     b = 10
#     gini, gintropy = eco_window_er(network_size, a, b)
#     avg_gini += gini
#     avg_gintropy += gintropy
#
# avg_gini /= simulation_size
# avg_gintropy /= simulation_size
#
# print(f"avg_gini {avg_gini}")
# print(f"avg_gintropy {avg_gintropy}")
# -------------------------------natural-----------------------------

# avg_gini = 0
# avg_gintropy = 0
# simulation_size = 1
#
# for _ in range(0, simulation_size):
#     network_size = 500
#     p = 0.5
#     gini, gintropy = natural_er(network_size, p)
#     avg_gini += gini
#     avg_gintropy += gintropy
#
# avg_gini /= simulation_size
# avg_gintropy /= simulation_size
#
# print(f"avg_gini {avg_gini}")
# print(f"avg_gintropy {avg_gintropy}")

# n = 100
# natural_er(n)
# ------------------------------------capitalism---------------------
# n = 100
# m = 2
# capitalism_ba(n, m)

# avg_gini = 0
# avg_gintropy = 0
# simulation_size = 1
#
# for _ in range(0, simulation_size):
#     network_size = 500
#     m = 5
#     gini, gintropy = capitalism_ba(network_size, m)
#     avg_gini += gini
#     avg_gintropy += gintropy
#
# avg_gini /= simulation_size
# avg_gintropy /= simulation_size
#
# print(f"avg_gini {avg_gini}")
# print(f"avg_gintropy {avg_gintropy}")
#
# plt.show()
