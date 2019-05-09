#Find a boom in multi-dimention array
#

col = int(input("Type column : "))
row = int(input("Type row : "))
r = [-1, 1, 0 , 0, -1, 1, -1, 1]
c = [0, 0, -1, 1, -1, 1, 1, -1]

#ERROR IS ON HERE
boom = []
for i in range(row):
        boom.append(list(input()))

for i in range(0, col):
        for j in range(0, row):
                if boom[i][j] == '.' :
                        counts = 0
                        for k in range(8) :
                                nextX = i + c[k]
                                nextY = j + r[k]

                                if(nextX < 0 or nextY > 0 or nextX > col or nextY > row) :
                                        continue
                                
                                else :
                                        if(boom[nextX][nextY] == '*'):
                                                counts += 1

# Display boom map.
for i in range(col):
        for j in range(row):
                print(boom[i][j], end= '')
        print()

                                

