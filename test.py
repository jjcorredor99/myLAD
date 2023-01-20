import pickle as pk
import numpy as np 
from sklearn.preprocessing import normalize
from datasets import derecha_loader
import Anomaly_Detection as anom
import os 

def Derecha(eigen_file,fname):

    timestamps = 61
    percent_ranked = 0.085
    difference=True
    #real_events = [3,7]

    window1 = 5
    window2 = 10
    initial_window = 10
    (z_shorts,z_longs,z_scores, events) = anom.detection_with_bothwindows(eigen_file=eigen_file, timestamps=timestamps, 
            percent_ranked=percent_ranked, window1=window1, window2=window2, initial_window=initial_window, difference=difference)

    scores = []
    scores.append(z_shorts)
    scores.append(z_longs)
    score_labels = ["short term " + str(window1), "long term " + str(window2)]
    anom.plot_anomaly_score("derecha", fname, scores, score_labels, events)

    scores = [z_scores]
    score_labels = ["anomaly score"]
    #plot_anomaly_and_spectro(fname, scores, score_labels, events, eigen_file=eigen_file)

    # anomaly_ranks = [sorted(z_scores).index(x) for x in z_scores]
    # G_times = USLegis_loader.load_legis_temporarl_edgelist("datasets/USLegis_processed/LegisEdgelist.txt")  
    #spearman(G_times, anomaly_ranks, False, window1, initial_window, plot=False)

directory = os.fsencode("Resultados eigenvalues\eigen")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)
    Derecha(str('Resultados eigenvalues\eigen' + '\d'+ filename[1:]),filename)


