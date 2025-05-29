def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    char_nums = {}
    for c in text:
        c = c.lower()
        char_nums[c] = char_nums.get(c, 0) + 1
    return char_nums
