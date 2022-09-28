import json
from time import time
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
from IPython.display import display
import time
import random
import os.path as os
# Goals of project:
#   Keep track of incoming comics
#   Keep track of outgoing comics
#   Keep running stock
#   Track location of comics in store
#       Define locations of comics in store - combo of publisher and title
#           Publisher:
#               Marvel
#               DC
#               Dark Horse
#               Image
#               IDW Publishing
#               Valiant Comics
#   Should also probably define price

# Json dictionary to store comic information
comics = {1: {
            "title": "Batman: The Long Halloween",
            "publisher": "DC",
            "price": 20.99,
            "quantity": 20
            },
        2: {
            "title": "Batman: Year One",
            "publisher": "DC",
            "price": 15.00,
            "quantity": 13
            },
        3: {
            "title": "The Umbrella Academy: Apocalypse Suite",
            "publisher": "Dark Horse",
            "price": 24.99,
            "quantity": 15
            },
        4: {
            "title": "The Umbrella Academy: Dallas",
            "publisher": "Dark Horse",
            "price": 24.99,
            "quantity": 14
            },
        5: {
            "title": "The Umbrella Academy: Hotel Oblivion",
            "publisher": "Dark Horse",
            "price": 24.99,
            "quantity": 9
            },
        6: {
            "title": "Edge of Spider-Verse",
            "publisher": "Marvel",
            "price": 13.99,
            "quantity": 25
            },
        7: {
            "title": "Ultraman: The Mystery of Ultraseven",
            "publisher": "Marvel",
            "price": 14.99,
            "quantity": 13
            },
        8: {
            "title": "I Hate This Place",
            "publisher": "Image",
            "price": 12.95,
            "quantity": 7
            },
        9: {
            "title": "Creepshow",
            "publisher": "Image",
            "price": 13.50,
            "quantity": 12
            },
        10: {
            "title": "The Walking Dead",
            "publisher": "Image",
            "price": 44.99,
            "quantity": 35 
            },

}

# Json dictionary to store customer data
cust_data = {

}

# Json dictionary to store purchase data 
purch_report = {

}
# Formatting dictionary into JSON
js = json.dumps(comics)
fd = open("data.json", 'w')
fd.write(js)
fd.close()

cd = json.dumps(cust_data)
fd = open("cust_data.json", 'w')
fd.write(cd)
fd.close()

pr = json.dumps(purch_report)
fd = open("purch_report", 'w')
fd.write(pr)
fd.close()

# Admin process for store owner/manager
# User level process for clerks

def admin():
    print("Welcome to admin functionality")
    while (1):
        print("1) Display Comic Database")
        print("2) Comic Search")
        print("3) Process Sale Transaction")
        print("4) Add New Comic")
        print("5) Update Comic")
        print("6) Delete Comic")
        print("7) Display Inventory Reports")
        print("8) Add Customer")
        print("9) User functionality")
        print("10) Exit")
        print("Enter your choice: ")

        n = int(input())
        if (n == 1):
            comic_database()
        elif (n == 2):
            comic_search()
        elif (n == 3):
            make_sale()
        elif (n == 4):
            add_new()
        elif (n == 5):
            update_comic()
        elif (n == 6):
            del_comic()
        elif (n == 7):
            inv_reports()
        elif (n == 8):
            new_cust()
        elif (n == 9):
            user()
        elif (n == 10):
            break
        else:
            print("Invalid input.")

def user():
    print("Welcome to user functionality")
    while (1):
        print("1) Display Comic Database")
        print("2) Comic Search")
        print("3) Process Sale Transaction")
        print("4) Admin Mode")
        print("5) Exit")

        n = int(input())
        if (n == 1):
            comic_database()
        elif (n == 2):
            comic_search()
        elif (n == 3):
            make_sale()
        elif (n == 4):
            admin()
        elif (n == 5):
            break
        else:
            print("Invalid input.")

