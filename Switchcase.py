def Number(spelling):
    g={1:'One',
       2:'Two',
       3: 'Three',
       4: 'Four',
       5: 'Five',
       6: 'Six',
       7: 'Seven',
       8:'Eight',
       9:'Nine',
       10:'Ten',

    }
    return g[spelling]
print("Enter 1 to 10 any number for spelling : ")
n=int(input())
print(Number(n))