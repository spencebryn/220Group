import json
from time import time
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
from IPython.display import display
import time
import random
import os.path 
import easygui as eg


# Creating Dictionary to store data

# comment in to reset dictionary
# comics = {1: {
#            "title": "Batman: The Long Halloween",
#            "publisher": "DC",
#            "price": 20.99,
#            "quantity": 20.0
#            },
#		2: {
#            "title": "Batman: Year One",
#            "publisher": "DC",
#            "price": 15.00,
#            "quantity": 13.0
#            },
#        3: {
#            "title": "The Umbrella Academy: Apocalypse Suite",
#            "publisher": "Dark Horse",
#            "price": 24.99,
#            "quantity": 15.0
#            },
#        4: {
#            "title": "The Umbrella Academy: Dallas",
#            "publisher": "Dark Horse",
#            "price": 24.99,
#            "quantity": 14.0
#            },
#        5: {
#            "title": "The Umbrella Academy: Hotel Oblivion",
#            "publisher": "Dark Horse",
#            "price": 24.99,
#            "quantity": 9.0
#            },
#        6: {
#            "title": "Edge of Spider-Verse",
#            "publisher": "Marvel",
#            "price": 13.99,
#            "quantity": 25.0
#            },
#        7: {
#            "title": "Ultraman: The Mystery of Ultraseven",
#            "publisher": "Marvel",
#            "price": 14.99,
#            "quantity": 13.0
#            },
#        8: {
#            "title": "I Hate This Place",
#            "publisher": "Image",
#            "price": 12.95,
#            "quantity": 7.0
#            },
#        9: {
#            "title": "Creepshow",
#            "publisher": "Image",
#            "price": 13.50,
#            "quantity": 12.0
#            },
#        10: {
#            "title": "The Walking Dead",
#            "publisher": "Image",
#            "price": 44.99,
#            "quantity": 35.0 
#            },
#
#}

# Formatting Dictionary into JSON format
#	js = json.dumps(comics)
#	fd = open("data.json", 'w')
#	fd.write(js)
#	fd.close() 

def admin():
	admin_text = "Welcome to the Admin Inventory Management System"
	admin_title = "Admin Inventory Management System"
	button_list = []
	button1 = "Display Comic Database"
	button2 = "Comic Search"
	button3 = "Add New Comic"
	button4 = "Update Comic"
	button5 = "Delete Comic"
	button6 = "Buy Comic"
	button7 = "Exit"
	button_list.append(button1)
	button_list.append(button2)
	button_list.append(button3)
	button_list.append(button4)
	button_list.append(button5)
	button_list.append(button6)
	button_list.append(button7)
	print("User selected option: ", end = " ")
	while (1):
		n = eg.buttonbox(admin_text, admin_title, button_list)
		if (n == button1):
			comic_database()
		elif (n == button2):
			comic_search()
		elif (n == button3):
			add_new()
		elif (n == button4):
			update_comic()
		elif (n == button5):
			delete_comic()
		elif (n == button6):
			buy_product()
		elif (n==button7):
			break
		else:
			print("Invalid Choice...!!!")


def comic_database():

	comicdb_text = "Comic Database"
	comicdb_title = "Comic Database"
	button_list = []
	button1 = "Display Comics by Publisher"
	button2 = "Display Comics in Order Added to Database"
	button3 = "Exit"
	button_list.append(button1)
	button_list.append(button2)
	button_list.append(button3)
	print("User selected option: ", end = " ")

	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	n = eg.buttonbox(comicdb_text, comicdb_title, button_list)


	
	# Display All Records
	if (n == button2):
		table = pd.DataFrame(
			columns=['ID', 'title', 'price', 'publisher', 'quantity'])
		
		# Creating Pandas dataframe to show data in table format later
		for i in data.keys():
		
			# Fetch all keys in dictionary
			temp = pd.DataFrame(columns=['ID'])
			temp['ID'] = [i]
			for j in data[i].keys():
				temp[j] = [data[i][j]]
			table = table.append(temp)
		table = table.reset_index(drop=True)
		'''This will reset index of dataframe'''
		from IPython.display import display
		display(table)
		eg.msgbox(table)
		
	elif (n == button1):
	
		# Display Records by publisher
		table = pd.DataFrame(
			columns=['ID', 'title', 'price', 'publisher',
					'quantity'])
		cat = []
		
		for i in data.keys():
			temp = pd.DataFrame(columns=['ID'])
			temp['ID'] = [i]
			for j in data[i].keys():
				temp[j] = [data[i][j]]
				if (j == 'publisher'):
					cat.append(data[i][j])
			table = table.append(temp)
			table = table.reset_index(drop=True)
			cat = set(cat)
			cat = list(cat)
			
		for k in cat:
			temp = pd.DataFrame()
			temp = table[table['publisher'] == k]
			eg.msgbox(msg = temp, title="Comics By Publisher", ok_button="OK")
	else:
		eg.msgbox("Please enter a valid response.")
		
