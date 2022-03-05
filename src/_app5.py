import json
from multitracker import InitialCondition

initial_conditions_file = 'data-io/input/initial_conditions.json'


with open(initial_conditions_file) as json_file:
    data = json.load(json_file)
    print(data)
    list = []
    for item in data:
        initial_boundig_box = InitialCondition(item)
        list.append(initial_boundig_box)
