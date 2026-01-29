import random

from to_do import TODO

def task6(membership: str) -> bool:

    result = False

    if membership is not None:

        parts = membership.split('-')
        if len(parts) == 2:
            year_part = parts[0]
            code_part = parts[1]

            if year_part.isdigit() and int(year_part) >= 2015 and len(year_part) == 4:

                if code_part.isdigit() and len(code_part) == 3:
                    result = True

    return result


if __name__ == "__main__":

        print(task6(membership="2020-345"))
        print(task6(membership="2015-000"))
        print(task6(membership="2014-123"))



