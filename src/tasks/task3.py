from to_do import TODO

def task3(text: str) -> dict[str, int]:

    text = text.lower()

    words = text.split()

    result = {}

    for word in words:
        first = word[0]
        last = word[-1]

        if first == last:

            if first in ['a', 'e', 'i', 'o', 'u']:
                if first in result:
                    result[first] += 1
                else:
                    result[first] = 1

    return result
