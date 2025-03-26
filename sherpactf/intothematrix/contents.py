import numpy as np

# Load the .npy file
data = np.load("matrix.npy")

# Display the data
print(data)

# Optional: Inspect metadata
print(f"Shape: {data.shape}")
print(f"Data Type: {data.dtype}")
