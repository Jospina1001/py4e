purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)

print(purse['candy'])

purse['candy'] = purse['candy'] + 2
print(purse['candy'])

print(list(purse))
print(purse.keys())
print(purse.values())
print(purse.items())

for aaa,bbb in purse.items():
    print(aaa,bbb)
