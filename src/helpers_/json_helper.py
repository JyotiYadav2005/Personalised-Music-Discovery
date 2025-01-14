'''
The purpose of this module is to ease the method of reading
and dumping data into json files into a single call method.
'''

import json, os, sys
project_root = os.getcwd()
sys.path.append(f'{project_root}/src/data')

# Dumps data into a json file
def dump_file(file, dump_this):
    # Dump to json
    with open(file, "w") as outfile:
        json.dump(dump_this, outfile,indent=4)

# Reads data from a json file
def read_file(file,default={}):
    # Read from json
    if os.path.getsize(file) == 0:
        return default
    
    else:
        with open(file) as data_file:
            data = json.load(data_file)
        return data

def count_data(dataset):
    leng = 0
    for key in dataset.keys():
        leng += len(dataset[key])
    return leng

if __name__ == "__main__":
    pass
    