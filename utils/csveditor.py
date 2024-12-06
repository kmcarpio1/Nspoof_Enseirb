import csv
import json
import os

def update_csv_with_json(csv_file_path, json_data):

    try:
        data = json.loads(json_data)
    except json.JSONDecodeError:
        return

    if isinstance(data, list):
        print(data)
        return

    file_exists = os.path.isfile(csv_file_path)
    file_empty = not file_exists or os.path.getsize(csv_file_path) == 0

    writer = None
    reader = None
    fieldnames = []

    with open(csv_file_path, mode='a+', newline='', encoding='utf-8') as csvfile:
        if not file_empty:

            csvfile.seek(0)
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames if reader.fieldnames else []

            if not fieldnames:
                fieldnames = list(data.keys())

            new_keys = [key for key in data.keys() if key not in fieldnames]

            if new_keys:
                fieldnames.extend(new_keys)
                # Réécrire l'entête dans le fichier CSV
                csvfile.seek(0)
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

        if writer is None:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames or list(data.keys()))
            if file_empty:
                writer.writeheader()

        writer.writerow(data)
