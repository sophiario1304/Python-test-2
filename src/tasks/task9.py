from to_do import TODO

def task9(sentence: str) -> int:

    points = {'a': 1,'e': 2,'r': 3,'t': 5,'s': 6}

    total = 0

    for character in sentence:

        if character.isalpha():
            lower_character = character.lower()

            if lower_character in points:
                total += points[lower_character]
            else:
                if character.islower():
                    total += 4
                else:
                    total += 8

    if sentence[-1].isdigit():
        total *= int(sentence[-1])

    result = total

    return result

if __name__ == "__main__":

    print(task9(sentence="StarterXb4"))
    print(task9(sentence="Sophia3"))