# comic_database() # Uncomment This Line To Run This Function
def comic_search():

	intboxtext = "Enter ID of the comic to display details: "
	title = "Comic Search"
	d_int = 0
	lower = 0
	upper = 99999
	output = eg.integerbox(intboxtext, title, d_int, lower, upper)

	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	
	# Following Code will Filter out Product ID from Records
	i = str(output)
	if i in data.keys():
		temp = pd.DataFrame(columns=['ID'])
		temp['ID'] = [i]
		for j in data[i].keys():
			temp[j] = [data[i][j]]
		eg.msgbox(temp)
	else:
		eg.msgbox("Not a valid ID.")


# comic_search() # Uncomment This Line To Run This Function
def add_new():
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	intboxtext = "Enter ID of the comic to add: "
	title = "Comic Add"
	d_int = 0
	lower = 0
	upper = 99999
	output = eg.integerbox(intboxtext, title, d_int, lower, upper)
	id = str(output)
	
	if id not in data.keys():
		title = eg.enterbox(msg='Enter the name of the comic: ', title='Comic Add', default='', strip=True, image=None, root=None)
		output = eg.enterbox(msg='Enter the price of the comic: ', title='Comic Add', default='', strip=True, image=None, root=None)
		price = float(output)
		publisher = eg.enterbox(msg='Enter the publisher of the comic: ', title='Comic Add', default='', strip=True, image=None, root=None)
		intboxtext = "Enter the quantity in stock: "
		intboxtitle = "Comic Add"
		d_int = 0
		lower = 0
		upper = 99999
		output = eg.integerbox(intboxtext, intboxtitle, d_int, lower, upper)
		quantity = float(output)
		data[id] = {'title': title, 'price': price,
					'publisher': publisher, 'quantity': quantity}
		eg.msgbox("Comic "+str(title)+" added successfully.", "Comic Add")
	else:
		eg.msgbox("This comic already exists.")
	js = json.dumps(data)
	fd = open("data.json", 'w')
	fd.write(js)
	fd.close()
	
# add_new() # Uncomment This Line To Run This Function
def delete_comic():
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	output = eg.enterbox("Enter the ID of the comic you wish to delete: ", "Comic Delete")
	temp = str(output)
	if temp in data.keys():
		data.pop(temp)
		eg.msgbox("Comic ID "+str(temp)+" deleted successfully.", "Comic Delete")
	else:
		eg.msgbox("Invalid comic ID.", "Comic Delete")
	js = json.dumps(data)
	fd = open("data.json", 'w')
	fd.write(js)
	fd.close()
	
# delete_comic() # Uncomment This Line To Run This Function
def update_comic():
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	intboxtext = "Enter ID of the comic to update: "
	title = "Comic Update"
	d_int = 0
	lower = 0
	upper = 99999
	output = eg.integerbox(intboxtext, title, d_int, lower, upper)
	id = str(output)
	
	if id in data.keys():
		title = eg.enterbox(msg='Enter the name of the comic to update: ', title='Comic Update', default='', strip=True, image=None, root=None)
		output = eg.enterbox(msg='Enter the price of the comic: ', title='Comic Update', default='', strip=True, image=None, root=None)
		price = float(output)
		publisher = eg.enterbox(msg='Enter the publisher of the comic: ', title='Comic Update', default='', strip=True, image=None, root=None)
		intboxtext = "Enter the quantity in stock: "
		intboxtitle = "Comic Update"
		d_int = 0
		lower = 0
		upper = 99999
		output = eg.integerbox(intboxtext, intboxtitle, d_int, lower, upper)
		quantity = float(output)
		data[id] = {'title': title, 'price': price,
					'publisher': publisher, 'quantity': quantity}
		eg.msgbox("Comic "+str(title)+" updated successfully.", "Comic Add")
	else:
		eg.msgbox("This comic doesn't exist.")
	js = json.dumps(data)
	fd = open("data.json", 'w')
	fd.write(js)
	fd.close()
	
# update_comic() # Uncomment This Line To Run This Function


# display_reports_admin() # Uncomment This Line To Run This Function
def delete_all():
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	data = {} # Replacing Data with NULL Dictionary
	js = json.dumps(data)
	fd = open("data.json", 'w')
	fd.write(js)
	fd.close()


