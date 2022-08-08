def vowel_filter(function):
    def wrapper():
        text = function()
        return [i for i in text if i.lower() in 'aioeu']
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

