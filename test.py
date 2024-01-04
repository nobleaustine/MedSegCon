import pickle

with open("paths.pickle","rb") as file:
    loaded_list = pickle.load(file)

raw_paths = list(loaded_list["raw_paths"])
label_paths = list(loaded_list["label_paths"])

final_raw = []
final_label = []

n = len(raw_paths)
for i in range(0,n):
    if(i+9<n-1):
        chunk = raw_paths[i:i+9]
    else:
        chunk = raw_paths[i:n-1]
    final_raw.append(chunk)
        
    
n = len(label_paths)
for i in range(0,n):
    if(i+9<n-1):
        chunk = label_paths[i:i+9]
    else:
        chunk = label_paths[i:n-1]
    final_label.append(chunk)
    

pickle_filename = 'paths_list.pickle'
with open(pickle_filename, 'wb') as file:
    pickle.dump({'final_raw': final_raw, 'final_label': final_label}, file)

