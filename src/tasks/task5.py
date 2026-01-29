import string
from itertools import count
from to_do import TODO

def task5(text: str) -> dict[str, int]:

    result = {"vowels": 0,"consonants": 0,"numbers": 0}

    if text is None:
        return {"vowels": 0,"consonants": 0,"numbers": 0}

    for character in text:
        if character.isalpha():
            if character.lower() in ['a', 'e', 'i', 'o', 'u']:
                result["vowels"] += 1
            else:
                result["consonants"] += 1
        elif character.isdigit():
            result["numbers"] += 1

    return result

if __name__ == "__main__":

    print(task5(text="Hell0"))
    print(task5(text="Sophia3"))