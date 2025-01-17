from datetime import datetime
import os

#
# Function checking/creating files to store the historic informations.
#     
def create_ip_file(folder_path,file_path):    
    # Does "history" exists ?
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    # Check if file already exists
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            pass  # Create an empty file

#
# Function, adding the domain name and the informations of an internet connection to the right file.
#
def add_to_history(IP, domain_name):
    folder_path = "history"
    file_path = os.path.join(folder_path, IP)

    create_ip_file(folder_path,file_path)

    now = datetime.now()
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, 'a') as file:
        file.write(f"{formatted}|||{domain_name}.\n")
    