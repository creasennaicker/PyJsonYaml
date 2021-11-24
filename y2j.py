import yaml, json


with open("verify.yaml", 'r') as yaml_in, open("verify.json", "w") as json_out:
    yaml_object = yaml.safe_load(yaml_in)
    json.dump(yaml_object, json_out)