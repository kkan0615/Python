def calc(x, y):
    return x+y, x-y, x*y, x//y

x,y = map(int, input().split())

a,s,m,d = calc(x,y)

print('Add: {0}, Sub: {1}, Mul: {2}, Div: {3}'.format(a,s,m,d))