from json_to_models import JsonToModels
import glob, json

jtm = JsonToModels(root_name='Root')

for path in glob.glob(f'./json_data/*.json'):
    print(path)
    with open(path) as f:
        data = json.load(f)
    jtm.extract_models(data)   

jtm.write_models()
