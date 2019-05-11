import json


def json_load(value):
    file = open(value, "r").read()
    return json.loads(file)

def build_return(param, gui ,function):
    def ret_function():
        function(param)
    return ret_function()
