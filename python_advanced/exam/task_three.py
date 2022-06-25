def shopping_cart(*args):
    foods = {'Soup': [], 'Pizza': [], 'Dessert': []}
    for command in args:
        if command == 'Stop':
            break
        meal, product = command
        if len(foods['Soup']) < 3 and meal == 'Soup':
            if product not in foods[meal]:
                foods[meal].append(product)
        elif len(foods['Pizza']) < 4 and meal == 'Pizza':
            if product not in foods[meal]:
                foods[meal].append(product)
        elif len(foods['Dessert']) < 2 and meal == 'Dessert':
            if product not in foods[meal]:
                foods[meal].append(product)
    all_length = 0
    for i in foods:
        all_length += len(foods[i])
    if all_length == 0:
        result = "No products in the cart!"
        return result
    sorted_dict = sorted(foods.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ''
    for key, value in sorted_dict:
        result += f"{key}:\n"
        sorted_value = sorted(value)
        for j in sorted_value:
            result += f" - {j}\n"
    return result

