import json


ponya = {"Atomaru": "C", "Kanbara": "AA",
         "Hamuko": "E", "Konoha": "B", 
         "Mario": "F", "Gamera": "G", "oppai": {"size": "chiisai", "cup": 26}}

def get_value(table: dict, *args: str):
    assert (type(table) == dict)
    result = table
    for key in args:
        result = result[key]

    return (result)


def edit_value(table: dict, *args: str) -> None:
    assert (type(table) == dict)
    result = table
    for key in args:
        result = result[key]

    return (result)

# with open(f"data/sample.json", mode="w") as f:
#     json.dump(ponya, f, indent=4)