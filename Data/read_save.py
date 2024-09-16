import json

# file path from where to read JSON
file_path = "Data/garage.json"

# read from json function
def read_json():
    with open(file_path, 'r') as f:
        data = json.load(f)
        return data

# save to json function    
def save_json(garage):
    with open(file_path, 'w') as f:   
        json.dump(garage, f)

