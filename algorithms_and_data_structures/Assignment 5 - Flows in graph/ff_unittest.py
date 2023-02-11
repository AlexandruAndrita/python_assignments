import unittest

from ff import Graph
import numpy as np


class TestAssignment06Student(unittest.TestCase):
    # https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm
    _wikigraph = [
        [0, 3, 0, 3, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0],
        [3, 0, 0, 1, 2, 0, 0],
        [0, 0, 0, 0, 2, 6, 0],
        [0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    _maxWikiFlow = [
        [0, 2, 0, 3, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    _graph3 = [
        [0, 16, 13, 0, 0, 0],
        [0, 10, 0, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]

    _graph4 = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 0, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]

    _graph1 = [
        [0, 8, 0, 0, 3, 0],
        [0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 7, 4],
        [0, 0, 0, 0, 0, 5],
        [0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

    _graph2 = [
        [0, 67, 0, 72, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 99, 64, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 97, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 84, 0, 65, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 19, 16, 89, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 86, 77, 0, 77, 0, 0, 68],
        [93, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 17, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 84, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34, 32, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 98, 0, 83, 0, 0, 6, 94, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 42, 0, 0, 0, 0, 82, 84],
        [0, 0, 0, 0, 0, 0, 0, 54, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 99, 0, 95, 0, 0, 0, 0]
    ]

    def test_ff_wiki(self):
        g = Graph(self._wikigraph)
        source = 0
        sink = 6
        flow = g.ford_fulkerson(source, sink)

        self.assertEqual(5, flow, "max flow should be 5 : " + str(flow) + " given \n\n\t")
        self.assertEqual(True, g.current_flow <= g.graph,
                         "max flow should comply with capacities \n" + str(g.current_flow) + " \n\n\t")

        for node in range(len(self._maxWikiFlow)):
            self.assertEqual(g.current_flow[node], self._maxWikiFlow[node],
                             "flow of node " + str(node) + " incorrect (" + str(g.current_flow[node]) + " VS " + str(
                                 self._maxWikiFlow[node]) + ")")

    def test_ff_step4(self):
        try:
            g = Graph(self._graph4)
            source = 0
            sink = 5
            flow = 0
            residual_graph = [[j for j in i] for i in self._graph4]

            path_flow = g.ff_step(source, sink)
            while path_flow > 0:
                flow += path_flow

                self.assertEqual(2, np.unique(np.array(g.latest_augmenting_path)).size,
                                 "current augmenting graph should have 2 values \n" + str(
                                     np.unique(np.array(g.latest_augmenting_path))) + " given \n\n\t")

                self.assertEqual(True, g.latest_augmenting_path <= residual_graph,
                                 "current augmenting path should comply with residuals \n" + str(
                                     g.latest_augmenting_path) + " \n\n" + str(residual_graph) + " \n\n\t")

                self.assertEqual(True, g.current_flow <= g.graph,
                                 "current flow should comply with capacities \n" + str(g.current_flow) + " \n\n\t")

                residual_graph = [[j for j in i] for i in g.residual_graph]
                path_flow = g.ff_step(source, sink)

            self.assertEqual(23, flow, "max flow should be 23 : " + str(flow) + " given \n\n\t")

        except Exception as e:
            if not isinstance(e, AssertionError):
                self.fail("Could not test as an exception has been thrown: " + str(e))
            else:
                self.fail("The following error occurred during testing: " + str(e))

    def test_ff4(self):
        g = Graph(self._graph4)
        source = 0
        sink = 5
        flow = g.ford_fulkerson(source, sink)

        self.assertEqual(23, flow, "max flow should be 23 : " + str(flow) + " given \n\n\t")

    def test_ff_step3(self):
        try:
            g = Graph(self._graph3)
            source = 0
            sink = 5
            flow = 0
            residual_graph = [[j for j in i] for i in self._graph3]

            path_flow = g.ff_step(source, sink)
            while path_flow > 0:
                flow += path_flow

                self.assertEqual(2, np.unique(np.array(g.latest_augmenting_path)).size,
                                 "current augmenting graph should have 2 values \n" + str(
                                     np.unique(np.array(g.latest_augmenting_path))) + " given \n\n\t")

                self.assertEqual(True, g.latest_augmenting_path <= residual_graph,
                                 "current augmenting path should comply with residuals \n" + str(
                                     g.latest_augmenting_path) + " \n\n" + str(residual_graph) + " \n\n\t")

                self.assertEqual(True, g.current_flow <= g.graph,
                                 "current flow should comply with capacities \n" + str(g.current_flow) + " \n\n\t")

                residual_graph = [[j for j in i] for i in g.residual_graph]
                path_flow = g.ff_step(source, sink)

            self.assertEqual(23, flow, "max flow should be 23 : " + str(flow) + " given \n\n\t")

        except Exception as e:
            if not isinstance(e, AssertionError):
                self.fail("Could not test as an exception has been thrown: " + str(e))
            else:
                self.fail("The following error occurred during testing: " + str(e))

    def test_ff3(self):
        g = Graph(self._graph3)
        source = 0
        sink = 5
        flow = g.ford_fulkerson(source, sink)

        self.assertEqual(23, flow, "max flow should be 23 : " + str(flow) + " given \n\n\t")

    def test_ff_step2(self):
        g = Graph(self._graph2)
        source = 0
        sink = 15
        flow = 0
        residual_graph = [[j for j in i] for i in self._graph2]

        path_flow = g.ff_step(source, sink)
        while path_flow > 0:
            flow += path_flow

            self.assertEqual(2, np.unique(np.array(g.latest_augmenting_path)).size,
                             "current augmenting graph should have 2 values \n" + str(
                                 np.unique(np.array(g.latest_augmenting_path))) + " given \n\n\t")

            self.assertEqual(True, g.latest_augmenting_path <= residual_graph,
                             "current augmenting path should comply with residuals \n" + str(
                                 g.latest_augmenting_path) + " \n\n\t")

            self.assertEqual(True, g.current_flow <= g.graph,
                             "current flow should comply with capacities \n" + str(g.current_flow) + " \n\n\t")

            residual_graph = [[j for j in i] for i in g.residual_graph]
            path_flow = g.ff_step(source, sink)

        self.assertEqual(41, flow, "max flow should be 41 : " + str(flow) + " given \n\n\t")

    def test_ff2(self):
        g = Graph(self._graph2)
        source = 0
        sink = 15
        flow = g.ford_fulkerson(source, sink)

        self.assertEqual(41, flow, "max flow should be 41 : " + str(flow) + " given \n\n\t")

    def test_ff_step1(self):
        g = Graph(self._graph1)
        source = 0
        sink = 5
        flow = 0
        residual_graph = [[j for j in i] for i in self._graph1]

        path_flow = g.ff_step(source, sink)
        while path_flow > 0:
            flow += path_flow

            self.assertEqual(2, np.unique(np.array(g.latest_augmenting_path)).size,
                             "current augmenting graph should have 2 values \n" + str(
                                 np.unique(np.array(g.latest_augmenting_path))) + " given \n\n\t")

            self.assertEqual(True, g.latest_augmenting_path <= residual_graph,
                             "current augmenting path should comply with residuals \n" + str(
                                 g.latest_augmenting_path) + " \n\n\t")

            self.assertEqual(True, g.current_flow <= g.graph,
                             "current flow should comply with capacities \n" + str(g.current_flow) + " \n\n\t")

            residual_graph = [[j for j in i] for i in g.residual_graph]
            path_flow = g.ff_step(source, sink)

        self.assertEqual(8, flow, "max flow should be 8 : " + str(flow) + " given \n\n\t")

    def test_ff1(self):
        g = Graph(self._graph1)
        source = 0
        sink = 5
        flow = g.ford_fulkerson(source, sink)

        self.assertEqual(8, flow, "max flow should be 8 : " + str(flow) + " given \n\n\t")


if __name__ == '__main__':
    unittest.main()
