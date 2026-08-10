# 使用大写字母来代替披萨的名字

pizzas = ['A','B','C']
friend_pizzas = pizzas[:]

pizzas.append('D')
friend_pizzas.append('E')

print("My favorate pizzas are:")
for pizza in pizzas:
    print(pizza)
print("\n")

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
