
def show_pizza(collection):
    number_of_pizzas = len(collection)
    print(f"There's actually ({number_of_pizzas}) Pizzas in the List: ")
    print()
    for i in collection:
        print(i)
    # return collection


pizzas = ("BlowMinder", "NightStalker", "Fairyzzas", "OnceUponAtamscotta")
show_pizza(pizzas)
