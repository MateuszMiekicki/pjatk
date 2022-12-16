from treelib import Tree
import time

# reachable_states = {"Gdansk": [["Gdynia", 24], ["Koscierzyna", 58], ["Tczew", 33], ["Elbląg", 63]],
#                     "Gdynia": [["Gdansk", 24], ["Lebork", 60], ["Wladyslawowo", 33]],
#                     "Elblag": [["Gdansk", 63], ["Tczew", 53]],
#                     "Hel": ["Wladyslawowo", 35],
#                     "Wladyslawowo": [["Leba", 66], ["Hel", 35], ["Gdynia", 42]],
#                     "Tczew": [["Koscierzyna", 59], ["Gdansk", 33], ["Elbląg", 53]],
#                     "Leba": [["Ustka", 64], ["Lebork", 29], ["Wladyslawowo", 66]],
#                     "Lebork": [["Leba", 29], ["Slupsk", 55], ["Koscierzyna", 58], ["Gdynia", 60]],
#                     "Koscierzyna": [["Chojnice", 70], ["Bytow", 40], ["Lebork", 58], ["Gdansk", 58], ["Tczew", 59]],
#                     "Ustka": [["Leba", 64], ["Slupsk", 21]],
#                     "Slupsk": [["Ustka", 21], ["Lebork", 55], ["Bytow", 70]],
#                     "Bytow": [["Slupsk", 70], ["Koscierzyna", 40], ["Chojnice", 65]],
#                     "Chojnice": [["Bytow", 65], ["Koscierzyna", 70]]}


def reachable_states(state):
    if state == "Gdansk":
        return [["Gdynia", 24], ["Koscierzyna", 58], ["Tczew", 33], ["Elblag", 63]]
    if state == "Gdynia":
        return [["Gdansk", 24], ["Lebork", 60], ["Wladyslawowo", 33]]
    if state == "Elblag":
        return [["Gdansk", 63], ["Tczew", 53]]
    if state == "Hel":
        return ["Wladyslawowo", 35]
    if state == "Wladyslawowo":
        return [["Leba", 66], ["Hel", 35], ["Gdynia", 42]]
    if state == "Tczew":
        return [["Koscierzyna", 59], ["Gdansk", 33], ["Elblag", 53]]
    if state == "Leba":
        return [["Ustka", 64], ["Lebork", 29], ["Wladyslawowo", 66]]
    if state == "Lebork":
        return [["Leba", 29], ["Slupsk", 55], ["Koscierzyna", 58], ["Gdynia", 60]]
    if state == "Koscierzyna":
        return [["Chojnice", 70], ["Bytow", 40], ["Lebork", 58], ["Gdansk", 58], ["Tczew", 59]]
    if state == "Ustka":
        return [["Leba", 64], ["Slupsk", 21]]
    if state == "Slupsk":
        return [["Ustka", 21], ["Lebork", 55], ["Bytow", 70]]
    if state == "Bytow":
        return [["Slupsk", 70], ["Koscierzyna", 40], ["Chojnice", 65]]
    if state == "Chojnice":
        return [["Bytow", 65], ["Koscierzyna", 70]]
    return []

def duplicate_node_path_check(tree, node):
    check_node = tree.get_node(node)
    current_node = check_node
    while not current_node.is_root():
        current_node = tree.parent(current_node.identifier)
        if check_node.tag == current_node.tag:
            return True
    return False

def dupilcate_node_path_check(tree,node_id):
    node = tree.get_node(node_id)
    current_node = node
    while not current_node.is_root():
        current_node = tree.parent(current_node.identifier)
        if current_node.tag[0] == node.tag[0]:
            return True
    return False


def breadth_first_search(start_state, target_state):
    id = 0
    fifo_queue = []
    tree = Tree()
    fifo_queue.append([start_state, 0, id])
    tree.create_node([start_state, 0, id], id)
    while True:
        print(fifo_queue)
        tree.show()
        if len(fifo_queue) == 0:
            print("failed to reach the target state")
            return 1
        temp = fifo_queue[0]

        if temp[0] == target_state:
            print("the target state " + temp[0] + " has been reached after " + str(temp[1]) + " kms!")
            return 0
        del (fifo_queue[0])
        if not (dupilcate_node_path_check(tree, temp[2])):
            for elem in reachable_states(temp):
                id += 1
                new_elem = [elem[0], temp[1] + elem[1], id]
                fifo_queue.append(new_elem)
                tree.create_node(new_elem, id, parent=temp[2])


def breadth_first_search2(start_state, target_state):
    id = 0
    fifo_queue = []

    tree = Tree()
    fifo_queue.append([start_state, 0, id])
    tree.create_node([start_state, 0, id], id)
    while True:
        print(fifo_queue)
        tree.show()
        if len(fifo_queue) == 0:
            print("failed to reach the target state")
            return 1
        temp = fifo_queue[0]

        if temp[0] == target_state:
            print("the target state " + temp[0] + " has been reached after " + str(temp[1]) + " kms!")
            return 0
        del (fifo_queue[0])
        for elem in reachable_states(temp):
            id += 1
            new_elem = [elem[0], temp[1] + elem[1], id]
            fifo_queue.append(new_elem)
            tree.create_node(new_elem, id, parent=temp[2])


start = time.time()
breadth_first_search("Gdansk","Ustka")
end = time.time()
time1 = end-start
print("--------------------------------------")
start1 = time.time()
breadth_first_search2("Gdansk","Ustka")
end1 = time.time()
time2 = end1-start1
print("--------------------------------------")
print("Z funkcją: " + str(time1) + ", bez funkcji: " + str(time2))