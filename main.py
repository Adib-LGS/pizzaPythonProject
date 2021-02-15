
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

        """" Split to show First and Last Elements in List(Tuple)
        for i in collection[0::number_of_pizzas-1]:
            print(i)"""


def add_pizza_user(collection):
    new_pizza = input("Add a new Pizza: ")
    collection.append(new_pizza)


pizzas = ["BlowMinder", "NightStalker", "Fairyzzas", "OnceUponAtamscotta"]
add_pizza_user(pizzas)
show_pizza(pizzas)
