


"""Store lookup script."""

stores = ('home_depot', 'walmart', 'target', 'costco', 'best_buy')

inventory = {
    'best_buy': ('tv', 'laptop', 'tablet', 'smartphone', 'headphones'),
    'costco': ('rice', 'chicken', 'vegetables', 'fruits', 'beef'),
    'home_depot': ('hammer', 'nails', 'screwdriver', 'drill', 'saw'),
    'walmart': ('bread', 'milk', 'eggs', 'cheese', 'butter'),
    'target': ('shirt', 'pants', 'jacket', 'shoes', 'hat')
}


customer = input("Enter customer name: ").strip().lower()
store = input("Enter store: ").strip().lower()
item = input("Enter item to purchase: ").strip().lower()



if store not in stores:
    print(f"Sorry {customer}, the {store} is not available. Please choose from one of the following {stores}.")
elif item in inventory.get(store, ()):
    print(f"Great work {customer}, you have successfully purchased {item} from {store}!")
else:
    # store exists but item not in that store
    choice = input(f"Sorry {customer}, the item {item} is not available in {store}. Would you like me to show you which stores have {item}? (y/n): ").strip().lower()
    if choice == 'y':
        available_stores = [s for s in stores if item in inventory.get(s, ())]
        if available_stores:
            print(f"The item {item} is available in the following stores: {', '.join(available_stores)}.")
        else:
            print(f"Sorry {customer}, the item {item} is not available in any store.")
    else:
        choice2 = input("Would you like to see the full inventory of all stores? (y/n): ").strip().lower()
        if choice2 == 'y':
            for s in stores:
                items = ', '.join(inventory.get(s, ()))
                print(f"{s.capitalize()} has the following items: {items}.")
                
        
