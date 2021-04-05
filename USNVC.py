# load USNVC data and process data to show best fit with baseline data

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# path to USNVC data, requires 4 different csv files: baseline vegetation data
#for the area, constancy of each vegetation type, scaling, and the user data
baselinePath = "baselineSS.csv"
constancyPath = "constancy.csv"
scalingPath = "scaling.csv"
plotDataPath = "PlotData.csv"

# load actual csv files
# Must be in utf-8 encoding! Excel can save it in this format.
baseline = pd.read_csv(baselinePath)
constancy = pd.read_csv(constancyPath)
scaling = pd.read_csv(scalingPath)
plots = pd.read_csv(plotDataPath)

# compute z-scores
zscore_base = (baseline.iloc[:,2:] - baseline.iloc[:,2:].mean()) / baseline.iloc[:,2:].std()
zscore_plot = (plots.iloc[:,1:] - baseline.iloc[:,1:].mean()) / baseline.iloc[:,1:].std()


# compute weights for data
weights = constancy.iloc[:,2:] * scaling.iloc[:,2:] # if using constancy and scaling
#~ weights = scaling.iloc[:,2:] # if only using scaling

# normalize weights so sum is 1
scaledWeights = weights.divide(weights.sum(axis=1),axis=0)


Nbases = len(baseline.index)
Nplots = len(plots.index)
dists = np.zeros(shape=(Nbases,Nplots))
best = []
plotIDlist = []
for plotID in range(0,Nplots):
  # compute distance between baseline and plot data
  temp = scaledWeights * (zscore_base - zscore_plot.iloc[plotID,:])**2
  dist = temp.sum(axis=1)

  # save distance in array called dists
  dists[:,plotID] = dist

  # identify best baseline as the one with minimum distance from the plot data
  minidx = dist.idxmin()
  best.append(minidx)
  plotIDlist.append(plots.iloc[plotID,0])

# the following code will make plots of each point of data to show a best fit
#graph with all the baseline scenarios

# ~ for col in range(0,Nplots):
# ~ for col in [0]:
  # ~ x = range(2,Nbases+2)
  # ~ y = dists[:,col]
  # ~ minrow = best[col]
  # ~ titlestr = baseline.iloc[minrow,1]
  # ~ fig = plt.figure(col)
  # ~ plotlabel = plt.semilogy(x,dists[:,col],'ro')
  # ~ plt.semilogy(x[minrow],dists[minrow,col],'gs')
  # ~ plt.semilogy([0, Nbases+2],[dists[minrow,col], dists[minrow,col]],'g--')
  # ~ plt.title("Best Fit for plot " + plots.iloc[col,0] + ": " + titlestr + ", " + "Row " + str(minrow+2))
  # ~ plt.xticks(np.arange(0, Nbases, 5.0))
  # ~ plt.xlabel("index of USNVC region")
  # ~ plt.ylabel("distance between USNVC region and plot data")
  # ~ plt.grid()

# ~ plt.show()

output = baseline.iloc[best, 0:2]
bestFitRow = np.array(best) + 2
output.insert(0,"best fit row",bestFitRow)
print(output)
output["plotIDs"] = plotIDlist
output.to_csv("best_fit_USNVC_region.csv",index=False)
