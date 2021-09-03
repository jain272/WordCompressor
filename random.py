def compressWord(word, k):
    size = len(word) - k + 1
    if size < 0:
        return word
    for i in range(0, size):
        substr = word[i:(i + k)]
        k_char_cons = substr_check(substr)
        if k_char_cons:
            word = word.replace(substr, "")
            return compressWord(word, k)
    return word


def substr_check(substr):
    if len(set(substr)) == 1:
        return True
    return False
