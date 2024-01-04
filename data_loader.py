# required libraries 
import h5py
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pydicom
import os
import nibabel as nib
import pickle

def pad_and_stack(pixel_arrays):

    # Find the maximum size along the first axis
    max_size = max(arr.shape[0] for arr in pixel_arrays)

    # Create a list to store padded or cropped arrays
    padded_arrays = []

    # Pad or crop each array to the maximum size along the first axis
    for arr in pixel_arrays:
        # Calculate padding or cropping
        pad_width = ((0, max_size - arr.shape[0]), (0, 0), (0, 0))

        # Pad or crop along the first axis
        padded_array = np.pad(arr, pad_width, mode='constant', constant_values=0)

        # Append the padded or cropped array to the list
        padded_arrays.append(padded_array)

    # Stack the padded or cropped arrays along the first axis
    stacked_array = np.stack(padded_arrays, axis=0)

    return stacked_array

def add_matrix(hdf5_file, dataset_name, matrix):
    with h5py.File(hdf5_file, 'a') as file:
        # Create or open the dataset
        if dataset_name not in file:
            file.create_dataset(dataset_name, data=matrix, maxshape=(None, matrix.shape[1],matrix.shape[2],matrix.shape[3]), chunks=True)
        else:
            # Resize the dataset to accommodate the new matrix
            file[dataset_name].resize((file[dataset_name].shape[0] + 1), axis=0)
            file[dataset_name][-1, ...] = matrix

def read_nii_new(paths):
    niis = []
    
    for path in paths:
        if os.path.isfile(path):
            nii_slice = nib.load(path)
            niis.append(nii_slice)
        else:
            print(f"Error : {path}")

    segments = [nii.get_fdata() for nii in niis]
    segments = [np.transpose(s, (2, 0, 1)) for s in segments]
    labels = pad_and_stack(segments)

    return labels

def read_dicom_new(paths):
    slices = []
    # dicom paths
    for path in paths:
        # print("path ",path)
        if os.path.isfile(path):
            dicom_slice = pydicom.read_file(path)
            slices.append(dicom_slice)
        else:
            print("error",path)
    # max_z_size=[(s.pixel_array).shape for s in slices]
    slices = [s.pixel_array for s in slices]

    # Convert to numpy
    #scans = np.stack([s.pixel_array for s in slices])
    scans = pad_and_stack(slices)

    scans = scans.astype(np.int16)
    
    # converting to range within 0-1
    scaler = MinMaxScaler(feature_range=(0, 1))
    image_shape = scans[0].shape
    images = np.array([(scaler.fit_transform(img.reshape(-1,1))).reshape(image_shape) for img in scans], dtype=np.float32)

    return images

with open("paths_list.pickle","rb") as file:
    loaded_list = pickle.load(file)

raw_paths = list(loaded_list["final_raw"])
label_paths = list(loaded_list["final_label"])
c=1
for raw, label in zip(raw_paths,label_paths):
    print("LAP:",c)
    dicom_matrices = read_dicom_new(raw)
    nii_matrices = read_nii_new(label)
    file_name = f"Lap {c}.h5"
    
    print("hdf5 file uploading ...")
    add_matrix(file_name, "data", dicom_matrices)
    add_matrix(file_name, "label", nii_matrices)
    c+=1
