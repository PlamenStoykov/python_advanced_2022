def words_sorting(*args):
    words = {}
    result_str = []
    for word in args:
        value = 0
        for letter in word:
            value += ord(letter)
            words[word] = value
    if not sum(words.values()) % 2 == 0:
        for word in sorted(words.items(), key=lambda x: -x[1]):
            result_str.append(f"{word[0]} - {word[1]}")
    else:
        for word in sorted(words.items(), key=lambda x: x[0]):
            result_str.append(f"{word[0]} - {word[1]}")
    return "\n".join(result_str)
