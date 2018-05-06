#importing mathematical calculation 
import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt 
from sklearn.cluster import KMeans 
# importing the data sets, data are collected from kaggle (Iris datasets)
df= pd.read_csv('Iris.csv')
print df.head() #data sets is imported successfully 

#Train the model
k=2 #Assigning the number of clusters
Kmeans = KMeans(n_clusters=K)
y,0
Kmeans= kmeans.fit(df) #training the model
labels= kmeans.labels_ #array that contains cluster number 

centroids= kmeans.cluster_centers_

#now plot the points representing their cluster 
colors= ['blue', 'red','green','black']
y=0
for x in labels:
	plt.scatter(df.iloc[y,0],df.iloc[y,1], color=colors[x])
	y+=1

for x in range(K):
	#now ploting the centroid 
	lines= plt.plot(centroids[x,0],centroids[x,1],'Kx')
	# we have to make the centroid larger 
	plt.setp(lines, ms=15.0)
	plt.setp(lines, mew=2.0)

title=('Number of cluster(K)={}').fromat(K)
plt.title(title)
plt.xlabel('eruptions(mins)')
plt.ylabel('waiting (mins)')
plt.show()	

