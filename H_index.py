import numpy as np


def calculate_w(degrees, i):
    sum = degrees.sum()
    return degrees[i] / sum


def calculate_h_index(array):
    # array = np.sort(array)
    # total_citations = sum(array)
    # cum_citations = np.cumsum(array)
    # cum_share = cum_citations / total_citations
    # n = np.shape(array)[0]
    # x_percent = i / n
    # y_percent = np.cumsum(array[0:i]) / cum_citations

    n = np.shape(array)[0]
    h = 0
    s = 0
    for i in range(n):
        w_i = calculate_w(array, i)
        for k in array[0:i + 1]:
            w_k = calculate_w(array, k)
            s += w_k - w_i

        s = 2 * s
        h += s / n

    h = 1 - h
    return h


def calculate_unified_h(degree_array, network_Size):
    avg_degree_network = degree_array.sum() / network_Size
    sum = 0
    for value in degree_array:
        for j in degree_array:
            sum += abs(value - j)
    print(sum)
    denominator = 2 * pow(network_Size, 2) * avg_degree_network
    H = sum / denominator
    return H


def degree_to_np_array(degree):
    wealth = [i[1] for i in degree]
    wealth_np = np.array(wealth, dtype=np.int32)
    return wealth_np


def calculate_h_long_formula(graph, network_size, landa):
    degrees = np.array(list(d for n, d in graph.degree()))
    print(f'lambda: {landa}')
    total_sum = 0
    for i in range(0, network_size):
        internal_sum = 0
        for k in range(0, i):
            w_k = calculate_w(degrees, k)
            w_i = calculate_w(degrees, i)
            internal_sum += w_k - w_i

        total_sum += (internal_sum * 2) / network_size

    h = 1 - (1 / network_size) * total_sum
    return h
