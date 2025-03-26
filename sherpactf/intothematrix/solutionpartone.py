import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import MDS

# Load the distance matrix
distance_matrix = np.load("matrix.npy")

# Ensure the matrix is symmetric and has zero diagonals
assert np.allclose(distance_matrix, distance_matrix.T), "Matrix is not symmetric!"
assert np.all(np.diag(distance_matrix) == 0), "Diagonal is not zero!"

# Apply MDS to reduce to 2D
mds = MDS(n_components=2, dissimilarity="precomputed", random_state=42)
coordinates = mds.fit_transform(distance_matrix)

# Plot the 2D coordinates
plt.scatter(coordinates[:, 0], coordinates[:, 1], s=10)
plt.title("MDS Output")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Save coordinates for further analysis if needed
np.savetxt("coordinates.txt", coordinates)
