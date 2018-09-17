#TODO: Trim imports
import os
import toml
import requests
import uuid
import json

def main():
    config_file_path = "{}/config.toml".format(os.getcwd())
    cache_file_path = "{}/cache.json".format(os.getcwd())
    #TODO: add try/catch block for redundancy
    config_dict = toml.load(config_file_path)
    api_key = config_dict["api"]["key"]
    config_file = open(config_file_path, "r+")
    # REFACTOR: turn this into a function all on it's own.
    if config_dict["project"]["todoist_id"] == "":
        todoist_project = requests.post(
            "https://beta.todoist.com/API/v8/projects", 
            data=json.dumps({
                "name": "%s" % config_dict["project"]["name"]
            }),
            headers={
                "Content-Type": "application/json",
                "X-Request-Id": str(uuid.uuid4()),
                "Authorization": "Bearer %s" % api_key
            }).json()
        config_dict["project"]["todoist_id"] = todoist_project["id"]
        config_file.truncate(0)
        toml.dump(config_dict, config_file)
        print("File created")
    
    keywords = (config_dict["project"]["keywords"])
    filenames = (config_dict["project"]["filetypes"])
    project_directory = "{}/{}".format(os.getcwd() ,config_dict["project"]["src_folder"])
    
    
    # NOTE: https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
    for subdir, dirs, files in os.walk(project_directory):
        for file in files: 
            filepath = subdir + os.sep + file

            if filepath.endswith(tuple(filenames)):
                print(filepath)
                # TODO: scan files for what is going on.
    
    
    
      

main()

"""
    #TODO: Refactor this stuff into the api package
    all_projects = requests.get("https://beta.todoist.com/API/v8/projects", headers={"Authorization": "Bearer %s" % config_dict["api"]["key"]}).json()
    cache_file = open(cache_file_path, 'r+')
    #TODO: in api crate implement equality check
    json.dump(all_projects, cache_file, sort_keys=True, indent=4)
    print(json.dumps(all_projects, sort_keys=True, indent=4))
    #print(config_dict["api"]["key"])
    """