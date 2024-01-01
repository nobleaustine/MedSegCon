import nibabel as nib
import matplotlib.pyplot as plt

def load_and_visualize_nii(nii_path):
    # Load NIfTI image
    nii_img = nib.load(nii_path)
    
    # Get the image data as a NumPy array
    nii_data = nii_img.get_fdata()
    flat_list = nii_data.flatten()

    print(set(flat_list))

    
    # Display three slices (axial, sagittal, coronal)
    plt.imshow(nii_data[:,200,:], cmap='gray')
    plt.show()

# Replace 'path/to/your/nii/file.nii' with the actual path to your NIfTI file
nii_file_path = "D:\\Norsvin - CT Segmentation Data\\AHFP-Scanrunde-1\\Kontroll 1 - 7569 - Norsvin AHFP\\Hjerte med kontrast\\DICOM\\ST00001\\SE00001\\IM00001.nii.gz"
load_and_visualize_nii(nii_file_path)