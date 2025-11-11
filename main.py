from stats import get_book_text
from stats import grep
from stats import get_num_charecter

path:str = "books/frankenstein.txt"
def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + path)
    print("----------- Word Count ----------")
    print("Found " + str(grep(get_book_text(path=path))) + " total words")
    print("--------- Character Count -------")
    print(get_num_charecter(get_book_text(path=path)))

main()