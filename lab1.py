def d(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def parser(s: str):
    return int(s.split(' ')[0]), int(s.split(' ')[1])


def parse_file(file='input.txt'):
    with open(file, 'r') as input:
        lines = input.readlines()
        return set(parser(s) for s in lines[1:]), len(lines) - 1


def get_dict(graph, N):
    dict_d = {}
    graph_array = list(graph)
    dict_p = dict((graph_array[i], i + 1) for i in range(N))
    for i in range(1,N+1):
        dict_p[i] = graph_array[i-1]
        for j in range(1,N+1):
            if i != j:
                dict_d[(i, j)] = d(graph_array[i-1], graph_array[j-1])
    return dict_d, dict_p


def algorithm(graph: set, N):
    dict_d, dict_p = get_dict(graph, N)
    tree = set()
    tree.add(graph.pop())
    result = dict((i+1, []) for i in range(N))
    sum = 0
    for i in range(N-1):
        min = 2000000
        p1 = 0
        p2 = 0
        for p_tree in tree:
            for p_graph in graph:
                pn_tree = dict_p[p_tree]
                pn_graph = dict_p[p_graph]
                if min > dict_d[pn_tree, pn_graph]:
                    min = dict_d[pn_tree, pn_graph]
                    p1 = pn_tree
                    p2 = pn_graph
        sum += min
        result[p1].append(p2)
        result[p2].append(p1)
        tree.add(dict_p[p2])
        graph.remove(dict_p[p2])
    return result, sum


def ouput_answer(result, sum, N):
    with open('output.txt', 'w') as output:
        for i in range(1, N + 1):
            output.write(' '.join(str(x) for x in sorted(result[i])) + ' 0\n')
        output.write(str(sum) + '\n')



def main():
    graph, N = parse_file()
    result,sum = algorithm(graph, N)
    ouput_answer(result, sum, N)

if __name__ == '__main__':
    main()