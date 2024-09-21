#this module will be where most functionality will be stored
#create your def blocks for the assignment in this module
#Use this  function that will return the item name and price for a given item code
# for example, find_menu_item('D2') should return Lemonade, and integer 3 as the result
import data
def get_item_information(item_code):
  """ this  function that will return the item name and price for a given item code.
    For example, find_menu_item('D2') should return Lemonade, and integer 3 as the result """
  for item in data.menu_items:
    item_number, item_name, item_price = item.split(' ')
    if item_number == item_code:
      return item_name.encode("ascii", "ignore").decode(), int(item_price)

def display_items():
  print("Menu:")
  for item in data.menu_items:
        item_number, item_name, item_price = item.split(' ')
        print(f"{item_number}: {item_name} - ${item_price}")


def get_item_number():
    #Prompts user for a valid item code and quantity.
    display_items()
    while True:
        order_item = input("Enter dish number and quantity (e.g., D1 2), or 'done' to finish: ")
        if order_item == 'done':
            return 'done'
        try:
            # Split user input into item_code and quantity
            item_code, quantity = order_item.split()
            quantity = int(quantity)  # Ensure quantity is an integer
            if item_code in data.all_items:
                return f"{item_code} {quantity}"  # Return the item code and quantity
            else:
                print("Invalid dish number. Please try again.")
        except ValueError:
            print("Invalid input format. Please enter a valid dish number and quantity.")
      
def display_current_order(order):
    #Displays the current items in the order.
    print("Current order:")
    
    # Debugging statement to see the structure of the current order
    print(f"Order list: {order}")
    
    for code, name, qty, price in order:
        price = int(price)  # Ensure price is an integer
        print(f"{code+name} - ${price}")