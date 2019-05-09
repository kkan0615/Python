#If key is delta or value is 30, delete them
#input : alpha bravo charlie delta, 10 20 30 40. output : {'alpha': 10, 'bravo': 20}

keys = input().split()
values = map(int, input().split())

x = dict(zip(keys,values))
x = {key: value for key, value in x.items() if key != 'delta' if value != 30}

print(x)