import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs

# Generate some data
X, y = make_blobs(n_samples=400, centers=4, cluster_std=0.60, random_state=0)

# kmeans clustering
kmeans = KMeans(4, random_state=0)
kmeans.fit(X)  # 训练模型
labels = kmeans.predict(X)  # 预测分类
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis')
plt.show()
