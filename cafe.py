#program to create a menu, with stock and pricing inforamtion as well as total stock worth
# list of menu
menu = ["chocolate", "toffee", "sherberts", "acid pops"]

# how much stock 
Stock_dic = {
            "chocolate": 5,
            "toffee": 2,
            "sherberts": 8,
            "acid pops": 10 }

# pricing for stock
price_dic = {
            "chocolate": 5,
            "toffee": 2,
            "sherberts": 8,
            "acid pops": 10}

#total stock worth
total_stock = 0.00
# price stock worth of each menu item printed
for item in menu:
    total_stock += Stock_dic[item] * price_dic[item]
    print("The stock worth of ", item,  "in the cafe is: £%.2f" % total_stock)

# price of all menu items printed 
total_stock = sum(Stock_dic[item] * price_dic[item] for item in menu)
print("The total worth of stock is £%.2f" % total_stock)
