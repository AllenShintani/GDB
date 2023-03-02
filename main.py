import json
from box import Box
from typing import Any

hashable = int | str | tuple | frozenset

ponya: dict = {"Atomaru": "C", "Kanbara": "AA",
               "Hamuko": "E", "Konoha": "B",
               "Mario": "F", "Gamera": "G",
               "oppai": {"A": 1, "B": 2, "C": {"D": 42}}
               }


def json_to_dict(path: str) -> dict:
    with open(path) as f:
        df: dict = json.load(f)
    return (df)


def get_value(path: str, *args: hashable) -> Any:

    df: dict = json_to_dict(path)

    mybox: Box = Box(df, box_dots=True)
    keys: list = list()
    for key in args:
        keys.append(key)

    KEY: str = ".".join(keys)

    if (KEY == ''):
        return (df)
    return (mybox[KEY])


def edit_value(table: dict, *args: hashable) -> None:

    key_count: int = len(args)
    table_copy: dict = table.copy()

    for i in range(key_count - 1):
        table = {}


def add_value(path: str, *args: dict) -> None:
    dict_is_empty: bool

    if (len(args) == 0):
        dict_is_empty = True
    if (len(args) == 1):
        dict_is_empty = False
    if (len(args) >= 2):
        raise TypeError(
            "add_value() takes 0 or 1 positional arguments but more arguments were given")

    assert (type(args[0]) == dict)

    with open(path, mode='w') as f:
        if (dict_is_empty == True):
            f.write(json.dumps(dict(), indent=4))
        if (dict_is_empty == False):
            f.write(json.dumps(args[0], indent=4))


def make_branch(name: str) -> None:
    with open(f"ponya/{name}.json", mode='w') as f:
        f.write(json.dumps(dict(), indent=4))

make_branch("abcde")