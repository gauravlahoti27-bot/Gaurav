print("Gautrav Lahoti B1 2501069")
my_list = ['MATHS','PYTHON','GRAPHICS']
print("the original list ",my_list)
choice=0
while choice <= 5:
    print("1 Insert String")
    print("2 Remove String")
    print("3 Update String")
    print("4 Sort String")
    choice=int(input("Enter Your Choice :"))

    if choice==1:
        element=input("Enter Element to Insert :")
        position=int(input("Enter the Index No :"))
        my_list.insert(position,element)
        print("my_list",my_list)
        print("\n")
                     
    elif choice==2:
        try:
            element=input("Enter Element to Remove :")
            my_list.remove(element)
            print("my_list",my_list)
        except ValueError:
            print("Element not found")
            print("\n")


    elif choice==3:
        try:
            old_element = input("Enter the element to update :")
            new_element = input("Enter the new element :")
            index = my_list.index(old_element)
            my_list[index] = new_element
            print("my_list",my_list)
        except ValueError:
            printf("Element not found")
            print("\n")

    elif choice==4:
        my_list.sort()
        print("my_list",my_list)
        print("\n")

    elif choice==5:
        print("Program Exited")
     
    else:
        print("Invalid choice, try again later :-)")
