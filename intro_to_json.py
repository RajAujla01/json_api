import json

car_data = {
    "name": "tesla",
    "engine": "electric",
}

print(type(car_data))

# json.dumps() --> turn python dict to str
car_data_json_string = json.dumps(car_data)
print(car_data_json_string)
print(type(car_data_json_string))


# json.dump() --> convert dict to str and put in file
with open("new_json_file.json", "w") as jsonfile:
    json.dump(car_data, jsonfile)


