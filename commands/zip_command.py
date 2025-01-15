import os
import tarfile
import shutil


#
# Handler to zip a file (ment to be used as a fake website later).s
#
def zip_command(params):  # params: [file_path, name_zip]
 
    if len(params) == 2:
        path = params[0]
        name = params[1]
        
        # Check if the directory exists
        if os.path.isdir(path):

            # Checking if the target file already exists
            target_path = os.path.join("web-templates", f"{name}.tar.gz")
            if os.path.exists(target_path):
                print(f"Error: A file named {name}.tar.gz already exists in the web-templates folder.")
            else:
                # Creating the tar.gz
                tar_gz_name = f"{name}.tar.gz"
                with tarfile.open(tar_gz_name, "w:gz") as tar:
                    # Use arcname to ensure no folder structure is added, just the content
                    for item in os.listdir(path):
                        item_path = os.path.join(path, item)
                        tar.add(item_path, arcname=item)  # Add content directly, not the directory itself
                
                # Move the tar.gz file to web-templates
                shutil.move(tar_gz_name, target_path)
                print(f"Folder {path} zipped and moved to web-templates.")
        else:
            print(f"The folder {path} does not exist.")
    else:
        print("You must specify the path of the folder to archive and the desired name of the archive.")
