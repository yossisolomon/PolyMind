'''
Created on May 27, 2015

@author: tal
'''
from sklearn import cluster, neighbors
import numpy as np

test_data = np.array([[0,0,0,0,0,0, 200, 0,0,0,0, 0],
             [2,0,0,0,0,0, 200, 0,0,0,0, 0],
             [1,0,0,0,0,0, 200, 0,0,0,0, 0],
             [3,0,0,0,0,0, 200, 0,0,0,0, 0],
             [4,0,0,0,0,0, 200, 0,0,0,0, 0],
             [5,0,0,0,0,0, 200, 0,0,0,0, 0],
             [6,0,0,0,0,0, 200, 0,0,0,0, 0],
             [7,0,0,0,0,0, 200, 0,0,0,0, 0],
             [8,0,0,0,0,0, 200, 0,0,0,0, 0],
             [9,0,0,0,0,0, 200, 0,0,0,0, 0]
             ])

test_label = [1,2,1,3,2,1,1,1,1,1]

pre_data = [[0,0,0,0,0,0, 200, 0,0,0,0, 0],
             [2,0,0,0,0,0, 200, 0,0,0,0, 0],
             [1,0,0,0,0,0, 200, 0,0,0,0, 0],
             [3,0,0,0,0,0, 200, 0,0,0,0, 0],
             [4,0,0,0,0,0, 200, 0,0,0,0, 0],
             [5,0,0,0,0,0, 200, 0,0,0,0, 0],
             [6,0,0,0,0,0, 200, 0,0,0,0, 0],
             [7,0,0,0,0,0, 200, 0,0,0,0, 0],
             [8,0,0,0,0,0, 200, 0,0,0,0, 0],
             [9,0,0,0,0,0, 200, 0,0,0,0, 0]
             ]

k_mean_class = neighbors.KNeighborsClassifier(n_neighbors=3, weights="distance")
k_mean_class.fit(X=test_data,y=test_label)
res = k_mean_class.predict(np.c_[2,0,0,0,0,0, 200, 0,0,0,0, 0])
print res 

# k_means = cluster.KMeans(n_clusters=3)
# k_means.fit(X=test_data,y=test_label)
# k_means.predict(X=np.c_[pre_data])
# print k_means.labels_