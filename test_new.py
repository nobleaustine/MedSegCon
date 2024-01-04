import numpy as np

# Example DICOM pixel arrays with varying sizes along axis=0
array1 = np.random.randint(0, 10, size=(5, 2, 2))  # Shape: (5, 3, 4)
array2 = np.random.randint(0, 10, size=(7, 2, 2))  # Shape: (7, 3, 4)
array3 = np.random.randint(0, 10, size=(4, 2, 2))  # Shape: (4, 3, 4)

# Find the maximum size along axis=0
max_size = max(array1.shape[0], array2.shape[0], array3.shape[0])
arrays = [array1, array2, array3]

print(arrays[2])

# Create a list to store padded or cropped arrays
padded_arrays = []

# Pad or crop each array to the maximum size along axis=0
for arr in arrays:
    # Calculate padding or cropping
    pad_width = ((0, max_size - arr.shape[0]), (0, 0), (0, 0))

    # Pad or crop along axis=0
    padded_array = np.pad(arr, pad_width, mode='constant', constant_values=0)

    # Append the padded or cropped array to the list
    padded_arrays.append(padded_array)
print(padded_arrays[2])