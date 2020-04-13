
def earliest_ancestor(ancestors, starting_node):
    graph = {}
    for ancestor in ancestors:
        try:
            graph[ancestor[1]].add(ancestor[0])
        except:
            graph[ancestor[1]] = set()
            graph[ancestor[1]].add(ancestor[0])

    def get_parents(node):
        try:
            return graph[node]
        except:
            return None

    visited = set()
    global longest_path
    longest_path = [starting_node]
    def traverse(node, path):
        if node not in visited:
            visited.add(node)
            parents = get_parents(node)
            if parents:
                for parent in parents:
                    if parent not in visited:
                        new_path = path + [parent]
                        global longest_path
                        if len(new_path) > len(longest_path):
                            longest_path = new_path
                        elif len(new_path) == len(longest_path) and new_path[-1] < longest_path[-1]:
                            longest_path = new_path
                        traverse(parent, new_path)
    
    traverse(starting_node, [starting_node])

    if starting_node == longest_path[-1]:
        return -1
    else:
        return longest_path[-1]

