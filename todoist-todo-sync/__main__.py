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
    #TODO: Refactor this stuff into the api package
    all_projects = requests.get("https://beta.todoist.com/API/v8/projects", headers={"Authorization": "Bearer %s" % config_dict["api"]["key"]}).json()
    cache_file = open(cache_file_path, 'r+')
    #TODO: in api crate implement equality check
    json.dump(all_projects, cache_file, sort_keys=True, indent=4)
    print(json.dumps(all_projects, sort_keys=True, indent=4))
    #print(config_dict["api"]["key"])
    

main()