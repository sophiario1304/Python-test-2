from to_do import TODO
def task3(text: str) -> dict[str, int]:

    words = text.lower().split()

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

if __name__ == "__main__":

    print(task3(text= "Anna area idea omega echo apple"))
    print(task3(text= "Hello world"))
