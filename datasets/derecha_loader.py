import numpy as np
import networkx as nx
import pylab as plt
import pandas as pd
import dateutil.parser as dparser
import re

'''
treat each day as a discrete time stamp
'''
fname="red_temporal_completa.csv"
def load_temporarl_edgelist(fname, max_nodes=-1):
	lines=pd.read_csv(fname)
	lines=lines[['sourcecol', 'targetcol', 'day', "weight"]]
	#lines=lines.sort_values("datetime")
	lines=lines.values.tolist()
	#assume it is a directed graph at each timestamp
	# G = nx.DiGraph()

	#date u  v  w
	#find how many timestamps there are
	max_time = 0
	current_date = ''
	G_times = []
	G = nx.DiGraph()
	if(max_nodes > 0):
		G.add_nodes_from(list(range(0, max_nodes)))

	for i in range(0, len(lines)):
		line = lines[i]
		date_str = line[2]  #dd/mm/aaaa
		#start a new graph with a new date

		if (date_str != current_date):
			if (current_date != ''):
				G_times.append(G)	#append old graph
				#print(G.number_of_edges)
				#print(G.number_of_nodes)
				G = nx.DiGraph()	#create new graph
				if(max_nodes > 0):
					G.add_nodes_from(list(range(0, max_nodes)))
			current_date = date_str		#update the current date

		source = int(line[0])		
		target = int(line[1])
		w=int(line[3])
		G.add_edge(source, target, weight=w)
		 
	G_times.append(G)
	print ("maximum time stamp is " + str(len(G_times)))
	return G_times

# def plot_nodes_edges(G_times, fname):
# 	max_time = len(G_times)
# 	t = list(range(0, max_time))
# 	print(t)
# 	num_nodes = []
# 	num_edges = []
# 	for G in G_times:
# 		num_nodes.append(G.number_of_nodes())
# 		num_edges.append(G.number_of_edges())
# 	print(t, num_edges)

# 	plt.rcParams.update({'figure.autolayout': True})
# 	plt.rc('xtick', labelsize='x-small')
# 	plt.rc('ytick', labelsize='x-small')
# 	fig = plt.figure(figsize=(4, 2))
# 	ax = fig.add_subplot(1, 1, 1)
# 	ax.plot(t, num_nodes, marker='o', color='#74a9cf', ls='solid', linewidth=0.5, markersize=1, label="nodes")
# 	ax.plot(t, num_edges, marker='o', color='#78f542', ls='solid', linewidth=0.5, markersize=1, label="edges")
# 	ax.set_xlabel('time stamp', fontsize=8)
# 	ax.set_xscale('log')
# 	ax.set_ylabel('number of nodes / edges', fontsize=8)
# 	plt.title("plotting number of nodes and edges in " + fname, fontsize='x-small')
# 	plt.legend(fontsize = 'x-small')
# 	plt.savefig("number of nodes and edges"+'.pdf',bbox_inches='tight', pad_inches=0)



# def main():
# 	fname = "red_temporal_completa.csv"
# 	G_times = load_temporarl_edgelist(fname)
# 	max_time = len(G_times)
# 	plot_nodes_edges(G_times, fname)



# if __name__ == "__main__":
#     main()
