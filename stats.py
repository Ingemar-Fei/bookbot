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

def sort_num_characters(dict_char:dict):
    def sort_on(dict):
        return dict['num']
    list_char_num = []
    for char in dict_char:
        if char.isalpha():
            list_char_num.append({"name":char,"num":dict_char[char]})
    list_char_num.sort(reverse=True,key=sort_on)
    return list_char_num 