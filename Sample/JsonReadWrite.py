import json

json_data = dict()

json_data["Key1"] = "Value1"
json_data["Key2"] = "Value2"

json_sub_data = dict()
json_sub_data["NewKey1"] = "NewValue1"
json_sub_data["NewKey2"] = "NewValue2"
json_sub_data["NewArrayValue"] = (1, 2, 3, 4, 5)

json_data["NewValues"]=json_sub_data

file_name = r".\Sample\sample_json.json"

with open(file_name, "w") as f:
    json.dump(json_data, f, indent=2)

with open(file_name) as f:
    json_data = json.load(f)

print(json_data)
print("Key1={0}".format(json_data["Key1"]))
print("NewKey1={0}".format(json_data["NewValues"]["NewKey1"]))