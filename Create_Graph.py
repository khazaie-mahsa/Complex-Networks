import math

import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from main import degree_to_np_array

# Load the CSV file
# csv_file_path = '2024_Q1_networth_shares.csv'
# df = pd.read_csv(csv_file_path)


# Define a function to create a graph from the wealth distribution data
def create_wealth_distribution_graph(df, total_nodes):
    # G = nx.Graph()

    # total_nodes = 1000  # Arbitrary number of nodes for the graph
    group_nodes = {}

    for _, row in df.iterrows():
        # group = row['Group']
        # percentage = row['Percentage']
        df_2024_q1 = df[df['Date'] == '2024:Q1']

        # Extract the Category and Net worth columns
        category_networth = df_2024_q1[['Category', 'Net worth']]
        # print(category_networth['Category'].astype(int))
        category_networth['Category'] = total_nodes / 1000 * category_networth['Category'].astype(int)
        # print(num_nodes)
        # print(category_networth)
        category_networth_dict = category_networth.to_dict('tight')['data']
        # print(category_networth_dict)
        # net_worth = category_networth['Net worth'].astype(float)
        # print(net_worth)
        # group_nodes[net_worth] = num_nodes
        # print(group_nodes)

    # Create nodes for each group
    # current_node_id = 0
    degree_dist = []
    print(category_networth_dict)
    for num_nodes, net_worth in category_networth_dict:
        print(num_nodes)
        print(net_worth)
        print("----------------------------------------------------------------------")
        for i in range(math.ceil(num_nodes)):
            degree_dist.append(int(net_worth))
    #         G.add_node(current_node_id, group=float(net_worth))
    #         current_node_id += 1
    #
    # # Connect nodes within the same group to represent wealth
    # for num_nodes, net_worth in category_networth_dict:
    #     nodes_in_group = [n for n, attr in G.nodes(data=True) if attr['group'] == float(net_worth)]
    #     for i in range(len(nodes_in_group)):
    #         for j in range(i + 1, len(nodes_in_group)):
    #             G.add_edge(nodes_in_group[i], nodes_in_group[j])

    print(degree_dist)
    print(len(degree_dist))
    # G = nx.expected_degree_graph(degree_dist, selfloops=False)
    if sum(degree_dist) % 2 != 0:
        degree_dist[0] += 1
    G = nx.configuration_model(degree_dist)
    G.remove_edges_from(nx.selfloop_edges(G))
    degree_dist_actual = nx.degree(G)
    print(degree_dist_actual)
    degree_dist_actual = degree_to_np_array(degree_dist_actual).tolist()
    # print(degree_dist_actual)
    # sum_degree_dist_actual = sum(degree_dist_actual)
    # print(sum_degree_dist_actual)
    # for i in degree_dist_actual:
    #     print(f"{i} : {i / sum_degree_dist_actual}")
    return G


# Create the graph
# G = create_wealth_distribution_graph(df)
#
# # Print some information about the graph
# # print(nx.info(G))
#
# # Visualize the graph (optional)
# plt.figure(figsize=(10, 10))
# pos = nx.spring_layout(G)  # Layout for visualization
# nx.draw(G, pos, node_size=20, with_labels=True)
# plt.show()

# Save the graph to a file
# nx.write_gpickle(G, '/mnt/data/wealth_distribution_graph.gpickle')
