import numpy as np
import networkx as nx
import pylab as plt
import pandas as pd
import dateutil.parser as dparser
import re

def extract_nodes():
	df = pd.read_csv("datasets\ed2derecha.csv")

	source = df["sourcecol"]
	source = set(source.drop_duplicates().tolist())

	target = df["targetcol"]
	target = set(target.drop_duplicates().tolist())

	nodes = list(source.union(target))

	return nodes


'''
treat each day as a discrete time stamp
'''
fname="datasets\ed2derecha.csv"
def load_temporarl_edgelist(fname, max_nodes=-1):
	all_nodes = extract_nodes()
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
	G_times = G_times[1:]
	print ("maximum time stamp is " + str(len(G_times)))
	return G_times
