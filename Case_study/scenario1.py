import json

json_file_path = r'D:\Case_study\pos_0.png.json'

formatted_file_path = r'D:\Case_study\formatted_pos_0.png.json'


def convert_json_format(json_file_path):
    # Read the JSON file
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # Modify the data according to the desired format
    formatted_data = {
        'formatted_file_name': 'formatted_pos_0.png.json',
        'data': data
    }

    return formatted_data


# Convert the JSON file to the standard format
formatted_data = convert_json_format(json_file_path)


# Write the formatted data to a new JSON file
with open(formatted_file_path, 'w') as f:
    json.dump(formatted_data['data'], f, indent=7)

print(f"Converted JSON file '{json_file_path}' to '{formatted_file_path}'.")
