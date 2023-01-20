from dask.distributed import Client, progress
import dask.array as da
import pickle
import networkx
import dask 
import numpy as np
import networkx as nx
from sklearn.utils.extmath import randomized_svd
from scipy.sparse.linalg import svds, eigsh
from scipy import sparse
from numpy import linalg as LA
from datasets import UCI_loader
from datasets import SBM_loader
from datasets import USLegis_loader
from datasets import canVote_loader
from datasets import derecha_loader
from util import normal_util 

client = Client(processes=False, threads_per_worker=4,
                n_workers=4, memory_limit='7GB')
with open('myLAD\matrices.pkl', 'rb') as f:
    X = da.from_array(networkx.directed_laplacian_matrix(pickle.load(f)[0]))
u, s, v = da.linalg.svd_compressed(X, k=5699)

s = s.compute()

print(s)