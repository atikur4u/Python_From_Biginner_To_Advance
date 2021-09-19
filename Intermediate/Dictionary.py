dic = {1: 'Atik', 2: 'Rahman', 3: 'Ane'}
dic2 = 0

print(dic)
print("copy method:", dic.copy())

d = dict.fromkeys(dic, dic2)
print("FromKey() method:", d)

print("Key Method:", dic.keys())

print("Get Methods: ", dic.get(2))

print("Item Method: ", dic.items())  # make each key_value pair in tuple

dic.setdefault(4, 'tareq')
print("Dictionary after the setDefult method", dic)

dic.update({5: "mizan"})
print("Dictionary after update mehtod: ", dic)

print("Values Method: ", dic.values())

dic.pop(5)
print("dictionary after pop method: ", dic)

dic.popitem()
print("Dictionary after popitem method: ", dic)  # This method will remove the last item of the dictionary

print("Dictionary after clear method: ", dic.clear())