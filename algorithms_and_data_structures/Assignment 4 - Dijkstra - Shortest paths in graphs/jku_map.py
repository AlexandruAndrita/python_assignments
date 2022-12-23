import sys

from graph import Graph
from vertex import Vertex
from step import Step


class JKUMap(Graph):

    def __init__(self):
        super().__init__()
        v_spar = self.insert_vertex("Spar")
        v_lit = self.insert_vertex("LIT")
        v_porter = self.insert_vertex("Porter")
        v_openLab = self.insert_vertex("Open Lab")
        v_bank = self.insert_vertex("Bank")
        v_khg = self.insert_vertex("KHG")
        v_chat = self.insert_vertex("Chat")
        v_parking = self.insert_vertex("Parking")
        v_bellaCasa = self.insert_vertex("Bella Casa")
        v_library = self.insert_vertex("Library")
        v_teichwerk = self.insert_vertex("Teichwerk")
        v_lui = self.insert_vertex("LUI")
        v_sp1 = self.insert_vertex("SP1")
        v_sp3 = self.insert_vertex("SP3")
        v_castle = self.insert_vertex("Castle")
        v_papaya = self.insert_vertex("Papaya")
        v_jkh = self.insert_vertex("JKH")

        self.insert_edge(v_spar, v_lit, 50)
        self.insert_edge(v_lit,v_porter,80)
        self.insert_edge(v_spar,v_porter,103)
        self.insert_edge(v_spar,v_khg,165)
        self.insert_edge(v_porter,v_openLab,70)
        self.insert_edge(v_porter,v_bank,100)
        self.insert_edge(v_bank,v_khg,150)
        self.insert_edge(v_bank,v_chat,115)
        self.insert_edge(v_khg,v_parking,190)
        self.insert_edge(v_parking,v_bellaCasa,145)
        self.insert_edge(v_parking,v_sp1,240)
        self.insert_edge(v_sp1,v_sp3,130)
        self.insert_edge(v_chat,v_library,160)
        self.insert_edge(v_chat,v_lui,240)
        self.insert_edge(v_lui,v_teichwerk,135)
        self.insert_edge(v_library,v_lui,90)
        self.insert_edge(v_lui,v_sp1,175)
        self.insert_edge(v_castle,v_papaya,85)
        self.insert_edge(v_papaya,v_jkh,80)

    def get_shortest_path_from_to(self, from_vertex: Vertex, to_vertex: Vertex):
        """
        This method determines the shortest path between two POIs "from_vertex" and "to_vertex".
        It returns the list of intermediate steps of the route that have been found
        using the dijkstra algorithm.

        :param from_vertex: Start vertex
        :param to_vertex:   Destination vertex
        :return:
           The path, with all intermediate steps, returned as a list. This list
           sequentially contains each vertex along the shortest path, together with
           the already covered distance (see example on the assignment sheet).
           Returns None if there is no path between the two given vertices.
        :raises ValueError: If from_vertex or to_vertex is None, or if from_vertex equals to_vertex
        """
        if from_vertex is None or to_vertex is None or from_vertex == to_vertex:
            raise ValueError

        paths = {from_vertex.name: (None, 0)}
        visited_vertices = set()
        current_vertex = from_vertex.name

        while current_vertex != to_vertex.name:
            visited_vertices.add(current_vertex)
            all_destinations=self.get_edges()
            destinations = []

            for edge in all_destinations:
                if edge.first_vertex.name==current_vertex:
                    destinations.append(edge.second_vertex.name)
                elif edge.second_vertex.name==current_vertex:
                    destinations.append(edge.first_vertex.name)

            weight_current_vertex = paths[current_vertex][1]

            for possible_way_vertex in destinations:
                weight = self.find_edge_by_vertex_names(current_vertex, possible_way_vertex).weight + weight_current_vertex
                if possible_way_vertex not in paths:
                    paths[possible_way_vertex] = (current_vertex, weight)
                else:
                    current_weight = paths[possible_way_vertex][1]
                    if current_weight > weight:
                        paths[possible_way_vertex] = (current_vertex, weight)

            next_destinations = {vertex: paths[vertex] for vertex in paths if vertex not in visited_vertices}
            if not next_destinations:
                return None

            min_destination=sys.maxsize
            for key,value in next_destinations.items():
                if value[1]<min_destination:
                    min_destination=value[1]
                    current_vertex=key

        path_result = []
        while current_vertex is not None:
            current_step = Step(self.find_vertex(current_vertex), paths[current_vertex][1])
            path_result.append(current_step)
            possible_way_vertex = paths[current_vertex][0]
            current_vertex = possible_way_vertex
        path_result = path_result[::-1]

        if len(path_result)==0:
            return None
        return path_result

    @staticmethod
    def get_value_index(steps_dict):
        return steps_dict[1]

    def get_steps_for_shortest_paths_from(self, from_vertex: Vertex):
        """
        This method determines the amount of "steps" needed on the shortest paths
        from a given "from" vertex to all other vertices.
        The number of steps (or -1 if no path exists) to each vertex is returned
        as a dictionary, using the vertex name as key and number of steps as value.
        E.g., the "from" vertex has a step count of 0 to itself and 1 to all adjacent vertices.

        :param from_vertex: start vertex
        :return:
          A map containing the number of steps (or -1 if no path exists) on the
          shortest path to each vertex, using the vertex name as key and the number of steps as value.
        :raises ValueError: If from_vertex is None.
        """
        if from_vertex is None:
            raise ValueError
        all_vertices=self.get_vertices()
        steps_dict=dict()

        for to_vertex in all_vertices:
            if to_vertex not in steps_dict:
                if from_vertex.name == to_vertex.name:
                    steps_dict[from_vertex.name] = 0
                else:
                    path = self.get_shortest_path_from_to(from_vertex, to_vertex)
                    if path is None:
                        steps_dict[to_vertex.name] = -1
                    elif path is not None:
                        steps_dict[to_vertex.name] = len(path)-1

        steps_dict=sorted(steps_dict.items(), key=self.get_value_index)
        steps_dict=dict(steps_dict)
        return steps_dict

    def get_shortest_distances_from(self, from_vertex: Vertex):
        """
        This method determines the shortest paths from a given "from" vertex to all other vertices.
        The shortest distance (or -1 if no path exists) to each vertex is returned
        as a dictionary, using the vertex name as key and the distance as value.

        :param from_vertex: Start vertex
        :return
           A dictionary containing the shortest distance (or -1 if no path exists) to each vertex,
           using the vertex name as key and the distance as value.
        :raises ValueError: If from_vertex is None.
        """
        if from_vertex is None:
            raise ValueError
        all_vertices = self.get_vertices()
        steps_dict = dict()

        for to_vertex in all_vertices:
            if to_vertex not in steps_dict:
                if from_vertex.name == to_vertex.name:
                    steps_dict[from_vertex.name] = 0
                else:
                    path = self.get_shortest_path_from_to(from_vertex, to_vertex)
                    if path is None:
                        steps_dict[to_vertex.name] = -1
                    elif path is not None:
                        steps_dict[to_vertex.name] = path[len(path)-1].covered_distance

        steps_dict = sorted(steps_dict.items(), key=self.get_value_index)
        steps_dict = dict(steps_dict)
        return steps_dict

    def _dijkstra(self, cur: Vertex, visited_list, distances: dict, paths: dict):
        """
        This method is expected to be called with correctly initialized data structures and recursively calls itself.

        :param cur: Current vertex being processed
        :param visited_list: List which stores already visited vertices.
        :param distances: Dict (nVertices entries) which stores the min. distance to each vertex.
        :param paths: Dict (nVertices entries) which stores the shortest path to each vertex.
        """

        # This method is not mandatory, but a recommendation by us
