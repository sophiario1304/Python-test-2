from to_do import TODO
import math
def task2(ratings: dict[str, list[float]]) -> str:

    highest_average = -math.inf
    result = ""

    for product in ratings:
        total = 0
        count = 0

        for value in ratings[product]:
            total += value
            count += 1

        average = total / count

        if average > highest_average:
            highest_average = average
            result = product

    return result

if __name__ == "__main__":

    print(task2(ratings={"Phone":[4.0, 5.0, 4.5],"Tablet":[3.5, 4.0, 4.0],"Laptop": [5.0, 4.5, 4.5]}))