def user():
	userbuttontext = "Welcome to the User Inventory Management System."
	userbuttontitle = "User Iventory Management System"
	buttonlist = []
	button1 = "Display Comic Database"
	button2 = "Comic Search"
	button3 = "Buy Comics"
	button4 = "Exit"
	buttonlist.append(button1)
	buttonlist.append(button2)
	buttonlist.append(button3)
	buttonlist.append(button4)

	while (1):
		n = eg.buttonbox(userbuttontext, userbuttontitle, buttonlist)
		if (n == button1):
			comic_database()
		elif (n == button2):
			comic_search()
		elif (n == button3):
			buy_product()
		elif (n == button4):
			break
		else:
			print("Invalid Choice.")




def generate_bill(cust_id, prod_id, price, time_date, purchase_no, title, publisher, quantity_all, transaction_id):
    amount = 0
    n = len(str(purchase_no))
    purchase_no = str(purchase_no)
    for i in range(n):
        amount = amount +float(price[i])*float(quantity_all[i]) 
        limited_amount = "{:.2f}".format(amount)
        tax = amount*0.07
        limited_tax = "{:.2f}".format(tax)                                       #7%  salestax
        totalamount = amount + tax
        limited_totalamount = "{:.2f}".format(totalamount)
        eg.msgbox("Customer Loyalty ID: " +str(cust_id)+ 
		"\nProduct ID: " +str(prod_id)+ 
		"\nTitle: " +str(title)+
		"\nPrice: " +str(price)+
		"\nPublisher: " +str(publisher)+
		"\nPurchase Quantity: " +str(quantity_all)+
		"\n********************************************************* \nSubtotal :" +str(limited_amount)+ "Sales Tax (7%) :-"+str(limited_tax)+ "\nTotal Payable Bill :-"+str(limited_totalamount)+ "Transaction ID :-"+str(transaction_id)+"")
		



