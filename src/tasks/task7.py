import math
from typing import Any
from to_do import TODO

def task7(items: list[dict[str, Any]]) -> str:

    if len(items) == 0:
        return  ""

    lowest_price = math.inf
    result = ""

    for item in items:
        if item["price"] < lowest_price:
            lowest_price = item["price"]
            result = item["name"]

    return result


if __name__ == "__main__":


    print(task7(items=[{"name":"Apple","quantity": 4,"price":0.75}]))
    print(task7(items=[{"name":"Apple","quantity":4,"price":0.75},{"name":"Bread","quantity":2,"price":2.50}]))
    print(task7(items=[]))