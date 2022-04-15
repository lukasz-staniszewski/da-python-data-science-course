import math


class Vertex(object):
    def __init__(self, v, p, d, is_terminal):
        """Vertex object representing single number in tree (vertex in graph)

        Args:
            v (bool): tells if vertex neighbours distances has been already counted
            p (int): index of vertex being predecessor in smallest path
            d (int): distance to starting vertex in smallest path
            is_terminal (bool): tells if such vertex is terminal (have no neighbours)
        """
        self.visited = v
        self.pred = p
        self.distance = d
        self.is_terminal = is_terminal


def findMax(vertexTab):
    """Function gives index of vertex which has largest distance to starting vertex
    and hasnt been visited already

    Args:
        vertexTab (list(Vertex)): list of Vertex objects

    Returns:
        int: index of not visited vertex with largest distance or -1 if every vertex visited
    """
    max = -1
    max_distance = -math.inf
    for vertex_nr in range(len(vertexTab)):
        if ((not vertexTab[vertex_nr].visited) and vertexTab[vertex_nr].distance > max_distance):
            max = vertex_nr
            max_distance = vertexTab[vertex_nr].distance
    return max


def Dijkstra(matrix, start, index_terminal_start):
    """Modified dijkstra algorithm

    Args:
        matrix (list(list(int))): matrix with wages of edges
        start (int): index of starting vertex
        index_terminal_start (int): index of vertex which starts terminal vertexes

    Returns:
        list(Vertex): list of vertexes with counted predecessors and distances to starting vertex
    """
    vertexTab = []
    number_of_vertexes = len(matrix)
    # creating vertex Tab with distances = inf and pred = -1
    for vertex_nr in range(number_of_vertexes):
        is_terminal = False
        if vertex_nr >= index_terminal_start:
            is_terminal = True
        vertexTab.append(Vertex(False, -1, -math.inf, is_terminal))
    # setting distance to starting vertex
    vertexTab[start].distance = 0
    u = start
    # while there is no vertex to visit left
    while(u != -1):
        # make actual vertex visited
        vertexTab[u].visited = True
        # for every neighbour of actual vertex do relaxation and set predecessor
        for i in range(u + 1, number_of_vertexes):
            if (matrix[u][i] > 0 and vertexTab[u].distance + matrix[u][i] > vertexTab[i].distance):
                vertexTab[i].distance = vertexTab[u].distance + matrix[u][i]
                vertexTab[i].pred = u
        # find next vertex in vertexTab with smallest distance or return -1 if all visited
        u = findMax(vertexTab)
    return vertexTab


def printInfo(vertexTab, values_tab):
    """Function prints informations:
        1) smallest path from starting vertex to one of terminals
        2) sum of numbers on given path
    Args:
        vertexTab (list(Vertex)): list of vertexes with counted predecessors and distances
        values_tab (list(int)): list of values of vertexes
    """
    best_paths_ends = []
    largest_path = -math.inf
    # search for terminal vertex(es) with smallest distance to starting vertex
    for ind, vertex in enumerate(vertexTab):
        if vertex.is_terminal:
            if vertex.distance > largest_path:
                best_paths_ends.clear()
                best_paths_ends.append(ind)
                largest_path = vertex.distance
            elif vertex.distance == largest_path:
                best_paths_ends.append(ind)
    # make list of strings representing best paths
    best_paths = []
    for path_end in best_paths_ends:
        best_paths.append(make_path(vertexTab, values_tab, path_end))
    print("PATHS:")
    for path in best_paths:
        print(path)
    print(f"SIZE: {largest_path+values_tab[0]}")
    print("~~~~~~")


def make_path(vertexTab, values_tab, index_end):
    """Function making string of path with given end of path
    by using predecessors

    Args:
        vertexTab (list(Vertex)): list of Vertexes with counted predecessors
        values_tab (list(int)): values of vertexes
        index_end (int): index of finishing path vertex

    Returns:
        str: path as string, ex: for path 1->2->3 returns 123
    """
    curr_index = index_end
    path = ""
    while vertexTab[curr_index].pred != -1:
        path = str(values_tab[curr_index]) + path
        curr_index = vertexTab[curr_index].pred
    return str(values_tab[0]) + path


def file_to_list(file_name):
    """Function creating list of values from file

    Args:
        file_name (str): name of file

    Returns:
        list(int): list of values from file
    """
    ret_list = []
    with open(file_name, 'r') as file:
        for line in file:
            ret_list.extend([int(s) for s in line.rstrip().split() if s.isdigit()])
    return ret_list


def make_matrix(values_tab):
    """Function makes matrix of edges' wages

    Args:
        values_tab (list(int)): list of values

    Returns:
        list(list(int)): matrix in which for every vertex there is wage
        of edge with its neighbour or 0 if edge doesnt exists
        int: number of values in last row of 'tree'
    """
    # creating matrix with zeros
    matrix = []
    for i in range(len(values_tab)):
        matrix.append([0 for _ in range(len(values_tab))])
    curr_row_len = 1
    counter = 0
    # adding values of edges
    for ind, row in enumerate(matrix):
        if ind + curr_row_len < len(matrix):
            row[ind + curr_row_len] = values_tab[ind + curr_row_len]
            row[ind + curr_row_len + 1] = values_tab[ind + curr_row_len + 1]
            counter += 1
            if counter >= curr_row_len:
                counter = 0
                curr_row_len += 1
        else:
            break

    return matrix, curr_row_len


def make_for_file(file_name):
    """Function makes full algorithm for given file

    Args:
        file_name (str): name of file
    """
    # make list of values from file
    values_tab = file_to_list(file_name)
    # make matrix of wages for graph
    matrix, last_row_length = make_matrix(values_tab)
    # make list of vertexes with counted distances and predecessors
    vertexTab = Dijkstra(matrix, 0, len(matrix) - last_row_length)
    # print paths and length of them
    printInfo(vertexTab, values_tab)


if __name__ == "__main__":
    make_for_file("1-vv_easy.txt")
    make_for_file("2-eeasy.txt")
    make_for_file("3-mmedium.txt")
