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

customer_details = {'name': 'Mark', 'phone': '0123456789', 'house': '34', 'street': 'Ones', 'suburb': 'Twos'}


#print(customer_details['name'],"\n",customer_details['phone'],"\n",customer_details['house'],"\n",customer_details['street'],"\n",customer_details['suburb'])

#print("\nCustomer Name: {} Customer Phone: \n{} Customer House Number:\n{} Customer Street Name:\n{} Customer Suburb:\n{}".format(customer_details['name'],customer_details['phone'],customer_details['house'],customer_details['street'],customer_details['suburb']))

print(f"{customer_details['name']} {customer_details['phone']} {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")



count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
    count = count + 1