# json to models
 
extracts python models from json files

## usage

- input: [./json_data](https://github.com/tesla-cat/json-to-models/tree/main/json_data)

```cmd
pip install json-to-models
```

```python
from json_to_models import JsonToModels

JsonToModels(data_dir='./json_data', root_name='Project')
```

- output: [models.py](https://github.com/tesla-cat/json-to-models/blob/main/models.py)
