names = ["Mark", "Pheobe", "Sally", "Michael", "Denise", "Ellen", "Eris", "Moana", "Lewis", "Lara"]

# list of pizza names
pizza_names = ['Margherita','Pepperoni','Hawaiian','Cheese','Italian','Veggie','Vegan','Chicken Deluxe',
                'Mega Meat Lovers','Seafood Deluxe','Apricot Chicken Deluxe','BBQ Chicken Deluxe]']

# lists of pizza prices
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

# list to store ordered pizzas
order_list =['Margherita','Mega Meat Lovers','BBQ Chicken Deluxe','Hawaiian']
#list to store pizzas prices
order_cost =[8.50,13.50,13.50,5.50]

count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
    count = count + 1