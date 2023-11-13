import yaml
import json
import time

start_time = time.time()

fJSON = open('lab4JSON.json')
fYAML = open('lab4YAML.yaml', 'w')

parsed_json = json.load(fJSON)
yaml.dump(parsed_json, fYAML, allow_unicode=True)
fYAML.close()
end_time = time.time()
print(end_time - start_time)