def buy_product():
	
	if (os.path.isfile("user_data.json") is False):
		user_data = {}
	else:
		fd = open("user_data.json", 'r')
		txt = fd.read()
		user_data = json.loads(txt)
		fd.close()
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()

	admin_text = "Comic Purchasing System"
	admin_title = "Comic Purchase"
	button_list = []
	button1 = "Existing User"
	button2 = "New User"
	button3 = "Exit"
	button_list.append(button1)
	button_list.append(button2)
	button_list.append(button3)
	
	while (1):
		n = eg.buttonbox(admin_text, admin_title, button_list)
		if (n == button2):
			if (len(user_data.keys()) == 0):
				user_id = 1000
				p = user_id
				if str(p) in user_data.keys():
					user_id = p
				else:
					user_id = -1
				if (user_id != -1):
					user_id = str(user_id)
					price = []
					time_date = []
					purchase_no = str(1)
					title = []
					publisher = []
					quantity_all = []
					prod_id = []
					transaction_id = ''.join(random.choice(
						'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(10))
				else:
					eg.msgbox("This is an invalid entry.")
					break
			else:
				intboxtext = "Enter User ID for New Customer (must be 1000 or greater): "
				intboxtitle = "Comic Purchase"
				d_int = 1000
				lower = 1000
				upper = 99999
				user_id_int = eg.integerbox(intboxtext, intboxtitle, d_int, lower, upper)
				p = str(user_id_int)
				if str(p) in user_data.keys():
					eg.msgbox("This user ID already exists.")
					break
				else:
					user_id = str(p)
					price = []
					time_date = []
					purchase_no = str(1)
					title = []
					publisher = []
					quantity_all = []
					prod_id = []
					transaction_id = ''.join(random.choice(
						'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(10))
		elif (n == button3):
			break
		elif (n == button1):
			intboxtext = "Enter the user ID for the customer who is checking out: "
			intboxtitle = "Comic Purchase"
			d_int = 1000
			lower = 1000
			upper = 99999
			output = eg.integerbox(intboxtext, intboxtitle, d_int, lower, upper)
			p = str(output)

			if str(p) in user_data.keys():
				user_id = p
			else:
				user_id = -1
			if (user_id != -1):
				user_id = str(user_id)
				price = []
				time_date = []
				purchase_no = str(1)
				title = []
				publisher = []
				quantity_all = []
				prod_id = []
				transaction_id = ''.join(random.choice(
					'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(10))
			else:
				eg.msgbox("This is an invalid entry.")
				break
		
		intboxtext = "Enter the number of comics to purchase: "
		intboxtitle = "Comic Purchase"
		d_int = 0
		lower = 0
		upper = 99999
		output = eg.integerbox(intboxtext, intboxtitle, d_int, lower, upper)
		n = int(output)
		if user_id not in user_data.keys():
			user_data[user_id] = {}
			g = 0
		else:
			g = int(list(user_data[user_id].keys())[-1])+1
		for i in range(n):
			intboxtext = "Enter comic ID for comic #" +str(i+1)+" that you want to buy: "
			intboxtitle = "Comic Purchase"
			d_int = 0
			lower = 0
			upper = 99999
			output = eg.integerbox(intboxtext, intboxtitle, d_int, lower, upper)
			id = str(output)
			if id in data.keys():
				user_data[user_id][str(i+1+g)] = {}
				user_data[user_id][str(i+1+g)]['time_date'] = str(time.ctime())
				time_date.append(str(time.ctime()))
				if(float(data[id]['quantity']) == 0.0):
					eg.msgbox("This comic is currently out of stock.")
					continue
				title.append(data[id]['title'])
				user_data[user_id][str(i+1+g)]['title'] = data[id]['title']
				prod_id.append(id)
				user_data[user_id][str(i+1+g)]['product_id'] = id
				publisher.append(data[id]['publisher'])
				user_data[user_id][str(
					i+1+g)]['publisher'] = data[id]['publisher']
				eg.msgbox("There are "+str(data[id]['quantity'])+
					" copies of " +str(data[id]['title']) + " available.")
				intboxtext = "Enter number of copies of comic #" +str(i+1)+" that you want to buy: "
				intboxtitle = "Comic Purchase"
				d_int = 0
				lower = 0
				upper = 99999
				output = eg.integerbox(intboxtext, intboxtitle, d_int, lower, upper)
				quantity = str(output)
				if (float(quantity) <= float(data[id]['quantity'])):
					data[id]['quantity'] = str(
						float(data[id]['quantity'])-float(quantity))
					quantity_all.append(quantity)
					user_data[user_id][str(i+1+g)]['quantity'] = str(quantity)
					price.append(data[id]['price'])
					user_data[user_id][str(i+1+g)]['price'] = data[id]['price']
					user_data[user_id][str(
						i+1+g)]['Transaction ID'] = str(transaction_id)
				else:
					eg.msgbox(
						"Sorry, you're trying to buy more than is in stock.")
					admin_text = "Select to change amount, or to skip this comic."
					admin_title = "Comic Purchase"
					button_list = []
					button1 = "Change Amount"
					button2 = "Skip Comic"
					button_list.append(button1)
					button_list.append(button2)
					
					key = eg.buttonbox(admin_text, admin_title, button_list)

					if (key == button1):
						intboxtext = "Enter number of copies of comic #" +str(i+1)+" that you want to buy: "
						intboxtitle = "Comic Purchase"
						d_int = 0
						lower = 0
						upper = 99999
						output = eg.integerbox(intboxtext, intboxtitle, d_int, lower, upper)
						quantity = str(output)
						if (float(quantity) <= float(data[id]['quantity'])):
							data[id]['quantity'] = str(
								float(data[id]['quantity'])-float(quantity))
							quantity_all.append(quantity)
							user_data[user_id][str(
								i+1)]['quantity'] = str(quantity)
							price.append(data[id]['price'])
							user_data[user_id][str(
								i+1)]['price'] = data[id]['price']
							user_data[user_id][str(
								i+1+g)]['Transaction ID'] = str(transaction_id)
						else:
							eg.msgbox("Invalid request repeated.")
							break
					elif (key == button2):
						continue
					else:
						eg.msgbox("Invalid choice.")
						break
			else:
				eg.msgbox("Invalid comic ID.")
				break
		if(len(purchase_no) != 0):
			generate_bill(user_id, prod_id, price, time_date, purchase_no,
						title, publisher, quantity_all, transaction_id)
	else:
		eg.msgbox("This user ID doesn't exist.")
		admin()
	js = json.dumps(data)
	fd = open("data.json", 'w')
	fd.write(js)
	fd.close()
	js = json.dumps(user_data)
	fd = open("user_data.json", 'w')
	fd.write(js)
	fd.close()


while (1):
	mainmenutext = "Welcome to the Inventory Management System."
	mainmenutitle = "Iventory Management System: Main Menu"
	buttonlist = []
	button1 = "Admin"
	button2 = "User"
	button3 = "Exit"
	buttonlist.append(button1)
	buttonlist.append(button2)
	buttonlist.append(button3)
	n = eg.buttonbox(mainmenutext, mainmenutitle, buttonlist)
	if (n == button1):
		admin()
	elif (n == button2):
		user()
	elif (n == button3):
		break
	else:
		print("Invalid Choice...!!!")
