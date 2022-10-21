import json


with open("goldenStandard.json", "r") as f1:
    file1 = json.loads(f1.read())
with open("test_file.json", "r") as f2:
    file2 = json.loads(f2.read())

for item in file2:
    if item not in file1:
        print(f"Found difference: {item}")
    
print('success')