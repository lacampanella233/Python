city = ['London','Beijing','Warsaw','Shanghai','New York']

print(city)

print(sorted(city))
print(city) # 这个输出应当保持原来的顺序不变

print(sorted(city,reverse=True))
print(city) # 这个输出应当保持原来的顺序不变

city.reverse()
print(city) # 这个输出应当与原列表反序.

city.reverse()
print(city) # 这个输出应当与原列表相同.

city.sort()
print(city) # 这个输出应当与原列表按升序进行排序后的顺序相同.

city.sort(reverse=True)
print(city) # 这个输出应当与原列表按降序进行排序后的顺序相同.

