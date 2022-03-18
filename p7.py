from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('.\p7.csv')
df1 = pd.DataFrame(data)
print(df1)

f1= df1['Distance_Feature'].values
f2= df1['Speeding_Feature'].values

X = np.matrix(list(zip(f1,f2)))

plt.plot()
plt.xlim([0,100])
plt.ylim([0,50])
plt.title('Datasets')
plt.xlabel('Distance_Feature')
plt.ylabel('Speeding_feature')
plt.scatter(f1,f2)
plt.show()

plt.plot()

colors = ['r','g','b']
markers = ['o','v','s']

kmeans_model = KMeans(n_clusters=3).fit(X)

plt.plot()

for i, l in enumerate(kmeans_model.labels_):
    plt.plot(f1[i],f2[i],color = colors[l], marker = markers[l],ls='None')
    plt.xlim([0,100])
    plt.ylim([0,50])
plt.show()

