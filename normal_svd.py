import pickle
import numpy as np
import networkx as nx
import os 
from numpy import linalg
from scipy.sparse.linalg import svds, eigsh
from scipy import sparse

with open('myLAD\matrices.pkl', 'rb') as f:
    G_times = pickle.load(f)

matrices = []
for G in G_times:
    matrices.append(nx.directed_laplacian_matrix(G))

print("inicio")
singular_values = []
i=0
for matrix in matrices:
    s = np.linalg.svd(matrix,compute_uv=False)
    os.system("cls")
    i+=1
    print("SVD" + " " + str(i))
    singular_values.append(s)

outfile = open("svd_completos",'wb')
pickle.dump(singular_values,outfile)
outfile.close()