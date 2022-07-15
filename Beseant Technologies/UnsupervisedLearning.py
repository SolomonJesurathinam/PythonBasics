#Unstructured data
#Clustering
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


data = pd.read_csv("Files/segmented_customers.csv")

X = data["Annual Income"]
Y = data["Spending Score"]

plt.scatter(X,Y)
plt.show()

new_df = data.iloc[:, 3:5]  # 1t for rows and second for columns
print(new_df)

#number of clusters
wcss=[]
for i in range(1,20):
    kmeans = KMeans(i)
    kmeans.fit(new_df)
    wcss_iter = kmeans.inertia_
    wcss.append(wcss_iter)
print(wcss)

number_clusters = range(1,20)
plt.plot(number_clusters,wcss)
plt.title('The Elbow title')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

#Clustering
kmeans = KMeans(5, init="random")
kmeans.fit(new_df)

y_kmeans = kmeans.fit_predict(new_df)
print(kmeans)
print(y_kmeans)

# Plot Cluster
data_with_clusters = data.copy()
data_with_clusters['Clusters'] = y_kmeans
plt.scatter(data_with_clusters['Annual Income'],data_with_clusters['Spending Score'],c=data_with_clusters['Clusters'],cmap='rainbow')
plt.show()

#method 2
#Clustering
kmeans = KMeans(5, init="k-means++")
kmeans.fit(new_df)

y_kmeans = kmeans.fit_predict(new_df)
print(kmeans)
print(y_kmeans)

# Plot Cluster
data_with_clusters = data.copy()
data_with_clusters['Clusters'] = y_kmeans
plt.scatter(data_with_clusters['Annual Income'],data_with_clusters['Spending Score'],c=data_with_clusters['Clusters'],cmap='rainbow')
plt.show()