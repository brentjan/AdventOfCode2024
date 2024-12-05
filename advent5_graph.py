def check_update(update, inverted_graph):
    printed = set()

    for node in update:
        incoming_edges = inverted_graph.get(node, set())
        
        for incoming_edge in incoming_edges:
            if incoming_edge in update and incoming_edge not in printed:
                return False

        printed.add(node)

    return True


def correct_update(update, inverted_graph):
    correct_order = []

    # Pre-process
    relevant_graph = dict()
    for node in update:
        relevant_graph[node] = inverted_graph[node]

    # Determine correct order
    while update:
        i = 0
        node = update[i]

        while not all(node in edges if other_node != node else True for other_node, edges in relevant_graph.items()):
            i += 1
            node = update[i]
        
        update.remove(node)
        correct_order.append(node)
        relevant_graph.pop(node)
        
    return correct_order


def check_updates(updates, graph):
    inverted_graph = invert_graph(graph)
    middle_count = 0

    for update in updates:
        if not check_update(update, inverted_graph):
            new_update = correct_update(update, inverted_graph)
            middle_count += new_update[len(new_update) // 2]

    return middle_count


def invert_graph(graph):
    all_nodes = set(graph.keys())
    inverted_graph = dict()

    for node, edges in graph.items():
        inverted_edges = all_nodes.difference(edges).difference({node})
        inverted_graph[node] = inverted_edges

    return inverted_graph


# Variables
graph = dict()
updates = []

# Parse input
with open("data/advent5.in") as file:

    parsing_rules = True
    for line in file:
        parsing_rules = parsing_rules and line != '\n'

        if parsing_rules:
            a, b = line.rstrip().split('|')
            graph.setdefault(int(a), set()).add(int(b))

            if int(b) not in graph:
                graph[int(b)] = set()

        elif line != '\n':
            updates.append(
                list(map(int, line.rstrip().split(',')))
            )

print(check_updates(updates, graph))
