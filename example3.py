a=[[0]*4]*4
for elem in a: 
    print(elem)
for i in range(len(a)):
    for j in range(len(a[i])):
        if i == j:
            a[i][j] = 1
        else:
            a[i][j] = 2
    print(a[i])       	