def get_num_words(contents:str):
    num_words =  len(contents.split())
    return num_words

def get_num_characters(contents:str):
    num_char = {}
    for i in contents.lower():
        if not i in num_char:
            num_char[i] = 1
        else:
            num_char[i] += 1
    return num_char
