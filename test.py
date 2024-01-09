import pydicom
import matplotlib.pyplot as plt

# Replace 'your_dicom_file.dcm' with the actual path to your DICOM file
dicom_file_path = "D:\\Norsvin - CT Segmentation Data\\AHFP-Scanrunde-1\\Kontroll 4 - 7570 - Norsvin AHFP\\Hjerte med kontrast\\DICOM\\ST00001\\SE00001\\IM00001"

# Read the DICOM file
dicom_data = pydicom.dcmread(dicom_file_path)

# Extract pixel data from the DICOM file
pixel_data = dicom_data.pixel_array

# Display the DICOM image using matplotlib
plt.imshow(pixel_data[:,:,200], cmap=plt.cm.gray)
plt.title('DICOM Image')
plt.show()