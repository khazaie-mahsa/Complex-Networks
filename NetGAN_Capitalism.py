from training import Trainer
import matplotlib.pyplot as plt
import networkx as nx
import torch
import pandas as pd
import numpy as np
import scipy
from utils import graph_from_scores
from Create_Graph import create_wealth_distribution_graph
# from netgan_files.netgan.netgan import NetGAN
import pickle


def plot_scores(trainer, create_graph_every):
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))
    iterations = create_graph_every * np.arange(len(trainer.eo))
    axes[0].plot(iterations, trainer.roc_auc)
    axes[0].set_title('roc auc')
    axes[0].grid()
    axes[1].plot(iterations, trainer.avp, color='g')
    axes[1].set_title('average precision')
    axes[1].grid()
    axes[2].plot(iterations, trainer.eo, color='r')
    axes[2].set_title('edge overlap')
    axes[2].grid()


csv_file_path = '2024_Q1_networth_shares.csv'
df = pd.read_csv(csv_file_path)
graph = create_wealth_distribution_graph(df, 3000)
graph = nx.to_numpy_array(graph)
graph[graph != 0] = 1.0
graph_nx = nx.from_numpy_array(graph)
graph_sparse = scipy.sparse.csr_matrix(graph)

adjacency_matrix = graph
n_edges = adjacency_matrix.sum()

nx.draw(graph_nx, node_size=25, alpha=0.5)
plt.show()

trainer = Trainer(graph_sparse, len(adjacency_matrix), max_iterations=20000, rw_len=12, batch_size=128, H_gen=40,
                  H_disc=30, H_inp=128, z_dim=16, lr=0.0003,
                  n_critic=3, gp_weight=10.0, betas=(.5, .9), l2_penalty_disc=5e-5, l2_penalty_gen=1e-7, temp_start=5.0,
                  val_share=0.2, test_share=0.1, seed=20, set_ops=False)
create_every = 100
plot_every = 500
trainer.train(create_graph_every=create_every, plot_graph_every=plot_every, num_samples_graph=50000,
              stopping_criterion='val')

plot_scores(trainer, create_every)
# torch.save(trainer, 'capitalism.pt')

trans_mat = trainer.create_transition_matrix(50000)
graph_synthetic = []
for i in range(3):
    graph_sampled = graph_from_scores(trans_mat, n_edges)
    graph_synthetic.append(graph_sampled)
    graph_nx_sampled = nx.from_numpy_array(graph_sampled)
    nx.draw(graph_nx_sampled, node_size=25, alpha=0.5)
    pickle.dump(graph_nx_sampled, open('synth_10000.pickle', 'wb'))
    plt.show()

for i, graph_sampled in enumerate(graph_synthetic):
    graph_sampled = scipy.sparse.csc_matrix(graph_sampled)
    path = 'graph_'+str(i) + '.npz'
    scipy.sparse.save_npz(path, graph_sampled)

    graph_nx_sampled = nx.from_numpy_array(graph_sampled)
    # pickle.dump(new_G, open('synth_10000.pickle', 'wb'))
    # nx.draw(new_G, node_size=25, alpha=0.5)
    # plt.show()
