try:
    while True:
        i=input("Enter item,price and quantity with space:")
        if i!="":
            a,b,c=i.split()
            b=int(b)
            c=int(c)
            print(a," ",b*c)
        else:
            break
except EOFError:
    pass
