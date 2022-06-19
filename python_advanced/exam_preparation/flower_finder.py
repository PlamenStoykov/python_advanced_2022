from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())
special_words = {'rose': list('rose'), 'tulip': list('tulip'), 'lotus': list('lotus'), 'daffodil': list('daffodil')}
won = False


def checker(words, l):
    for current_word in words:
        if l in current_word:
            while l in words[current_word]:
                words[current_word].remove(l)
        if not words[current_word]:
            return words, current_word
    return words


while True:
    if not vowels:
        break
    if not consonants:
        break
    if won:
        break
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()
    tokens = checker(special_words, current_vowel)
    if len(tokens) == 2:
        won = True
        special_words = tokens[0]
        word = tokens[1]

    tokens_two = checker(special_words, current_consonant, )
    if len(tokens_two) == 2:
        won = True
        special_words = tokens_two[0]
        word = tokens_two[1]
if won:
    print(f"Word found: {word}")
else:
    print(f"Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
