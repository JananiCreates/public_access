# crud_app.py

items = []

def create_item(item):
    items.append(item)

def read_items():
    return items

def update_item(index, new_value):
    if 0 <= index < len(items):
        items[index] = new_value

def delete_item(index):
    if 0 <= index < len(items):
        items.pop(index)

# Example use:
create_item("Apple")
create_item("Banana")
update_item(1, "Grapes")
delete_item(0)
print(read_items())  # ['Grapes']
