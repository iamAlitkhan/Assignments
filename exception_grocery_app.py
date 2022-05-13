import traceback

class ShoppingList: 
  def __init__(self, title, address): 
    self.title = title 
    self.address = address 
    self.items = [] 

class Item: 
  def __init__(self, name): 
    self.name = name 

shopping_lists = [] 
while True: 
  print("Enter 1 to add shopping list: ")
  print("Enter 2 to add an item to a shopping list: ")
  print("Enter 3 to view shopping lists: ")
  print("Enter 4 to delete shopping list: ")
  print("Enter 5 to delete an item from a shopping list")
  print("Enter q to quit: ")
  choice = input("Enter choice: ")
  
  if choice == "1": 
    # ask user for title 
    title = input("Enter store title: ")
    # ask user for address 
    address = input("Enter store address: ")
    # create shopping list object 
    shopping_list = ShoppingList(title, address)
    # add shopping list object to shopping_lists array 
    shopping_lists.append(shopping_list)
  
  elif choice == "2":
    for index in range(0,len(shopping_lists)):
      print(f"{index + 1} - {shopping_lists[index].title} : {shopping_lists[index].address}")

    user_choice = int(input("Which shopping list you want to add items to: ")) - 1 

    shopping_list = shopping_lists[user_choice]
    item_name = input("Enter item name: ")
    item = Item(item_name)
    shopping_list.items.append(item)
    print("view shopping lists")
    
  elif choice == "3": 
    for index in range(0,len(shopping_lists)):
      print(shopping_lists[index].title)
      print(shopping_lists[index].address)
      for item in shopping_lists[index].items: 
        print(item.name)

  elif choice == "4":
    for index in range(0, len(shopping_lists)):
      print(f"{index + 1} - {shopping_lists[index].title}")
      for item in shopping_lists[index].items: 
        print(item.name)
        
    user_input = int(input("Which shopping list do you want to delete? ")) -1

    del shopping_lists[user_input]

  elif choice == "5":
    for index in range(0,len(shopping_lists)):
      print(f"{index + 1} - {shopping_lists[index].title}")
      
    user_entry = int(input("Which shopping list do you want to delete from? ")) - 1
      
    for index in range(0, len(shopping_lists[user_entry]).items):
        #print(item.name)
        print(shopping_lists[user_entry].items[index].name)
        
      # for item in shopping_lists[index].items: 
      #   print(item.name[user_entry])
      # for index in range(0,len(items)):
      #   print(f"{index + 1} - {shopping_lists[index].items}")

    # user_entry2 = int(input("Which item do you want to delete? ")) - 1
    # del shopping_lists[user_entry2]
   
  elif choice == "q":  
    break