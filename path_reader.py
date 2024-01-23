# entire path logic 
# only heart image with and without contrast 
# is used and image 1 and 5 (systol and dystol)
# thus for 1 animal in 1 round 4 images and 4 labels
# kontroll4 do not have round 4,5,6
# and kontroll3 and stent1 do not have round 6
# therefore total paths is
# round*animals*no_of_images - round_missed*no_of_dead_animals*no_of_images
# 6*10*4 - (3*1*4 + 1*2*4) = 240 - (12 +8) = 220
# each sub_raw_path contain 4 images of 1 animal in 1 round (systol and dystol with and without contrast)
# each sub_label_path contain 2 segmentations

# required libraries
import os
import pickle
# import random

# function to get paths of with and without contrast images 1 and 5
# systol and dystol
def get_paths(root_path,round_1):
    
    # two required images type
    img1 =  "kontrast\DICOM\ST00001\SE00001\IM0000"
    img2 =  "kontrast i mageleie\DICOM\ST00001\SE00001\IM0000"
    
    # collect all dicom images and labels
    raw_paths = []
    label_paths = []
    error_paths = []

    round_1 = root_path + round_1

    # taking all rounds and animal paths
    round_paths = [os.path.join(root_path, d) for d in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, d))]
    animal_paths = [d for d in os.listdir(round_1) if os.path.isdir(os.path.join(round_1, d))]
    
    # going through each round and each animal and taking 1st and 5th
    for i,round in enumerate(round_paths):
        print("round: ",i+1)
        for animal in animal_paths:
            sub_raw_paths = []
            sub_label_paths = []
            main = round + "\\" + animal
            if os.path.isfile(main + "\Hjerte med " + img1 + "1") :
                # file_path1 = main + "\Hjerte med " + img1 + "1"
                # file_path2 = main + "\Hjerte uten " + img1 + "1"
                # file_path3 = main + "\Hjerte med " + img1 + "1.nii.gz"
                sub_raw_paths.append(main + "\Hjerte med " + img1 + "1")
                sub_raw_paths.append(main + "\Hjerte uten " + img1 + "1")
                sub_label_paths.append(main + "\Hjerte med " + img1 + "1.nii.gz")

                # file_path1 = main + "\Hjerte med " + img1 + "5"
                # file_path2 = main + "\Hjerte uten " + img1 + "5"
                # file_path3 = main + "\Hjerte med " + img1 + "5.nii.gz"
                sub_raw_paths.append(main + "\Hjerte med " + img1 + "5")
                sub_raw_paths.append(main + "\Hjerte uten " + img1 + "5")
                sub_label_paths.append(main + "\Hjerte med " + img1 + "5.nii.gz")

            elif os.path.isfile(main + "\Hjerte med " + img2 + "1") :
                 # file_path1 = main + "\Hjerte med " + img2 + "1"
                # file_path2 = main + "\Hjerte uten " + img2 + "1"
                # file_path3 = main + "\Hjerte med " + img2 + "1.nii.gz"
                sub_raw_paths.append(main + "\Hjerte med " + img2 + "1")
                sub_raw_paths.append(main + "\Hjerte uten " + img2 + "1")
                sub_label_paths.append(main + "\Hjerte med " + img2 + "1.nii.gz")

                # file_path1 = main + "\Hjerte med " + img2 + "5"
                # file_path2 = main + "\Hjerte uten " + img2 + "5"
                # file_path3 = main + "\Hjerte med " + img2 + "5.nii.gz"
                sub_raw_paths.append(main + "\Hjerte med " + img2 + "5")
                sub_raw_paths.append(main + "\Hjerte uten " + img2 + "5")
                sub_label_paths.append(main + "\Hjerte med " + img2 + "5.nii.gz")
            else:
                error_paths.append(main)

            if not sub_raw_paths:
                print("scan missing")
            else:
              raw_paths.append(sub_raw_paths)
              label_paths.append(sub_label_paths)


    # combined_list = list(zip(raw_paths,label_paths))
    # random.shuffle(combined_list)
    # raw_paths,label_paths = zip(*combined_list)

    # check values by printing if label and image are matching
    # for i,j in zip(raw_paths,label_paths):
    #     print(i)
    #     print(j)

    return raw_paths,label_paths,error_paths

raw_paths,label_paths,error_paths = get_paths("D:\\Norsvin - CT Segmentation Data","\\AHFP-Scanrunde-1") 


# print error paths
print("error paths: ")
for i in error_paths :
    print(i)
print("length : ",len(raw_paths))

# cross checking
# for i in range(55):
#     print(i,raw_paths[i],label_paths[i])
#     print("------------------")

# saving as a pickle file
pickle_filename = 'list_of_paths.pickle'
with open(pickle_filename, 'wb') as file:
    pickle.dump({'raw_paths': raw_paths, 'label_paths': label_paths, 'error_paths': error_paths}, file)