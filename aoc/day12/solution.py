# Advent of Code - Day 12

from collections import defaultdict


def parse_to_graph(input):
    graph = defaultdict(list)

    for edge in input:
        a, b = edge.rstrip().split("-")

        if b != "start":
            graph[a].append(b)
        if a != "start":
            graph[b].append(a)
    return graph


def paths(graph, node_origin, destination_node):
    # Stack is list of tuples (node_to_visit, set_of_visited_nodes)
    stack = [(node_origin, {node_origin})]
    total = 0

    while stack:
        # print(f"Stack at beginning of check: {stack}")
        node, visited = stack.pop()
        # print(f"Node: {node}")
        # print(f"Visited: {visited}")

        # increment the count for each path to destination
        if node == destination_node:
            total += 1
            continue

        # print(f"Graph node: {graph[node]}")
        for n in graph[node]:
            print(f"n: {n}")
            # if lowercase and visited we can't continue
            if n in visited and n.islower():
                continue

            # perform a union to add the neighbour and visited nodes to the stack
            print(f"Union of visited and node: {visited | {n}}")
            stack.append((n, visited | {n}))

    return total


def paths_two(graph, node_origin, destination_node):
    # Stack is list of tuples (node_to_visit, set_of_visited_nodes, visited_twice:bool)
    stack = [(node_origin, {node_origin}, False)]
    total = 0

    while stack:
        # print(f"Stack at beginning of check: {stack}")
        node, visited, double = stack.pop()
        # print(f"Node: {node}")
        # print(f"Visited: {visited}")

        # increment the count for each path to destination
        if node == destination_node:
            total += 1
            continue

        # print(f"Graph node: {graph[node]}")
        for n in graph[node]:
            # print(f"n: {n}")
            if n not in visited or n.isupper():
                stack.append((n, visited | {n}, double))
                continue
            if double:
                continue
            # perform a union to add the neighbour and visited nodes to the stack
            stack.append((n, visited, True))

    return total


def result_part1(input):
    graph = parse_to_graph(input)
    return paths(graph, "start", "end")


def result_part2(input):
    graph = parse_to_graph(input)
    print(graph)
    return paths_two(graph, "start", "end")


sample_input = ["start-A", "start-b", "A-c", "A-b", "b-d", "A-end", "b-end"]
input = sample_input
# print(input)
# print(parse_to_graph(input))
# print(paths(input, "start", "end"))
# print(result_part1(input))
print(result_part2(input))
