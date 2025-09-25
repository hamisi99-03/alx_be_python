shopping_list = []
def add_item(shopping_list, item):
    shopping_list.append(item)
    return shopping_list
def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
    return shopping_list
def view_list(shopping_list):
    return shopping_list    
