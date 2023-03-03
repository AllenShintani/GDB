import os
import json
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
    result: Any = df

    for key in args:
        result = result[key]

    if (len(args) == 0):
        return (df)
    return (result)


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

make_branch("test")
add_value("test", "mario", "F")
add_value("test", "Atomaru", "C")
add_value("test", "Kanbara", "AA")
edit_value("test", "Kanbara", "H")