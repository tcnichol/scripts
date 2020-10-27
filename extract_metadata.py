import json
import datetime
from datetime import datetime

def read_for_keys():

    metadata ={}

    keys_needed = ["owner", "unit", "created", "deadline"]
    with open('items.json') as f:
        items = json.load(f)

    for key in keys_needed:
        if key in items:
            metadata[key] = items[key]
        else:
            print(key + " is not in the file")
    print(metadata)

def dump_to_json():

    foods = {}
    foods["a"] = "apple"
    foods["b"] = "banana"
    foods["c"] = "carrot"
    foods["d"] = "date"
    foods["e"] = "eggplant"

    tools = {}

    tools["a"] = "axe"
    tools["b"] = "band saw"
    tools["c"] = "coping saw"

    items = {}
    items["foods"] = foods
    items["tools"] = tools
    items["owner"] = "John Smith"
    items["unit"] = "procurement"
    current_datetime = str(datetime.now())
    items["created"] = current_datetime

    with open('items.json', 'w') as fp:
        json.dump(items, fp)


if __name__ == '__main__':
    # dump_to_json()
    read_for_keys()
