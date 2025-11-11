def get_book_text(path:str) -> str:
    with open(path) as book:
        return book.read()

def grep(text:str) -> int:
    return len(text.split())

def get_num_charecter(text:str) -> dict[str, int]:
    return_value:dict[str, int] = dict()
    letters:list[str] = list(text)
    for letter in letters:
        if letter.lower() in return_value:
            return_value[letter.lower()] += 1
        else:
            return_value[letter.lower()] = 1
    return return_value

def sort_key(letter: dict[str, int]):
    return letter.values()
    
def sort_charecters(carechters:dict[str, int]) -> list[dict[str, int]]:
    sorted_list: list[dict[str, int]] = []
    for key, item in carechters.items():
        sorted_list.append({key: item})
    return sorted(sorted_list, key=sort_key)
        

print(sort_charecters(get_num_charecter(get_book_text("books/frankenstein.txt"))))