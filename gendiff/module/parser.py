import json
import yaml
from pathlib import Path


def parse(path):
    suffix = Path(path).suffix
    if suffix == ".json":
        return json.load(open(path))
    elif suffix == ".yaml" or suffix == ".yml":
        #print(yaml.safe_load(open(path)))
        return yaml.safe_load(open(path))
    else:
        raise Exception("Wrong Extension")
