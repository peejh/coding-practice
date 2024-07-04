# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/6660878585954304/6705546245832704

import timeit

def get_longest_chain(conns, existing_chain, curr_chain):
    curr = curr_chain[-1]
    subchains = []
    for i in conns[curr]:
        # print(i, subchains, curr_chain)
        if i in curr_chain:
            subchains.append(curr_chain)
        elif i in existing_chain and i not in existing_chain[i]:
            subchains.append([*curr_chain, *existing_chain[i]])
        else:
            subchains.append(get_longest_chain(conns, existing_chain, [*curr_chain, i]))
    # print(subchains)

    longest = []
    for subchain in subchains:
        if len(subchain) > len(longest):
            longest = subchain
        
    return longest

def min_height_trees(n, edges):

    # track direct connections
    dconns = {} # direct connections
    for i in range(n):
        dconns[i] = set()
    for e in edges:
        dconns[e[0]].add(e[1])
        dconns[e[1]].add(e[0])
    # print(dconns)

    # find longest chain from a given root
    chains = {}
    for i in range(n):
        chains[i] = get_longest_chain(dconns, chains, [i])
    # print(chains)        

    # find roots that has min longest chain
    roots = []
    min_height = 1000
    for i in range(n):
        curr_chain_len = len(chains[i])
        if curr_chain_len < min_height:
            min_height = curr_chain_len
            roots = []
            roots.append(i)
        elif curr_chain_len == min_height:
            roots.append(i)

    return roots

def min_height_trees_better(n, edges):

    # track direct connections
    dconns = {} # direct connections
    for i in range(n):
        dconns[i] = set()
    for e in edges:
        dconns[e[0]].add(e[1])
        dconns[e[1]].add(e[0])
    # print(dconns)

    # prune leaf nodes by layer
    while len(dconns) > 2:
        todelete = []
        for k, v in list(dconns.copy().items()):
            if len(v) == 1:
                todelete.append((k, v.pop()))
        for k, v in todelete:
            del dconns[k]
            dconns[v].remove(k)

    return list(dconns.keys())

if __name__ == "__main__":
    start = timeit.default_timer()
    print(min_height_trees(6, [[0,1],[0,2],[0,3],[0,4],[4,5]]))
    print(min_height_trees(2, [[0,1]]))
    print(min_height_trees(1, []))
    print(min_height_trees(3, [[0,1],[1,2]]))
    print(min_height_trees(4, [[1,0],[1,2],[2,3]]))
    print("CPU time:", timeit.default_timer() - start)

    start = timeit.default_timer()
    print(min_height_trees_better(6, [[0,1],[0,2],[0,3],[0,4],[4,5]]))
    print(min_height_trees_better(2, [[0,1]]))
    print(min_height_trees_better(1, []))
    print(min_height_trees_better(3, [[0,1],[1,2]]))
    print(min_height_trees_better(4, [[1,0],[1,2],[2,3]]))
    print("CPU time:", timeit.default_timer() - start)