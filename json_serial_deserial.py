import json

records = {"student_records": [
    {"id": 1, "name": "ebuka", "age": 40},
    {"id": 2, "name": "torin", "age": 38},
    {"id": 3, "name": "sultan", "age": 30}
]}

print(records)

with open("records.json", mode="w") as rec:
    json.dump(records, rec)

with open("records.json", mode="r") as rec2:
    print(json.dumps(json.load(rec2), indent=4))
