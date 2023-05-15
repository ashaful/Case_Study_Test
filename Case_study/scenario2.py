import json
import os


def combine_and_modify_json(folder_path, output_file):
    combined_json = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            with open(os.path.join(folder_path, filename)) as file:
                data = json.load(file)

                # Modify class names
                for obj in data:
                    if 'class_name' in obj:
                        if obj['class_name'] == 'vehicle':
                            obj['class_name'] = 'car'
                        elif obj['class_name'] == 'license plate':
                            obj['class_name'] = 'number'

                combined_json.extend(data)

    with open(output_file, 'w') as outfile:
        json.dump(combined_json, outfile)


# Usage example
folder_path = r'D:\Case_study\combindJSON'
output_file = r'D:\Case_study\updatedJSON\output.json'

combine_and_modify_json(folder_path, output_file)
