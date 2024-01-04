import os
import random
import pickle

def get_dicom_paths(root_path,animal_1):

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
    for i,round in enumerate(round_paths):
        print("round: ",i)
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

    # check values by printing if label and image are matching
    # for i,j in zip(raw_paths,label_paths):
    #     print(i)
    #     print(j)

    return raw_paths,label_paths

raw_paths,label_paths= get_dicom_paths("D:\\Norsvin - CT Segmentation Data","\\AHFP-Scanrunde-1") 

pickle_filename = 'paths.pickle'
with open(pickle_filename, 'wb') as file:
    pickle.dump({'raw_paths': raw_paths, 'label_paths': label_paths}, file)