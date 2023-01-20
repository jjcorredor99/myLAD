import derecha_loader
import pickle as pk
import networkx as nx
import pandas as pd

"""
G_times = derecha_loader.load_temporarl_edgelist("datasets\ed2derecha.csv")
average_clustering = []
for i in range(len(G_times)):
    print(i)
    average_clustering.append(nx.average_clustering(G_times[i].to_undirected()))
outfile = open("metrica_clustering.pkl",'wb')
pk.dump(average_clustering,outfile)
outfile.close()

global_efficiency = []
for i in range(len(G_times)):
    print(i)
    global_efficiency.append(nx.global_efficiency(G_times[i].to_undirected()))
outfile = open("metrica_efficiency.pkl",'wb')
pk.dump(global_efficiency,outfile)
outfile.close()

average_degree_connectivity = []
for i in range(len(G_times)):
    print(i)
    average_degree_connectivity.append(nx.average_degree_connectivity(G_times[i].to_undirected()))
outfile = open("metrica_averagedegreeconnectivity.pkl",'wb')
pk.dump(average_degree_connectivity,outfile)
outfile.close()
"""

clustering = pd.read_pickle("metrica_clustering.pkl")
degree = pd.read_pickle("metrica_averagedegreeconnectivity.pkl")
efficiency = pd.read_pickle("metrica_efficiency.pkl")

print("a")