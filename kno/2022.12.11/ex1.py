from treelib import Tree, Node 
#tworzenie drzewa
tree = Tree()
tree.create_node("Harry", "h") # korzen
tree.create_node("Jane", "j", parent="h")
tree.create_node("Bill", "b", parent="h")
tree.create_node("Diane", "d", parent="j")
tree.create_node("Mary", "m", parent="d")
tree.create_node("Harry", "h2", parent="j")
#wyswietlenie drzewa
tree.show()
#wyswietlenie info o niektorych wierzcholkach
x = tree.get_node("m")
print(x.tag)
print(x.identifier)
y = tree.parent("m")
print(y.tag)
print(y.identifier)
z = tree.get_node("h")
print(z.tag)
print(z.is_root())
def duplicate_node_path_check(tree, node):
    #uzupelnij wnetrze funkcji
    #byc moze warto skorzystac z petli
    #petla dziala tak dlugo az zaglebi sie od node do korzenia
    #petla robi przeskoki z wierzcholka na ojca
    #gdy znajdziemy wierzcholki o tych samych tagach zwroc True
    #w przeciwnym wypadku zwroc False
    current_node = node
    while not current_node.is_root():
        current_node = tree.parent(current_node.identifier)
        if node.tag == current_node.tag:
            return True
    return False


x = tree.get_node("h2")
print(duplicate_node_path_check(tree,x))
x = tree.get_node("m")
print(duplicate_node_path_check(tree,x))