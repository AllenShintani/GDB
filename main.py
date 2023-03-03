import os
import json
from box import Box
from typing import Any

keyable = str | int | float | bool | None

ponya: dict = {"Atomaru": "C", "Kanbara": "AA",
               "Hamuko": "E", "Konoha": "B",
               "Mario": "F", "Gamera": "G",
               "oppai": {"A": 1, "B": 2, "C": {"D": 42}}
               }

def json_to_dict(name: str) -> dict:
    path: str = "data/" + name + "/sample.json"
    with open(path) as f:
        df: dict = json.load(f)
    return (df)


def get_value(name: str, *args: keyable) -> Any:

    df: dict = json_to_dict(name)

    mybox: Box = Box(df, box_dots=True)
    keys: list = list()
    for key in args:
        keys.append(key)

    KEY: str = ".".join(keys)

    if (KEY == ''):
        return (df)
    return (mybox[KEY])


def edit_value(name: str, key: keyable, value: Any) -> None:
    path: str = "data/" + name + "/sample.json"
    make_branch(name)
    df: dict = json_to_dict(name)

    if not (key in df):
        raise KeyError(f"'{key}'")

    df[key] = value
    with open(path, mode='w') as f:
        json.dump(df, f, indent=4)


def add_value(name: str, key: keyable, value: Any) -> None:
    path: str = "data/" + name + "/sample.json"
    make_branch(name)
    df: dict = json_to_dict(name)

    if (key in df):
        raise KeyError(f"{key} is already exist")

    df[key] = value
    with open(path, mode='w') as f:
        json.dump(df, f, indent=4)


def make_branch(name: str) -> None:
    name = str(name)
    path: str = "data/" + name
    if (os.path.exists(path) == False):
        os.makedirs(path)

    if (os.path.exists(path + "/sample.json") == False):
        with open(path + "/sample.json", mode='w') as f:
            json.dump(dict(), f, indent=4)

make_branch("XXX")
add_value("XXX", "oppai", "Fcup")
print(get_value("XXX", "oppai"))
edit_value("XXX", "oppai", "Lcup")
print(get_value("XXX", "oppai"))
print(add_value("XXX", "ashi", "futomomo"))
print(get_value("XXX"))
edit_value("XXX", "ashi", "tsurutsuru")
print(get_value("XXX"))
add_value("XXX", "oppai", "Mcup")