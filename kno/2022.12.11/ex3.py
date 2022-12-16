from treelib import Tree, Node
import time

# reachable_states = {"Gdańsk": [["Gdynia", 24], ["Kościerzyna", 58], ["Tczew", 33], ["Elbląg", 63]],
#                     "Gdynia": [["Gdańsk", 24], ["Lębork", 60], ["Władysławowo", 33]],
#                     "Elbląg": [["Gdańsk", 63], ["Tczew", 53]],
#                     "Hel": ["Władysławowo", 35],
#                     "Władysławowo": [["Łeba", 66], ["Hel", 35], ["Gdynia", 42]],
#                     "Tczew": [["Kościerzyna", 59], ["Gdańsk", 33], ["Elbląg", 53]],
#                     "Łeba": [["Ustka", 64], ["Lębork", 29], ["Władysławowo", 66]],
#                     "Lębork": [["Łeba", 29], ["Słupsk", 55], ["Kościerzyna", 58], ["Gdynia", 60]],
#                     "Kościerzyna": [["Chojnice", 70], ["Bytów", 40], ["Lębork", 58], ["Gdańsk", 58], ["Tczew", 59]],
#                     "Ustka": [["Łeba", 64], ["Słupsk", 21]],
#                     "Słupsk": [["Ustka", 21], ["Lębork", 55], ["Bytów", 70]],
#                     "Bytów": [["Słupsk", 70], ["Kościerzyna", 40], ["Chojnice", 65]],
#                     "Chojnice": [["Bytów", 65], ["Kościerzyna", 70]]}


def reachable_states(state):
    if state == "Gdańsk":
        return [["Gdynia", 24], ["Kościerzyna", 58], ["Tczew", 33], ["Elbląg", 63]]
    if state == "Gdynia":
        return [["Gdańsk", 24], ["Lębork", 60], ["Władysławowo", 33]]
    if state == "Elbląg":
        return [["Gdańsk", 63], ["Tczew", 53]]
    if state == "Hel":
        return ["Władysławowo", 35]
    if state == "Władysławowo":
        return [["Łeba", 66], ["Hel", 35], ["Gdynia", 42]]
    if state == "Tczew":
        return [["Kościerzyna", 59], ["Gdańsk", 33], ["Elbląg", 53]]
    if state == "Łeba":
        return [["Ustka", 64], ["Lębork", 29], ["Władysławowo", 66]]
    if state == "Lębork":
        return [["Łeba", 29], ["Słupsk", 55], ["Kościerzyna", 58], ["Gdynia", 60]]
    if state == "Kościerzyna":
        return [["Chojnice", 70], ["Bytów", 40], ["Lębork", 58], ["Gdańsk", 58], ["Tczew", 59]]
    if state == "Ustka":
        return [["Łeba", 64], ["Słupsk", 21]]
    if state == "Słupsk":
        return [["Ustka", 21], ["Lębork", 55], ["Bytów", 70]]
    if state == "Bytów":
        return [["Słupsk", 70], ["Kościerzyna", 40], ["Chojnice", 65]]
    if state == "Chojnice":
        return [["Bytów", 65], ["Kościerzyna", 70]]
    return []


def duplicate_node_path_check(tree, node):

    check_node = tree.get_node(node)
    current_node = check_node
    while not current_node.is_root():
        current_node = tree.parent(current_node.identifier)
        if check_node.tag == current_node.tag:
            return True
    return False


def breadth_first_search(start_state, target_state):
    # do budowy drzewa potrzebujemy dla kazdego wierzcholka id
    # bedziemy je pozniej inkrementowac
    id = 0
    # wrzucenie stanu startowego do drzewa (korzen) i kolejki
    tree = Tree()
    current_node = tree.create_node(start_state, id)
    fifo_queue = []
    fifo_queue.append(current_node)
    # petla szukajaca sciezki do stnau koncowego
    # robimy ograniczenie na max wierzcholkow (id<200000)
    while id < 200000:
        # jesli kolejka pusta to znaczy ze nie da sie dojsc do stanu koncowego
        # drukowanie kolejki: print(fifo_queue)
        if len(fifo_queue) == 0:
            tree.show()
            print("failed to reach the target state")
            return 1
        # jesli kolejka niepusta to wez pierwszy stan z kolejki
        current_node = fifo_queue[0]
        # jesli ten stan jest koncowy to zakoncz program z sukcesem
        if current_node.tag == target_state:
            tree.show()
            print("the target state "+str(current_node.tag)+" with id = "+str(current_node.identifier) +
                  "has been reached!")
            return 0
        # jesli stan niekoncowy to usun go z kolejki
        del(fifo_queue[0])
        # a nastepnie dodaj stany osiagalne z niego
        # na koniec kolejki i do drzewa
        if not duplicate_node_path_check(tree, id):
            for elem in reachable_states(current_node.tag):
                id += 1
                new_elem = tree.create_node(elem[0], id, parent=current_node.identifier)
                fifo_queue.append(new_elem)
    print("time limit exceeded")


print('def breadth_first_search')
start = time.time()
breadth_first_search("Gdańsk", "Ustka")
end = time.time()
print(end - start)


def deph_first_search(start_state, target_state):
    id = 0
    tree = Tree()
    current_node = tree.create_node(start_state, id)
    lifo_stack = []
    lifo_stack.insert(0, current_node)

    while id < 200000:
        if len(lifo_stack) == 0:
            tree.show()
            print("failed to reach the target state")
            return 1

        current_node = lifo_stack[0]
        if current_node.tag == target_state:
            tree.show()
            print("the target state " + str(current_node.tag) + " with id = " + str(current_node.identifier) +
                  "has been reached!")
            return 0

        del (lifo_stack[0])
        if not duplicate_node_path_check(tree, id):
            for elem in reachable_states(current_node.tag):
                id += 1
                new_elem = tree.create_node(elem[0], id, parent=current_node.identifier)
                lifo_stack.append(new_elem)
    print("time limit exceeded")


print('def deph_first_search')
start = time.time()
deph_first_search("Gdańsk", "Slupsk")
end = time.time()
print(end - start)