# Defining all functions
def comic_database():
    fd = open("data.json", 'r')
    txt = fd.read()
    data = json.loads(txt)
    fd.close()
    print("Enter '0' to display comics based on Publisher or '1' to show comics in the order they were added:- ")
    n = int(input())

    if (n==1):
        table = pd.DataFrame(
            columns = ['ID', 'title', 'publisher', 'price', 'quantity'])
        # Creating Pandas dataframe to show data in table
        for i in data.keys():
            '''Fetch all keys in dictionary'''
            temp = pd.DataFrame(columns=['ID'])
            temp['ID'] = [i]

            for j in data[i].keys():
                temp[j] = [data[i][j]]
            table = table.append(temp)
        table = table.reset_index(drop=True)
        display(table)
    elif (n==0):
        table = pd.DataFrame(
            columns = ['ID', 'title', 'publisher', 'price', 'quantity'])
        
        pub = []

        for i in data.keys():
            temp = pd.DataFrame(columns=['ID'])
            temp['ID'] = [i]
            for j in data[i].keys():
                temp[j] = [data[i][j]]
                if (j == 'publisher'):
                    pub.append(data[i][j])
            table = table.append(temp)
            table = table.reset_index(drop = True)
            pub = set(pub)
            pub = list(pub)
        for k in pub:
            temp = pd.DataFrame()
            temp = table[table['publisher'] == k]
            print("Comics in inventory by publisher "+k+" are:- ")
            display(temp)
    else: 
        print("Enter a valid response.")
    comic_database()
def comic_search():
    fd = open("data.json", 'r')
    txt = fd.read()
    data = json.loads(txt)
    fd.close()
    print("Enter the ID for the comic you want to view:- ")
    i = input()
    if i in data.keys():
        temp = pd.DataFrame(columns=['ID'])
        temp['ID'] = [i]
        for j in data[i].keys():
            temp[j] = [data[i][j]]
        display(temp)
    else:
        print("You have entered an invalid ID. Do you need to add a comic to inventory?")
    comic_search()
def new_cust():
    pass
def trans_receipt(cust_id, prod_id, price, time_date, purchase_no, title, publisher, quantity_all, transaction_id):
    print("================================\
  ================= Bill ================\
  =================================")
    print("########################################")
    print("   Customer Loyalty ID :-", cust_id)
    print("############################################")
    amount = 0
    n = len(purchase_no)
    for i in range(n):
        print("--------------------------------------")
        amount = amount +float(price[i])*float(quantity_all[i])
        print("Purchase number", purchase_no[i],
        "\nPurchase time:- ", time_date[i],
        "\nComic ID:- ", prod_id[i],
        "\nTitle of Comic:- ", title[i],
        "\nPrice of Comic:- ", title[i],
        "\nPublisher of Comic:- ", publisher[i],
        "\nPurchase Quantity:- ", quantity_all[i])
        print("*********************************************************")
    print("      Total Payable Bill :-",
          amount, "Transaction ID :-", transaction_id)
    print("*************************************")


