def reverse_text(text):
    for num in range(len(text)-1,-1,-1):
        yield text[num]


