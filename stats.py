def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    char_nums = {}
    for c in text:
        c = c.lower()
        char_nums[c] = char_nums.get(c, 0) + 1
    return char_nums

def sort_dict(char_num_dict):
    dict_list = []
    for c, n in char_num_dict.items():
        dict_list.append({"char": c, "num": n})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(dict):
    return dict["num"]

