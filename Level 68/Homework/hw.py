# Write a function that takes a list, an index, and an item, and inserts the item at the specified index.

def insert_at_index(lst, index, item):
    lst.insert(index, item)
    return lst

# Create a function that takes a list and a list of items, and appends each item to the original list.

def append_items(lst, items):
    for item in items:
        lst.append(item)
    return lst

# Create a function that appends all elements of one list to another list.

def append_lists(lst1, lst2):
    lst1.extend(lst2)
    return lst1
