import h5py

def print_hdf5_structure(group, indent=0):
    """Recursively print the structure and contents of an HDF5 group."""
    items = list(group.items())

    for name, item in items:
        if isinstance(item, h5py.Group):
            print(" " * indent + f"Group: {name}")
            print_hdf5_structure(item, indent + 2)
        elif isinstance(item, h5py.Dataset):
            print(" " * indent + f"Dataset: {name} (Shape: {item.shape}, Dtype: {item.dtype})")

# Specify the HDF5 file path
hdf5_file_path = '/path/to/your/file.h5'

# Open the HDF5 file in read mode
with h5py.File(hdf5_file_path, 'r') as file:
    # Print the structure and contents starting from the root group
    print_hdf5_structure(file)