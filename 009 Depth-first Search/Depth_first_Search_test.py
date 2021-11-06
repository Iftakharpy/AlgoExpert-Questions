from Depth_first_Search import Node


def findNode(nodes, id):
    for node in nodes:
        if node["id"] == id:
            n = Node(node['value'])
            for ch in node['children']:
                n.children.append(findNode(nodes,ch))
            return n
                

def buildGraph(graph):
    nodes = graph['nodes']
    head = graph['startNode']
    return findNode(nodes, head)


def test_depthFirstSearch_case_1():
    graph = {'nodes': [{'children': ['B', 'C', 'D'], 'id': 'A', 'value': 'A'}, {'children': ['E', 'F'], 'id': 'B', 'value': 'B'}, {'children': [], 'id': 'C', 'value': 'C'}, {'children': ['G', 'H'], 'id': 'D', 'value': 'D'}, {'children': [], 'id': 'E', 'value': 'E'}, {'children': ['I', 'J'], 'id': 'F', 'value': 'F'}, {'children': ['K'], 'id': 'G', 'value': 'G'}, {'children': [], 'id': 'H', 'value': 'H'}, {'children': [], 'id': 'I', 'value': 'I'}, {'children': [], 'id': 'J', 'value': 'J'}, {'children': [], 'id': 'K', 'value': 'K'}], 'startNode': 'A'}
    graph = buildGraph(graph)
    res = ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'K', 'H']
    assert graph.depthFirstSearch([]) == res

def test_depthFirstSearch_case_2():
    graph={'nodes': [{'children': ['B', 'C'], 'id': 'A', 'value': 'A'}, {'children': ['D'], 'id': 'B', 'value': 'B'}, {'children': [], 'id': 'C', 'value': 'C'}, {'children': [], 'id': 'D', 'value': 'D'}], 'startNode': 'A'}
    graph = buildGraph(graph)
    res = ['A', 'B', 'D', 'C']
    assert graph.depthFirstSearch([]) == res

def test_depthFirstSearch_case_3():
    graph={'nodes': [{'children': ['B', 'C', 'D', 'E'], 'id': 'A', 'value': 'A'}, {'children': [], 'id': 'B', 'value': 'B'}, {'children': ['F'], 'id': 'C', 'value': 'C'}, {'children': [], 'id': 'D', 'value': 'D'}, {'children': [], 'id': 'E', 'value': 'E'}, {'children': [], 'id': 'F', 'value': 'F'}], 'startNode': 'A'}
    graph = buildGraph(graph)
    res = ['A', 'B', 'C', 'F', 'D', 'E']
    assert graph.depthFirstSearch([]) == res

def test_depthFirstSearch_case_4():
    graph={'nodes': [{'children': ['B'], 'id': 'A', 'value': 'A'}, {'children': ['C'], 'id': 'B', 'value': 'B'}, {'children': ['D', 'E'], 'id': 'C', 'value': 'C'}, {'children': ['F'], 'id': 'D', 'value': 'D'}, {'children': [], 'id': 'E', 'value': 'E'}, {'children': [], 'id': 'F', 'value': 'F'}], 'startNode': 'A'}
    graph = buildGraph(graph)
    res = ['A', 'B', 'C', 'D', 'F', 'E']
    assert graph.depthFirstSearch([]) == res

def test_depthFirstSearch_case_5():
    graph={'nodes': [{'children': ['B', 'C', 'D', 'E', 'F'], 'id': 'A', 'value': 'A'}, {'children': ['G', 'H', 'I'], 'id': 'B', 'value': 'B'}, {'children': ['J'], 'id': 'C', 'value': 'C'}, {'children': ['K', 'L'], 'id': 'D', 'value': 'D'}, {'children': [], 'id': 'E', 'value': 'E'}, {'children': ['M', 'N'], 'id': 'F', 'value': 'F'}, {'children': [], 'id': 'G', 'value': 'G'}, {'children': ['O', 'P', 'Q', 'R'], 'id': 'H', 'value': 'H'}, {'children': [], 'id': 'I', 'value': 'I'}, {'children': [], 'id': 'J', 'value': 'J'}, {'children': ['S'], 'id': 'K', 'value': 'K'}, {'children': [], 'id': 'L', 'value': 'L'}, {'children': [], 'id': 'M', 'value': 'M'}, {'children': [], 'id': 'N', 'value': 'N'}, {'children': [], 'id': 'O', 'value': 'O'}, {'children': ['T', 'U'], 'id': 'P', 'value': 'P'}, {'children': [], 'id': 'Q', 'value': 'Q'}, {'children': ['V'], 'id': 'R', 'value': 'R'}, {'children': [], 'id': 'S', 'value': 'S'}, {'children': [], 'id': 'T', 'value': 'T'}, {'children': [], 'id': 'U', 'value': 'U'}, {'children': ['W', 'X', 'Y'], 'id': 'V', 'value': 'V'}, {'children': [], 'id': 'W', 'value': 'W'}, {'children': ['Z'], 'id': 'X', 'value': 'X'}, {'children': [], 'id': 'Y', 'value': 'Y'}, {'children': [], 'id': 'Z', 'value': 'Z'}], 'startNode': 'A'}
    graph = buildGraph(graph)
    res = ['A', 'B', 'G', 'H', 'O', 'P', 'T', 'U', 'Q', 'R', 'V', 'W', 'X', 'Z', 'Y', 'I', 'C', 'J', 'D', 'K', 'S', 'L', 'E', 'F', 'M', 'N']
    assert graph.depthFirstSearch([]) == res

