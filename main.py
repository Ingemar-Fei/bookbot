from stats import get_num_characters

def get_book_text(path_to_file:str):
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents

def main():
    contents = get_book_text(path_to_file="./books/frankenstein.txt")
    num_words = get_num_characters(contents)
    print(num_words)

main()