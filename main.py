def store_details():
    laptops = {}
    with open('lap.txt', 'r') as file:
        for line in file:
            name, brand, price, quantity, processor, graphics = line.strip().split(', ')
            laptops[name.upper()] = {'brand': brand, 'price': float(price.strip('$')), 'quantity': int(quantity), 'processor': processor, 'graphics': graphics}
    return laptops
