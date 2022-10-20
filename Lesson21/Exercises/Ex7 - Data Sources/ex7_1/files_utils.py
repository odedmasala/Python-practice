import json
import os
import sys

path = os.path.join(sys.path[0], "persons.json")


def person_by_street(street):
    with open(path, "r") as f:
        data = json.load(f)
        persons = data["persons"]
        persons = list(
            filter(lambda per: per["address"]["street"]["name"] == street, persons)
        )
        persons = list(
            map(
                lambda per: {
                    "name": per["name"],
                    "city": per["address"]["city"],
                    "street": street,
                },
                persons,
            )
        )

    return persons
