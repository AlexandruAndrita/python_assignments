from vertex import Vertex
from edge import Edge


class Graph():
    def __init__(self):
        self.vertices = []  # list of vertices in the graph
        self.edges = []  # list of edges in the graph
        self.num_vertices = 0
        self.num_edges = 0
        self.undirected_graph = True

    def get_number_of_vertices(self):
        """
        :return: the number of vertices in the graph
        """
        return self.num_vertices

    def get_number_of_edges(self):
        """
        :return: the number of edges in the graph
        """
        return self.num_edges

    def get_vertices(self):
        """
        :return: list of length get_number_of_vertices() with the vertices of the graph
        """
        return self.vertices

    def get_edges(self):
        """
        :return: list of length get_number_of_edges() with the edges of the graph
        """
        return self.edges

    def insert_vertex(self, vertex_name):
        """
        Inserts a new vertex with the given name into the graph.
        Returns None if the graph already contains a vertex with the same name.
        The newly added vertex should store the index at which it has been added.

        :param vertex_name: The name of vertex to be inserted
        :return: The newly added vertex, or None if the vertex was already part of the graph
        :raises: ValueError if vertex_name is None
        """
        if vertex_name is None:
            raise ValueError("vertex_name is None")
        if self.find_vertex(vertex_name) is not None:
            return None
        index=len(self.vertices)
        new_vertex=Vertex(index,vertex_name)
        self.vertices.append(new_vertex)
        self.num_vertices+=1
        return new_vertex


    def find_vertex(self, vertex_name):
        """
        Returns the respective vertex for a given name, or None if no matching vertex is found.
        :param vertex_name: the name of the vertex to find
        :return: the found vertex, or None if no matching vertex has been found.
        :raises: ValueError if vertex_name is None.
        """
        if vertex_name is None:
            raise ValueError("vertex_name is None")
        for vertex in self.vertices:
            if vertex.name==vertex_name:
                return vertex
        return None

    def insert_edge_by_vertex_names(self, v1_name, v2_name, weight: int):
        """
        Inserts an edge between two vertices with the names v1_name and v2_name and returns the newly added edge.
        None is returned if the edge already existed, or if at least one of the vertices is not found in the graph.
        A ValueError shall be thrown if v1 equals v2 (=loop).
        :param v1_name: name (string) of vertex 1
        :param v2_name: name (string) of vertex 2
        :param weight: weight of the edge
        :return: Returns None if the edge already exists or at least one of the two given vertices is not part of the
                 graph, otherwise returns the newly added edge.
        :raises: ValueError if v1 is equal to v2 or if v1 or v2 is None.
        """
        if v1_name is None or v2_name is None or v1_name==v2_name:
            raise ValueError
        if self.find_vertex(v1_name) is None or self.find_vertex(v2_name) is None:
            return None
        if self.num_edges!=0:
            for edge in self.edges:
                if (edge.first_vertex.name==v1_name and edge.second_vertex.name==v2_name) or (edge.first_vertex.name==v2_name and edge.second_vertex.name==v1_name):
                    return None

        first_vertex=Vertex(-1,"")
        second_vertex=Vertex(-1,"")
        if self.num_vertices!=0:
            for vertex in self.vertices:
                if vertex.name==v1_name:
                    first_vertex.idx=vertex.idx
                    first_vertex.name=vertex.name
                elif vertex.name==v2_name:
                    second_vertex.idx=vertex.idx
                    second_vertex.name=vertex.name

        new_edge=Edge(first_vertex,second_vertex,weight)
        self.edges.append(new_edge)
        self.num_edges+=1
        return new_edge

    def insert_edge(self, v1: Vertex, v2: Vertex, weight: int):
        """
        Inserts an edge between two vertices v1 and v2 and returns the newly added edge.
        None is returned if the edge already existed, or if at least one of the vertices is not found in the graph.
        A ValueError shall be thrown if v1 equals v2 (=loop).
        :param v1: vertex 1
        :param v2: vertex 2
        :param weight: weight of the edge
        :return: Returns None if the edge already exists or at least one of the two given vertices is not part of the
                 graph, otherwise returns the newly added edge.
        :raises: ValueError if v1 is equal to v2 or if v1 or v2 is None.
        """
        if v1 is None or v2 is None or v1.name==v2.name:
            raise ValueError
        if self.find_vertex(v1.name) is None or self.find_vertex(v2.name) is None:
            return None
        if self.num_edges!=0:
            for edge in self.edges:
                if (edge.first_vertex.name==v1.name and edge.second_vertex.name==v2.name) or (edge.first_vertex.name==v2.name and edge.second_vertex.name==v1.name):
                    return None
        new_edge = Edge(v1, v2, weight)
        self.edges.append(new_edge)
        self.num_edges+=1
        return new_edge

    def find_edge_by_vertex_names(self, v1_name, v2_name):
        """
        Returns the edge if there is an edge between the vertices with the name v1_name and v2_name, otherwise None.
        In case both names are identical a ValueError shall be raised.
        :param v1_name: name (string) of vertex 1
        :param v2_name: name (string) of vertex 2
        :return: Returns the found edge or None if there is no edge.
        :raises: ValueError if v1_name equals v2_name or if v1_name or v2_name is None.
        """
        if v1_name is None or v2_name is None or v1_name==v2_name:
            raise ValueError
        for edge in self.edges:
            if (edge.first_vertex.name==v1_name and edge.second_vertex.name==v2_name) or (edge.first_vertex.name==v2_name and edge.second_vertex.name==v1_name):
                return edge
        return None

    def find_edge(self, v1: Vertex, v2: Vertex):
        """
        Returns the edge if there is an edge between the vertices v1 and v2, otherwise None.
        In case v1 equals v2 a ValueError shall be raised.
        :param v1: vertex 1
        :param v2: vertex 2
        :return: Returns the found edge or None if there is no edge.
        :raises: ValueError if v1 equals v2 or if v1 or v2 are None.
        """
        if v1 is None or v2 is None or v1.name==v2.name:
            raise ValueError
        for edge in self.edges:
            if (edge.first_vertex.name==v1.name and edge.second_vertex.name==v2.name) or (edge.first_vertex.name==v2.name and edge.second_vertex.name==v1.name):
                return edge
        return None

    @staticmethod
    def create_row(dimension):
        row=list()
        tmp=dimension
        while tmp:
            row.append(-1)
            tmp-=1
        return row

    def get_adjacency_matrix(self):
        """
        Returns the NxN adjacency matrix for the graph, where N = get_number_of_vertices().
        The matrix contains the edge weight if there is an edge at the corresponding index position, otherwise -1.
        :return: adjacency matrix
        """
        N=self.get_number_of_vertices()
        matrix=[]
        tmp=N
        while tmp:
            row=self.create_row(N)
            matrix.append(row)
            tmp-=1
        for edge in self.edges:
            matrix[edge.first_vertex.idx][edge.second_vertex.idx]=edge.weight
            matrix[edge.second_vertex.idx][edge.first_vertex.idx]=edge.weight
        return matrix

    @staticmethod
    def return_vertex(vertex_list,index):
        for vertex in vertex_list:
            if vertex.idx==index:
                return vertex

    def get_adjacent_vertices_by_vertex_name(self, vertex_name):
        """
        Returns a list of vertices which are adjacent to the vertex with name vertex_name based on the ordering in which
        they occur in the adjacency matrix.
        :param vertex_name: The name of the vertex to which adjacent vertices are searched.
        :return: list of vertices that are adjacent to the vertex with name vertex_name.
        :raises: ValueError if vertex_name is None
        """
        if vertex_name is None:
            raise ValueError
        matrix=self.get_adjacency_matrix()
        index=-1
        for vertex in self.vertices:
            if vertex.name==vertex_name:
                index=vertex.idx
        position=0
        vertex_list_returned=[]
        while position<len(matrix):
            if matrix[index][position]!=-1:
                vertex_list_returned.append(self.return_vertex(self.vertices,position))
            position+=1
        return vertex_list_returned


    def get_adjacent_vertices(self, vertex: Vertex):
        """
        Returns a list of vertices which are adjacent to the given vertex based on the ordering in which
        they occur in the adjacency matrix.
        :param vertex: The vertex to which adjacent vertices are searched.
        :return: list of vertices that are adjacent to the vertex.
        :raises: ValueError if vertex is None
        """
        if vertex is None:
            raise ValueError
        matrix = self.get_adjacency_matrix()
        position = 0
        vertex_list_returned = []
        while position < len(matrix):
            if matrix[vertex.idx][position] != -1:
                vertex_list_returned.append(self.return_vertex(self.vertices, position))
            position += 1
        return vertex_list_returned

