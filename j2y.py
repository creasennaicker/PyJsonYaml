import yaml, json

with open("emojis.json", 'r') as json_in, open("emojis.yaml", "w") as yaml_out:
    json_object = json.load(json_in)
    yaml.dump(json_object, yaml_out)