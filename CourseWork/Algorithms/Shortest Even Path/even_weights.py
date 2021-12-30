

def num_opt_even_weight_paths(graph, s):
    '''
    The num_opt_even_weight_paths function should return a dictionary mapping node v to the number of optimal
    paths of even weight from s to v.

    graph - an adjacency list of a DAG in the form {u: {v:w(u,v)} mapping nodes to a dictionary
            where the keys are their adjacencies and the values are the edge weights
            graph[u][v] would be equal to the weight of the edge u to v.
            you may assume that graph.keys() represents all nodes present
    s - start node

    return: a dictionary mapping node v to the number of optimal paths of even weight from s to v.
            optimal[s] should be 1.
    '''
    mem = {}
    reveresed_graph = {}

    for i in graph:
        reveresed_graph[i] = {}
    for j in graph:
        for out_going,w in graph[j].items():
            reveresed_graph[out_going][j] = w


    def paths_counter(s,u,even):
        # checking memoization table
        if (u,even) in mem:
            return mem[(u,even)]

        if s == u:
            tup = (0, 1) if even else (float('inf'), 0)
            mem[(u,even)] = tup
            return tup

        min_len,paths = float('inf'),0

        in_coming_neighbors = reveresed_graph[u]
        for v,weight in in_coming_neighbors.items():
            if weight % 2 == 0:
                l,n = paths_counter(s, v, even)
            else:
                l,n = paths_counter(s, v, not even)

            length = l + weight

            if length < min_len:
                min_len = length
                paths = 1 # reset number of paths
            elif length == min_len:
                paths += n

        mem[(u, even)] = (min_len, paths)

        return (min_len, paths)

    out = {}

    for point in graph:
        out[point] = paths_counter(s, point, True)[1]

    return out


if __name__ == "__main__":
    num_opt_even_weight_paths({"a":{"b":3, "c":5}, "b":{"c":3}, "c":{}}, "a")
    # should return {"a":1, "b":0, "c":1}

    num_opt_even_weight_paths({"a":{"b":3, "c":5, "d":2}, "b":{"c":3}, "d":{"c":4}, "c":{}}, "a")
    # should return {"a":1, "b":0, "c":2}
