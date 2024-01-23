import zipfile
import os

# files = []
# for i in range(0,55,5):
#     files_to_zip = []
#     for j in range(i,i+5):
#         files_to_zip.append(f'C:\\NOBLEAUSTINE\\GitWorld\\MedSegCon\\data\\set_{j}.h5')
#     files.append(files_to_zip)


# List of files to be included in the zip file
files_to_zip = ["C:\\NOBLEAUSTINE\\GitWorld\\MedSegCon\\data\\set_1.h5",
                  "C:\\NOBLEAUSTINE\\GitWorld\\MedSegCon\\data\\set_2.h5",
                   "C:\\NOBLEAUSTINE\\GitWorld\\MedSegCon\\data\\set_3.h5",
                    "C:\\NOBLEAUSTINE\\GitWorld\\MedSegCon\\data\\set_4.h5",
                     "C:\\NOBLEAUSTINE\\GitWorld\\MedSegCon\\data\\set_5.h5"]

# Name of the zip file to be created
zip_file_name = 'C:\\NOBLEAUSTINE\\GitWorld\\MedSegCon\\data\\c_1_5.zip'

# Create a zip file and add the specified files
with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in files_to_zip:
        if os.path.isfile(file):
            zipf.write(file, os.path.basename(file))
        elif os.path.isdir(file):
            for root, dirs, files in os.walk(file):
                for f in files:
                    file_path = os.path.join(root, f)
                    zipf.write(file_path, os.path.relpath(file_path, file))

print(f"File '{zip_file_name}' has been created.")
