import math


def construct_DAG(D):
    """
    Args:
         D, an array of deals, where each deal is of the form (A, x, B, y)
    Returns:
        Adjacency list, dictionary with product types as keys, a set of neighbors as values
        Weights dictionary for every edge (u,v) as keys, weight as values
    """
    Adj = {"super_node":set()}
    S = "super_node"
    weights = {}
    for deal in D:
        A, x, B, y = deal
        Adj[S].add(A)

        if A in Adj:
            Adj[A].add(B)
        else:
            Adj[A] = {B}
        if B not in Adj:
            Adj[B] = set()

        weights[(A,B)] = -math.log2(y/x)
        weights[(S,A)] = 0

    return Adj,weights


def relax(weights, d, parent, node, nxt):
    """
    the relax procedure
    updates the parent dictionary
    """
    if d[nxt] > d[node] + weights[(node,nxt)]:
        d[nxt] = d[node] + weights[(node,nxt)]
        parent[nxt] = node


def construct_cycle(v,parent):
    """
    Args:
        v: starting node
        parent: parent dictionary

    Returns: negative cycle

    """
    cycle = []
    visited = set()

    while v not in visited:
        visited.add(v)
        v = parent[v]

    while v not in cycle:
        cycle += [v]
        v = parent[v]
    cycle.reverse()
    return cycle if cycle else None



def bellman_ford(Adj, weights, source):
    """
    Args:
        Adj: adjacency list representing a DAG
        weights: weights of edges in DAG
        source: starting point
    Returns: list of nodes in negative cycle
    """
    inf = float('inf') # number greater than sum of all + weights
    d = {node:inf for node in Adj} # shortest path estimates d(s, v)
    parent = {node:None for node in Adj} # initialize parent pointers
    d[source], parent[source] = 0, source
    # construct shortest paths in rounds
    V = len(Adj) # number of vertices
    for i in range(V - 1): # relax all edges in (V - 1) rounds
        for node in Adj: # loop over all edges
            for nxt in Adj[node]: # relax edge
                relax(weights, d, parent, node, nxt)
    # check for negative weight cycles accessible from s
    for node in Adj: # Loop over all edges (u, v)
        for nxt in Adj[node]:
            if d[nxt] > d[node] + weights[(node, nxt)]: # If edge relax-able, construct the cycle
                return construct_cycle(nxt,parent)



def ez_money(D):
    """Find a sequence of commodities to exchange to get more of that
    commodity.

    Args:
        D: A list of deals, each deal is of the form (A, x, B, y)
           which means someone will give you y of B for x of A.

    Returns:
        None if no such opputunity is found, otherwise a List of
        commodities to exchange.
    """
    Adj,weights = construct_DAG(D)
    return bellman_ford(Adj,weights,"super_node")

