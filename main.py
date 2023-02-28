import json

ponya = {"Atomaru": "C", "Kanbara": "AA",
         "Hamuko": "E", "Konoha": "B", "Mario": "F"}


with open(f"data/sample.json", mode="w") as f:
    json.dump(ponya, f, indent=4)
