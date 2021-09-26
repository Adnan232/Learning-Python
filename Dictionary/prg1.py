basket = {}
fruits = ['Apple', 'Orange', 'Apple', 'Grapes', 'Mango', 'Orange']
print('List of Items: ', fruits)
for fruit in fruits:
    # if fruit not in basket:
    #     basket[fruit] = 1
    # else:
    #     basket[fruit] = basket[fruit] + 1
    basket[fruit] = basket.get(fruit, 0) + 1
print(basket)
for key in basket:
    print(key, basket[key])

print(basket.keys())
print(basket.values())
print(basket.items())

for k, v in basket.items():
    print('Key: ', k, 'Value: ', v)