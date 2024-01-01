import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import pydicom

data_paths = [
    "D:\\Norsvin - CT Segmentation Data\\AHFP-Scanrunde-1\\Kontroll 1 - 7569 - Norsvin AHFP\\Hjerte med kontrast (heart with contrast)\\DICOM\\ST00001\\SE00001\\IM00001",
    "D:\\Norsvin - CT Segmentation Data\\AHFP-Scanrunde-1\\Kontroll 1 - 7569 - Norsvin AHFP\\Hjerte med kontrast (heart with contrast)\\DICOM\\ST00001\\SE00001\\IM00002",
    "D:\\Norsvin - CT Segmentation Data\\AHFP-Scanrunde-1\\Kontroll 1 - 7569 - Norsvin AHFP\\Hjerte med kontrast (heart with contrast)\\DICOM\\ST00001\\SE00001\\IM00003"
]




def con_hounsfield(scans):
    
    # Convert to Hounsfield units (HU)
    # getting slope & intercept
    slope = getattr(scans[0], 'RescaleSlope', 1.0)
    intercept = getattr(scans[0], 'RescaleIntercept', 0.0)
    
    # doing calculation if slope!=1 & intercept!=0
    if slope != 1:
        images = slope * scans.astype(np.float64)
        images = images.astype(np.int16)

    if intercept !=0:  
        images += np.int16(intercept)  
    
    return images

def read_dicom(paths):
    #reaing dicom files
    slices = [pydicom.read_file(path) for path in paths]
    
    # Convert to numpy
    scans = np.stack([s.pixel_array for s in slices])
    scans = scans.astype(np.int16)
    
    # convertin to range with in 0-1
    scaler = MinMaxScaler(feature_range=(0, 1))
    image_shape = scans[0].shape
    images = np.array([(scaler.fit_transform(img.reshape(-1,1))).reshape(image_shape) for img in scans],dtype=np.float32)

    return images

patient_pixels = read_dicom(data_paths)

# Visualize a slice
plt.imshow(patient_pixels[0][200], cmap='gray')
plt.show()
