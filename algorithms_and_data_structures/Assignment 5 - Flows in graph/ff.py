# Ford-Fulkerson algorith in Python
import sys


class Graph:

    def __init__(self, graph):
        self.graph = graph  # original graph
        self.residual_graph = [[cell for cell in row] for row in graph]  # cloned graph
        self.latest_augmenting_path = [[0 for cell in row] for row in
                                       graph]  # empty graph with same dimension as graph
        self.current_flow = [[0 for cell in row] for row in graph]  # empty graph with same dimension as graph

    def bfs(self,source,sink,path):
        visited_vertices=[False]*(len(self.residual_graph[0]))
        queue=[]
        queue.append(source)
        visited_vertices[source]=True
        while queue:
            vertex=queue.pop(0)
            i=0
            while i<len(self.residual_graph[vertex]):
                if visited_vertices[i]==False and self.residual_graph[vertex][i]:
                    queue.append(i)
                    visited_vertices[i]=True
                    path[i]=vertex
                    if i==sink:
                        return True
                i+=1

        return False

    def check_latest_augmenting_path(self):
        for i in range(len(self.latest_augmenting_path)):
            for j in range(len(self.latest_augmenting_path)):
                if self.latest_augmenting_path[i][j]!=0:
                    self.latest_augmenting_path=[]
                    self.latest_augmenting_path=[[0]*len(j) for j in self.graph]
                    break

    def ff_step(self, source, sink):
        """
        Perform a single flow augmenting iteration from source to sink
        Update the latest augmenting path, the residual graph and the current flow by the maximum possible amount according to your chosen path.
        The path must be chosen based on BFS.
        @param source the source's vertex id
        @param sink the sink's vertex id
        @return the amount by which the flow has increased.
        """
        path=[-1]*len(self.residual_graph[0])
        flow=sys.maxsize
        if self.bfs(source,sink,path) is True:
            current_vertex=sink

            #finding the minimum capacity
            while current_vertex!=source:
                parent_vertex=path[current_vertex]
                if self.residual_graph[parent_vertex][current_vertex]<flow:
                    flow=self.residual_graph[parent_vertex][current_vertex]
                current_vertex=path[current_vertex]

            #adjusting the residual graph and the current flow by going backwards and reversing the edges
            current_vertex=sink
            while current_vertex!=source:
                parent_vertex=path[current_vertex]
                self.residual_graph[parent_vertex][current_vertex]-=flow
                self.residual_graph[current_vertex][parent_vertex]+=flow

                #backward edge handling
                if self.graph[parent_vertex][current_vertex]>0:
                    self.current_flow[parent_vertex][current_vertex]+=flow
                else:
                    self.current_flow[current_vertex][parent_vertex]-=flow
                current_vertex=path[current_vertex]

            #updating latest augmenting path
            self.check_latest_augmenting_path()
            current_vertex=sink
            while current_vertex!=source:
                parent_vertex=path[current_vertex]
                self.latest_augmenting_path[parent_vertex][current_vertex]=flow
                current_vertex=path[current_vertex]

            #if flow has been changed, meaning there existed a path
            if flow:
                return flow
        #if flow has not been changed
        return 0

    def ford_fulkerson(self, source, sink):
        """
        Execute the ford-fulkerson algorithm (i.e., repeated calls of ff_step())
        @param source the source's vertex id
        @param sink the sink's vertex id
        @return the max flow from source to sink
        """
        maximum_flow=0
        maximum_number_iterations=0
        for i in self.graph[source]:
            maximum_number_iterations+=i
        #repeated calls of ff_step() until the maximum number of iterations is reached
        while maximum_number_iterations:
            maximum_flow+=self.ff_step(source,sink)
            maximum_number_iterations-=1
        return maximum_flow