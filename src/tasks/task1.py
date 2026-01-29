import math
from typing import Any
from to_do import TODO
def task1(library: dict[str, dict[str, Any]]) -> str:

    least_pages = math.inf
    result = ""

    for book,details in library.items():
        pages = details["pages"]
        genre = details["genre"]

        if pages < least_pages:
            least_pages = pages
            result = f"{book}-{genre}"

    return result

if __name__ == "__main__":

    #library= {"Clean Code":{"pages":464,"genre":"programming"},"The Hobbit":{"pages" 310,"genre":"fantasy"},"Short Stories":{"pages":120,"genre":"fiction"}}
    print(task1(library = {"Clean Code":{"pages":464,"genre":"programming"},"The Hobbit":{"pages":310,"genre":"fantasy"},"Short Stories":{"pages":120,"genre":"fiction"}}))
    print(task1(library= {'Tiny': {'pages': 50, 'genre': 'poetry'}, 'Medium': {'pages': 200, 'genre': 'essay'}, 'Large': {'pages': 800, 'genre': 'reference'}}))