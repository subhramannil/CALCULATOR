from art import logo
print(logo)


a=int(input("What's the first number: "))
c=0
def sec():
    global c
    pick=input("+\n-\n*\n/\nPick an operation: ")
    b=int(input("What's the second number: "))
    if pick=="+":
        c=a+b
        print(c)
    elif pick=="-":
        c=a-b
        print(c)
    elif pick=="*":
        c=a*b
        print(c)
    elif pick=="/":
        c=a/b
        print(c)

sec()

again=True

while again:
    d=input("Type y to calculating with "+str(c)+",or type n to start a new calculation: ")
    if d=="y":
        pick=input("+\n-\n*\n/\nPick an operation: ")
        b=float(input("What's the second number: "))
        if pick=="+":
            c=c+b
            print(c)
        elif pick=="-":
            c=c-b
            print(c)
        elif pick=="*":
            c=c*b
            print(c)
        elif pick=="/":
            c=c/b
            print(c)
                
    elif d=="n":
        again=False
        print("Your final result is : "+str(c))
