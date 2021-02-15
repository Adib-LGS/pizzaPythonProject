
def show_pizza(collection):
    number_of_pizzas = len(collection)
    if number_of_pizzas == 0:
        print("Sorry there's nothing yet")
    else:
        print(f"There's actually ({number_of_pizzas}) Pizzas in the List: ")
        for i in collection:
            print(i)
        print()

        print(f"First one: {collection[0]}")
        print(f"Last one: {collection[-1]}")

        """" Split to show First and Last Elements in List
        for i in collection[0::number_of_pizzas-1]:
            print(i)"""


pizzas = ("BlowMinder", "NightStalker", "Fairyzzas", "OnceUponAtamscotta")
show_pizza(pizzas)
