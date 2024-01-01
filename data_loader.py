# required libraries 
import h5py
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pydicom
import os
import random
import nibabel as nib

def read_nii_new(paths):
    niis = []
    for path in paths:
        if os.path.isfile(path):
            nii_slice = nib.load(path)
            niis.append(nii_slice)
        else:
            print(f"Error : {path}")
        labels = [nii.get_fdata() for nii in niis]
    return labels

# read DICOM images and rescale to 0-1
def read_dicom(paths):
    #reading dicom files
    slices = [pydicom.read_file(path) for path in paths]
    
    # Convert to numpy
    scans = np.stack([s.pixel_array for s in slices])
    scans = scans.astype(np.int16)
    
    # converting to range with in 0-1
    scaler = MinMaxScaler(feature_range=(0, 1))
    image_shape = scans[0].shape
    images = np.array([(scaler.fit_transform(img.reshape(-1,1))).reshape(image_shape) for img in scans],dtype=np.float32)

    return images

def read_dicom_new(paths):
    slices = []
    # dicom paths
    for path in paths:
        if os.path.isfile(path):
            dicom_slice = pydicom.read_file(path)
            slices.append(dicom_slice)
        else:
            print(f"Error : {path}")
    
    # Convert to numpy
    scans = np.stack([s.pixel_array for s in slices])
    scans = scans.astype(np.int16)
    
    # converting to range within 0-1
    scaler = MinMaxScaler(feature_range=(0, 1))
    image_shape = scans[0].shape
    images = np.array([(scaler.fit_transform(img.reshape(-1,1))).reshape(image_shape) for img in scans], dtype=np.float32)

    return images

# get nifti images
def read_nii(paths):
    # read and covert to numpy
    niis = [nib.load(path) for path in paths]
    labels = [nii.get_fdata() for nii in niis]

    return labels
    
# function to get all DICOM paths
def get_dicom_paths(root_path,animal_1):

    data = {}
    label = {}

    img1 =  "kontrast\DICOM\ST00001\SE00001\IM0000"
    img2 =  "kontrast i mageleie\DICOM\ST00001\SE00001\IM0000"
    
    raw_paths = []
    label_paths = []

    animal_1 = root_path + animal_1
    round_paths = []
    animal_paths = []
    
    # taking all rounds and animal paths
    round_paths = [os.path.join(root_path, d) for d in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, d))]
    animal_paths = [d for d in os.listdir(animal_1) if os.path.isdir(os.path.join(animal_1, d))]
    
    # going through each round and each animal and taking 1st and 5th
    for round in round_paths:
        for animal in animal_paths:
            main = round + "\\" + animal
            if os.path.isfile(main + "\Hjerte med " + img1 + "1") :
                file_path1 = main + "\Hjerte med " + img1 + "1"
                file_path2 = main + "\Hjerte uten " + img1 + "1"
                file_path3 = main + "\Hjerte med " + img1 + "1.nii.gz"
                raw_paths.append(file_path1)
                raw_paths.append(file_path2)
                label_paths.append(file_path3)
                label_paths.append(file_path3)

                file_path1 = main + "\Hjerte med " + img1 + "5"
                file_path2 = main + "\Hjerte uten " + img1 + "5"
                file_path3 = main + "\Hjerte med " + img1 + "5.nii.gz"
                raw_paths.append(file_path1)
                raw_paths.append(file_path2)
                label_paths.append(file_path3)
                label_paths.append(file_path3)
            else:
                file_path1 = main + "\Hjerte med " + img2 + "1"
                file_path2 = main + "\Hjerte uten " + img2 + "1"
                file_path3 = main + "\Hjerte med " + img2 + "1.nii.gz"
                raw_paths.append(file_path1)
                raw_paths.append(file_path2)
                label_paths.append(file_path3)
                label_paths.append(file_path3)

                file_path1 = main + "\Hjerte med " + img2 + "5"
                file_path2 = main + "\Hjerte uten " + img2 + "5"
                file_path3 = main + "\Hjerte med " + img2 + "5.nii.gz"
                raw_paths.append(file_path1)
                raw_paths.append(file_path2)
                label_paths.append(file_path3)
                label_paths.append(file_path3)

        

    combined_list = list(zip(raw_paths,label_paths))
    random.shuffle(combined_list)
    raw_paths,label_paths = zip(*combined_list)

    # check values by printing
    # for i,j in zip(raw_paths,label_paths):
    #     print(i)
    #     print(j)

    return raw_paths,label_paths

raw_paths,label_paths= get_dicom_paths("D:\\Norsvin - CT Segmentation Data","\\AHFP-Scanrunde-1") 
raw_data = read_dicom_new(raw_paths)
label_data = read_nii_new(label_paths)

# dataset path
file_path = 'dataset.h5'

# Create a new HDF5 file with raw and label
with h5py.File(file_path, 'w') as file:
   
    file.create_dataset('raw', data=raw_data)
    file.create_dataset('label', data=label_data)
