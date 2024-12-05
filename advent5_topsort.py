import random
from copy import deepcopy


def check_update(update, sorted_pages, island_pages):
    update_index = 0

    for sorted_pages_index in range(len(sorted_pages)):
        if update[sorted_pages_index] == sorted_pages[sorted_pages_index]:
            update_index += 1

    return update_index == len(update) - 1


def check_updates(updates, rules):
    correct = 0
    for update in updates:
        topological_sorted = topological_sort(rules)
        if topological_sorted:
            correct += check_update(update, *topological_sorted)

    return correct


def topological_sort(graph):
    """
    https://en.wikipedia.org/wiki/Topological_sorting
    """
    sorted_elements = []
    islands = set()

    while graph:
        node = random.choice(list(graph.keys()))
        edges = graph.pop(node)

        sorted_elements.append(node)

        for other_node, other_node_edges in graph.items():

            new_edges = deepcopy(graph[other_node])

            for other_node_edge in other_node_edges:
                if other_node_edge in edges:
                    new_edges.remove(other_node_edge)
                    if not new_edges:
                        islands.add(other_node)

            graph[other_node] = new_edges
    
    return sorted_elements, islands if not any(edges for _, edges in graph.items()) else None


graph = dict()
updates = []

# Parse input
with open("data/test.in") as file:

    parsing_rules = True
    for line in file:
        parsing_rules = parsing_rules and line != '\n'

        if parsing_rules:
            a, b = line.rstrip().split('|')
            graph.setdefault(int(a), set()).add(int(b))
        elif line != '\n':
            updates.append(
                list(map(int, line.rstrip().split(',')))
            )

print(topological_sort(graph))
print(check_updates(updates, graph))