def make_sale():
    if (os.isfile("cust_data.json") is False):
        cust_data = {}
    else:
        fd = open("cust_data.json", 'r')
        txt = fd.read()
        cust_data = json.loads(txt)
        fd.close()



    fd = open("data.json", 'r')
    txt = fd.read()
    data = json.loads(txt)
    fd.close()
    p = int(input("Enter the customer's loyalty ID or press '0' to add a new customer:- "))
    cust_id = 0
    if (p == 0):
        if (len(cust_data.keys()) == 0):
            cust_id == 1000
        else:
            cust_id = int(list(cust_data.keys())[-1])+1
    else:
        if str(p) in cust_data.keys():
            cust_id = p
        else:
            cust_id = -1
    # Process purchase
    if (cust_id != -1):
        cust_id = str(cust_id)
        price = []
        time_date = []
        purchase_no = []
        title = []
        publisher = []
        price = []
        quantity_all = []
        prod_id = []
        transaction_id = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range (10))
        n = int(input("Number of comics being purchased:- "))
        print("Enter the following information:- ")
        if cust_id not in cust_data.keys():
            cust_data[cust_id] = {}
            g = 0
        else:
            g = int(list(cust_data[cust_id].keys())[-1])+1

        for i in range (n):
            print("Enter the comic ID for comic #"+str(i+1)+":- ")
            id = input()
            if id in data.keys():
                cust_data[cust_id][str(i+1+g)] = {}
                cust_data[cust_id][str(i+1+g)]['time_date'] = str(time.ctime())
                time_date.append(str(time.ctime()))
                if(int(data[id]['quantity']) == 0):
                    print("Sorry, this comic is out of stock.")
                    continue
                purchase_no.append(i+1+g)
                title.append(data[id]['title'])
                cust_data[cust_id][str(i+1+g)]['title'] = data[id]['title']
                prod_id.append(id)
                cust_data[cust_id][str(i+1+g)]['product_id'] = id
                publisher.append(data[id]['publisher'])
                cust_data[cust_id][str(i+1+g)]['publisher'] = data[id]['publisher']
                if (int(data[id]['quantity']) >= 1):
                    print("There are "+str(data[id]['quantity'])+" copies of "+str(data[id]['title'])+" available.")
                elif (int(data[id]['quantity']) == 1):
                    print("There is "+str(data[id]['quantity'])+" copy of "+str(data[id]['title'])+" available.")
                quantity = int(input("Enter how many for purchase:- "))

                if (int(quantity) <= int(data[id]['quantity'])):
                    data[id['quantity']] = int(data[id]('quantity'))-int(quantity)
                    quantity_all.append(quantity)
                    cust_data[cust_id][str(i+1+g)]['quantity'] = str(quantity)
                    quantity_all.append(quantity)
                    price.append(price)
                    cust_data[cust_id][str(i+1+g)]['price'] = data[id]['price']
                    cust_data[cust_id][str(i+1+g)]['Transaction ID'] = str(transaction_id)
                else:
                    print("You have requested to purchase more than is currently available.")
                    print("Press '0' to re-enter a valid amount, or '1' to skip this comic.")
                    key = int(input())
                    if (key == 0):
                        quantity = int(input("Enter how many for purchase:- "))
                        if (int(quantity) <= int(data[id]['quantity'])):
                            data[id['quantity']] = (int(data[id]['quantity'])-int(quantity))
                            quantity_all.append(quantity)
                            cust_data[cust_id][str(i+1+g)]['quantity'] = str(quantity)
                            quantity_all.append(quantity)
                            price.append(price)
                            cust_data[cust_id][str(i+1+g)]['price'] = data[id]['price']
                            cust_data[cust_id][str(i+1+g)]['Transaction ID'] = str(transaction_id)
                        else:
                            print("Oops, you did it again.")
                    elif (key == 1):
                        continue
                    else:
                        print("You've met with a terrible fate, haven't you?")
            else:
                print("The comic ID entered doesn't exist. Do you need to add a comic to inventory?")
        if(len(purchase_no) != 0):
            trans_receipt(cust_id, prod_id, price, time_date, purchase_no, title, publisher, quantity_all, transaction_id)
    else:
        print("This customer loyalty number doesn't exist. Do you need to create a new customer?")
    js = json.dumps(data)
    fd = open("data.json", 'w')
    fd.write(js)
    fd.close()

    js = json.dumps(cust_data)
    fd = open("cust_data.json", 'w')
    fd.write(js)
    fd.close

def add_new():
    fd = open("data.json", 'r')
    txt = fd.read()
    data = json.loads(txt)
    fd.close()
    print("Enter the new comic's ID:- ")
    id = input()

    if id not in data.keys():
        title = input("Enter the title of the comic:- ")
        publisher = input("Enter the publisher of the comic:- ")
        price = float(input("Enter the price of the comic:- "))
        quantity = int(input("Enter the amount of comics in inventory:- "))
        data[id] = {'title': title, 'publisher': publisher, 'price': price, 'quantity': quantity}
        print("You have successfully added the comic "+title+" to inventory.")
    else:
        print("The ID you are attempting to add already exists in the system.")
    js = json.dumps(data)
    fd = open("data.json", 'w')
    fd.write(js)
    fd.close       
def update_comic():
    pass
def del_comic():
    pass
def inv_reports():
    if (os.isfile("cust_data.json") is False):
        print("No customer data is available.")
        return

admin()