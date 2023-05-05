import json

def load_user_info():
    json_open = open('user_info.json', 'r')
    json_load = json.load(json_open)
    print(json_load)
    pass
