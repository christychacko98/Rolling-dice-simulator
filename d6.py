def nom():
         if num==1:
            print("---------")
            print("         ")
            print("    o    ")
            print("         ")
            print("---------")
            print()
         elif num==2:
            print("---------")
            print("         ")
            print("   o o   ")
            print("         ")
            print("---------")
            print()

         elif num==3:
            print("---------")
            print("  o   o  ")
            print("    o    ")
            print("         ")
            print("---------")
            print()

         elif num==4:
            print("---------")
            print("  o   o  ")
            print("  o   o  ")
            print("         ")
            print("---------")
            print()

         elif num==5:
            print("----------")
            print("  o     o ")
            print("     o    ")
            print("  o     o ")
            print("----------")
            print()

         else:
            print("---------")
            print(" o   o   ")
            print(" o   o   ")
            print(" o   o   ")
            print("---------")
            print()


import random
print("this is rolling dice program !!!")
print("lets start the program")
print("Please enter your details :")
print("Enter your name :")
c=input()
print("welecome to program")
lp=0
while lp !="q":
    print("press enter key to start your program:")
    input()
    n=int(input("enter any number:"))
    num=random.randint(1,6)
    print("random number is = ",num)
    print("your number is = ",n)
    nom()
    if n==num:
        print("hurray you win!!!!!!")
    else:
        print("awwww you loose ")
        print("try next time")
    print("type q to quit !!!!")
    lp=input()
