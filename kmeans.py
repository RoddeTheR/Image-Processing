import numpy as np


def k_means(k, data_set, limit=0.0001, debug=False):

	clusters = data_set[np.random.choice(len(data_set), k)]

	diff = float('inf')
	while diff > limit:
		# Calculates distances between all points and all clusters
		dist = np.array([np.linalg.norm(data_set - clusters[i], axis=1) for i in range(len(clusters))])

		# Selects the closest cluster
		min_dist = np.argmin(dist, axis=0)

		# Recalculates the clusters (Mean of all the objects closest to the cluster)
		new_clusters = np.array([np.mean(data_set[min_dist == i], axis=0) for i in range(len(clusters))])

		diff = np.sum(np.abs(clusters-new_clusters))
		clusters = new_clusters

		if debug:
			print(f"Diff:{diff}")

	if debug:
		print("Averages:", clusters)
	return clusters, min_dist
