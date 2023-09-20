
'''
Create a grocery list program. It will let the user
    1. Add something to the list
    2. Remove something from the list
    3. Show the list
    4. Clear the list

Let the interface be as follows: (>>> indicates user input)
'''


print("Welcome to the Grocery List Program. Use the following commands to interact with the list")
print("\t1. Add an item (add <item>)")
print("\t2. Remove an item (remove <item>)")
print("\t3. Show the list (show)")
print("\t4. Clear the list (clear)")
print("\t5. Exit (exit)")

list_name = input("Please name your grocery list: ")
grocery_list = []
input_element = input(">>> ")
input_command = input_element.split()

def add(item, g_list):
	g_list.append(item)
	return g_list

def remove(item, g_list):
	if item in g_list:
		g_list.remove(item)
	else:
		print(f"'{item}' is not in {list_name}.")
	return g_list

def show(g_list):
	if g_list == []:
		print(f"{list_name} is empty.")
	else:
		print(f"{list_name}:")
		for i in range(0, len(g_list)):
			print(f"\t {i+1}. {g_list[i]}")

def clear(g_list):
	g_list = []
	return g_list

while 'exit' not in input_command:
	if 'add' in input_command:
		grocery_list = add(input_command[1], grocery_list)
	elif 'remove' in input_command:
		grocery_list = remove(input_command[1], grocery_list)
	elif 'show' in input_command:
		show(grocery_list)
	elif 'clear' in input_command:
		grocery_list = clear(grocery_list)
	input_element = input(">>> ")
	input_command = input_element.split()