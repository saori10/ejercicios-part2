user_decision = input("¿Desea una pizza vegetariana o no vegetariana? ")


if user_decision.lower() in "vegetariana":
    menu_vegetarian = input("Para la siguiente pizza vegetariana, tenemos los siguientes ingredientes:\n -Pimiento\n -Tofu\n Elija uno: ")
    if menu_vegetarian.lower() in "tofu":
        print("La pizza elegida es vegetariana\n Y tiene los siguientes ingredientes:\n -Mozzarella\n -Tomate\n -Tofu") 
    else:
        print("La pizza elegida es vegetariana\n Y tiene los siguientes ingredientes:\n -Mozzarella\n -Tomate\n -Pimiento") 
elif user_decision.lower() in "no vegetariana":
    menu_no_vegetarian = input("Para la siguiente pizza no vegetariana, tenemos los siguientes ingredientes:\n -Pepperoni\n -Jamon\n -Salmon\n Elija uno: ")
    if menu_no_vegetarian.lower() in "pepperoni":
        print("La pizza elegida no es vegetariana\n Y tiene los siguientes ingredientes\n -Mozarrella\n -Tomate\n -Pepperoni")
    elif menu_no_vegetarian.lower() in "jamon":
        print("La pizza elegida no es vegetariana\n Y tiene los siguientes ingredientes\n -Mozzarella\n -Tomate\n -Jamon")
    else:
        print("La pizza elegida no es vegetariana\n Y tiene los siguientes ingredientes\n -Mozzarella\n -Tomate\n -Salmon")
else:
    print("No tenemos ese tipo de pizza")