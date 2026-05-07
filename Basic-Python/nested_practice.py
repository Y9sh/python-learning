def multiplication_table():
    for i in range(1,6):
        for j in range(1,6):
            l = i * j 
            if l %3 == 0 :
                print(f"   -" , end=" ")
            else:
                print(f"{l:4}", end=" ")
        print()

multiplication_table()

def table_list(z): 
    x = []
    for l in range(1,z +1):
        y =[]
        for m in range(1,z+1):
            y.append(l*m)
        x.append(y)
    return x
print(table_list(2))


def mult_table():
    for j in range(5,10):
        for k in range(5,10):
            print(f"{j*k:4}",end=" ")
        print()
        
mult_table()


def pattern(n):
    for x in range(n+1):
        #print("* ", end=" ")
        for y in range(x):
            print("*",end=" ")
        print()

print(pattern(4))