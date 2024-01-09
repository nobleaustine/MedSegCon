import pickle

# open pickle file with all paths and taking all data 
with open("paths.pickle","rb") as file:
    loaded_list = pickle.load(file)

# taking image and label into separate lists
raw_paths = list(loaded_list["raw_paths"])
label_paths = list(loaded_list["label_paths"])

# to store list of divided paths : list of list of paths
final_raw = []
final_label = []

# converting to list of 5 paths for image
n = len(raw_paths)
for i in range(0,n,5):
    if(i+5<n-1):
        chunk = raw_paths[i:i+5]
    else:
        chunk = raw_paths[i:n-1]
    final_raw.append(chunk)      

# converting to list of 5 paths for label    
n = len(label_paths)
for i in range(0,n,5):
    if(i+5<n-1):
        chunk = label_paths[i:i+5]
    else:
        chunk = label_paths[i:n-1]
    final_label.append(chunk)
    
# checking lengths
print("total length",len(raw_paths))
print('total lists',len(final_raw))
print('length of 1 list',len(final_raw[0]))

# storing final lists of lists 
pickle_filename = 'paths_list.pickle'
with open(pickle_filename, 'wb') as file:
    pickle.dump({'final_raw': final_raw, 'final_label': final_label}, file)

