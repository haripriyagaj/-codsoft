#calculator
def simple_calc(n1,n2):
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.multiplication")
    print("4.division")
    print("5.exit")
    while True:
        choice = int(input("enter choice:"))
        if choice=="1":
            add = n1+n2
        print(add)
        elif choice=="2":
            sub = n1-n2
        print(sub)
        elif choice=="3":
            multi = n1*n2
        print(multi)
        elif choice=="4":
            divi  = n1/n2
        print(divi)
        elif choice=="5":
            print("Exit the operation")
        break
    else:
        print("Invalid data")
    return
num1 = int(input("enter num1"))
num2 = int(input("enter num2"))
simple_calc(num1,num2)

