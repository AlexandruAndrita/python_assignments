import unittest
from jku_map import JKUMap

class TestAssignment04Student(unittest.TestCase):
    def test_map_construction(self):
        warning = " MAKE SURE TO FIX THIS, OTHERWISE ALL OTHER TESTS CANNOT WORK!"
        jku_map = JKUMap()
        self.assertEqual(17, jku_map.get_number_of_vertices(),
                         ".get_number_of_vertices() did return a wrong count." + warning)
        self.assertIsNotNone(jku_map.find_vertex("SP3"), ".find_vertex() did not find SP3." + warning)
        self.assertIsNotNone(jku_map.find_vertex("SP1"), ".find_vertex() did not find SP1." + warning)
        self.assertIsNotNone(jku_map.find_vertex("Parking"), ".find_vertex() did not find Parking." + warning)
        self.assertIsNotNone(jku_map.find_vertex("LUI"), ".find_vertex() did not find LUI." + warning)
        self.assertIsNotNone(jku_map.find_vertex("Teichwerk"), ".find_vertex() did not find Teichwerk." + warning)
        self.assertIsNotNone(jku_map.find_vertex("Bella Casa"), ".find_vertex() did not find Bella Casa." + warning)
        self.assertIsNotNone(jku_map.find_vertex("Chat"), ".find_vertex() did not find Chat." + warning)
        self.assertIsNotNone(jku_map.find_vertex("Library"), ".find_vertex() did not find Library." + warning)
        self.assertIsNotNone(jku_map.find_vertex("Bank"), ".find_vertex() did not find Bank." + warning)
        self.assertIsNotNone(jku_map.find_vertex("KHG"), ".find_vertex() did not find SP3." + warning)
        self.assertIsNotNone(jku_map.find_vertex("Spar"), ".find_vertex() did not find Spar." + warning)
        self.assertIsNotNone(jku_map.find_vertex("Porter"), ".find_vertex() did not find Porter." + warning)
        self.assertIsNotNone(jku_map.find_vertex("Open Lab"), ".find_vertex() did not find Open Lab." + warning)
        self.assertIsNotNone(jku_map.find_vertex("LIT"), ".find_vertex() did not find LIT." + warning)
        self.assertIsNotNone(jku_map.find_vertex("Castle"), ".find_vertex() did not find Castle." + warning)
        self.assertIsNotNone(jku_map.find_vertex("Papaya"), ".find_vertex() did not find Papaya." + warning)
        self.assertIsNotNone(jku_map.find_vertex("JKH"), ".find_vertex() did not find JHK." + warning)

        self.assertEqual(19, jku_map.get_number_of_edges(),
                         ".get_number_of_edges() did return a wrong count." + warning)

        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("SP1", "SP3"),
                             ".find_edge_by_vertex_names() did not find edge between SP1 and SP3." + warning)
        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("SP3", "SP1"),
                             ".find_edge_by_vertex_names() did not find edge between SP3 and SP1." + warning)
        self.assertEqual(130, jku_map.find_edge_by_vertex_names("SP3", "SP1").weight,
                         ".find_edge_by_vertex_names() returned wrong edge weight for edge between SP3 and SP1." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("SP1", "LUI"),
                             ".find_edge_by_vertex_names() did not find edge between SP1 and LUI." + warning)
        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("LUI", "SP1"),
                             ".find_edge_by_vertex_names() did not find edge between LUI and SP1." + warning)
        self.assertEqual(175, jku_map.find_edge_by_vertex_names("LUI", "SP1").weight,
                         ".find_edge_by_vertex_names() returned wrong edge weight for edge between LUI and SP1." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("SP1", "Parking"),
                             ".find_edge_by_vertex_names() did not find edge between SP1 and Parking." + warning)
        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Parking", "SP1"),
                             ".find_edge_by_vertex_names() did not find edge between Parking and SP1." + warning)
        self.assertEqual(240, jku_map.find_edge_by_vertex_names("Parking", "SP1").weight,
                         ".find_edge_by_vertex_names() returned wrong edge weight for edge between Parking and SP1." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Bella Casa", "Parking"),
                             ".find_edge_by_vertex_names() did not find edge between Bella Casa and Parking." + warning)
        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Parking", "Bella Casa"),
                             ".find_edge_by_vertex_names() did not find edge between Parking and Bella Casa." + warning)
        self.assertEqual(145, jku_map.find_edge_by_vertex_names("Parking", "Bella Casa").weight,
                         ".find_edge_by_vertex_names() returned wrong edge weight for edge between Parking and Bella "
                         "Casa." + warning)

        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("KHG", "Parking"),
                             ".find_edge_by_vertex_names() did not find edge between KHG and Parking." + warning)
        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Parking", "KHG"),
                             ".find_edge_by_vertex_names() did not find edge between Parking and KHG." + warning)
        self.assertEqual(190, jku_map.find_edge_by_vertex_names("Parking", "KHG").weight,
                         ".find_edge_by_vertex_names() returned wrong edge weight for edge between Parking and KHG." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("KHG", "Spar"),
                             ".find_edge_by_vertex_names() did not find edge between KHG and Spar." + warning)
        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Spar", "KHG"),
                             ".find_edge_by_vertex_names() did not find edge between Spar and KHG." + warning)
        self.assertEqual(165, jku_map.find_edge_by_vertex_names("Spar", "KHG").weight,
                         ".find_edge_by_vertex_names() returned wrong edge weight for edge between Spar and KHG." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("KHG", "Bank"),
                             ".find_edge_by_vertex_names() did not find edge between KHG and Bank." + warning)
        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Bank", "KHG"),
                             ".find_edge_by_vertex_names() did not find edge between Bank and KHG." + warning)
        self.assertEqual(150, jku_map.find_edge_by_vertex_names("Bank", "KHG").weight,
                         ".find_edge_by_vertex_names() returned wrong edge weight for edge between Bank and KHG." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Porter", "Spar"),
                             ".find_edge_by_vertex_names() did not find edge between Porter and Spar." + warning)
        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Spar", "Porter"),
                             ".find_edge_by_vertex_names() did not find edge between Spar and Porter." + warning)
        self.assertEqual(103, jku_map.find_edge_by_vertex_names("Spar", "Porter").weight,
                         ".find_edge_by_vertex_names() returned wrong edge weight for edge between Spar and Porter." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("LIT", "Spar"),
                             ".find_edge_by_vertex_names() did not find edge between LIT and Spar." + warning)
        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Spar", "LIT"),
                             ".find_edge_by_vertex_names() did not find edge between Spar and LIT." + warning)
        self.assertEqual(50, jku_map.find_edge_by_vertex_names("Spar", "LIT").weight,
                         ".find_edge_by_vertex_names() returned wrong edge weight for edge between Spar and LIT." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("LIT", "Porter"),
                             ".find_edge_by_vertex_names() did not find edge between LIT and Porter." + warning)
        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Porter", "LIT"),
                             ".find_edge_by_vertex_names() did not find edge between Porter and LIT." + warning)
        self.assertEqual(80, jku_map.find_edge_by_vertex_names("Porter", "LIT").weight,
                         ".find_edge_by_vertex_names() returned wrong edge weight for edge between Porter and LIT." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Open Lab", "Porter"),
                             ".find_edge_by_vertex_names() did not find edge between Open Lab and Porter." + warning)
        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Porter", "Open Lab"),
                             ".find_edge_by_vertex_names() did not find edge between Porter and Open Lab." + warning)
        self.assertEqual(70, jku_map.find_edge_by_vertex_names("Porter", "Open Lab").weight,
                         ".find_edge_by_vertex_names() returned wrong edge weight for edge between Porter and Open "
                         "Lab. " + warning)

        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Bank", "Porter"),
                             ".find_edge_by_vertex_names() did not find edge between Bank and Porter." + warning)
        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Porter", "Bank"),
                             ".find_edge_by_vertex_names() did not find edge between Porter and Bank." + warning)
        self.assertEqual(100, jku_map.find_edge_by_vertex_names("Porter", "Bank").weight,
                         ".find_edge_by_vertex_names() returned wrong edge weight for edge between Porter and Bank." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Bank", "Chat"),
                             ".find_edge_by_vertex_names() did not find edge between Bank and Chat." + warning)
        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Chat", "Bank"),
                             ".find_edge_by_vertex_names() did not find edge between Chat and Bank." + warning)
        self.assertEqual(115, jku_map.find_edge_by_vertex_names("Chat", "Bank").weight,
                         ".find_edge_by_vertex_names() returned wrong edge weight for edge between Chat and Bank." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Library", "Chat"),
                             ".find_edge_by_vertex_names() did not find edge between Library and Chat." + warning)
        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Chat", "Library"),
                             ".find_edge_by_vertex_names() did not find edge between Chat and Library." + warning)
        self.assertEqual(160, jku_map.find_edge_by_vertex_names("Chat", "Library").weight,
                         ".find_edge_by_vertex_names() returned wrong edge weight for edge between Chat and Library." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("LUI", "Chat"),
                             ".find_edge_by_vertex_names() did not find edge between LUI and Chat." + warning)
        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Chat", "LUI"),
                             ".find_edge_by_vertex_names() did not find edge between Chat and LUI." + warning)
        self.assertEqual(240, jku_map.find_edge_by_vertex_names("Chat", "LUI").weight,
                         ".find_edge_by_vertex_names() returned wrong edge weight for edge between Chat and LUI." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Library", "LUI"),
                             ".find_edge_by_vertex_names() did not find edge between Library and LUI." + warning)
        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("LUI", "Library"),
                             ".find_edge_by_vertex_names() did not find edge between LUI and Library." + warning)
        self.assertEqual(90, jku_map.find_edge_by_vertex_names("LUI", "Library").weight,
                         ".find_edge_by_vertex_names() returned wrong edge weight for edge between LUI and Library." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Teichwerk", "LUI"),
                             ".find_edge_by_vertex_names() did not find edge between Teichwerk and LUI." + warning)
        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("LUI", "Teichwerk"),
                             ".find_edge_by_vertex_names() did not find edge between LUI and Teichwerk." + warning)
        self.assertEqual(135, jku_map.find_edge_by_vertex_names("LUI", "Teichwerk").weight,
                         ".find_edge_by_vertex_names() returned wrong edge weight for edge between LUI and Teichwerk." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Castle", "Papaya"),
                             ".find_edge_by_vertex_names() did not find edge between Castle and Papaya." + warning)
        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Papaya", "Castle"),
                             ".find_edge_by_vertex_names() did not find edge between Papaya and Castle." + warning)
        self.assertEqual(85, jku_map.find_edge_by_vertex_names("Papaya", "Castle").weight,
                         ".find_edge_by_vertex_names() returned wrong edge weight for edge between Papaya and Castle." +
                         warning)

        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("JKH", "Papaya"),
                             ".find_edge_by_vertex_names() did not find edge between JKH and Papaya." + warning)
        self.assertIsNotNone(jku_map.find_edge_by_vertex_names("Papaya", "JKH"),
                             ".find_edge_by_vertex_names() did not find edge between Papaya and JKH." + warning)
        self.assertEqual(80, jku_map.find_edge_by_vertex_names("Papaya", "JKH").weight,
                         ".find_edge_by_vertex_names() returned wrong edge weight for edge between Papaya and JKH." +
                         warning)

    def test_non_existing_shortest_path_from_JKH_to_KHG(self):
        jku_map = JKUMap()
        path = jku_map.get_shortest_path_from_to(jku_map.find_vertex("JKH"), jku_map.find_vertex("KHG"))
        self.assertIsNone(path,
                          ".get_shortest_path_from_to() did not return None for a non-existing way from JKH to KHG")

    def test_non_existing_shortest_path_from_KHG_to_JKH(self):
        jku_map = JKUMap()
        path = jku_map.get_shortest_path_from_to(jku_map.find_vertex("KHG"), jku_map.find_vertex("JKH"))
        self.assertIsNone(path,
                          ".get_shortest_path_from_to() did not return None for a non-existing way from KHG to JKH")

    def test_existing_shortest_path_from_castle_to_papaya(self):
        jku_map = JKUMap()
        path = jku_map.get_shortest_path_from_to(jku_map.find_vertex("Castle"), jku_map.find_vertex("Papaya"))
        self.assertIsNotNone(path,
                             ".get_shortest_path_from_to() did return None for an existing way from Castle to Papaya")
        self.assertEqual("Castle", path[0].point.name)
        self.assertEqual(0, path[0].covered_distance)
        self.assertEqual("Papaya", path[1].point.name)
        self.assertEqual(85, path[1].covered_distance)

    def test_existing_shortest_path_from_SP3_to_spar(self):
        jku_map = JKUMap()
        path = jku_map.get_shortest_path_from_to(jku_map.find_vertex("SP3"), jku_map.find_vertex("Spar"))
        self.assertIsNotNone(path, ".get_shortest_path_from_to() did return None for an existing way from SP3 to Spar")
        self.assertEqual("SP3", path[0].point.name)
        self.assertEqual(0, path[0].covered_distance)
        self.assertEqual("SP1", path[1].point.name)
        self.assertEqual(130, path[1].covered_distance)
        self.assertEqual("Parking", path[2].point.name)
        self.assertEqual(370, path[2].covered_distance)
        self.assertEqual("KHG", path[3].point.name)
        self.assertEqual(560, path[3].covered_distance)
        self.assertEqual("Spar", path[4].point.name)
        self.assertEqual(725, path[4].covered_distance)

    def test_shortest_distances_from_JKH(self):
        jku_map = JKUMap()
        result = jku_map.get_shortest_distances_from(jku_map.find_vertex("JKH"))

        self.assertEqual(17, len(result),
                         ".get_shortest_distances_from() returned a map with a wrong number of entries.")
        self.assertEqual(165, result.get("Castle"),
                         ".get_shortest_distances_from() did return wrong distance for reachable point")
        self.assertEqual(80, result.get("Papaya"),
                         ".get_shortest_distances_from() did return wrong distance for reachable point")

        self.assertEqual(0, result.get("JKH"), ".get_shortest_distances_from() did not return 0 for the start point")

        self.assertEqual(-1, result.get("LUI"),
                         ".get_shortest_distances_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Library"),
                         ".get_shortest_distances_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Chat"),
                         ".get_shortest_distances_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Teichwerk"),
                         ".get_shortest_distances_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("SP1"),
                         ".get_shortest_distances_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("SP3"),
                         ".get_shortest_distances_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Parking"),
                         ".get_shortest_distances_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Bank"),
                         ".get_shortest_distances_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Bella Casa"),
                         ".get_shortest_distances_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("KHG"),
                         ".get_shortest_distances_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Porter"),
                         ".get_shortest_distances_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Spar"),
                         ".get_shortest_distances_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("LIT"),
                         ".get_shortest_distances_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Open Lab"),
                         ".get_shortest_distances_from() did not return -1 for a non-reachable point")

    def test_shortest_distances_from_LUI(self):
        jku_map = JKUMap()
        result = jku_map.get_shortest_distances_from(jku_map.find_vertex("LUI"))

        self.assertEqual(17, len(result),
                         ".get_shortest_distances_from() returned a map with a wrong number of entries.")
        self.assertEqual(-1, result.get("Castle"),
                         ".get_shortest_distances_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Papaya"),
                         ".get_shortest_distances_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("JKH"),
                         ".get_shortest_distances_from() did not return -1 for a non-reachable point")

        self.assertEqual(0, result.get("LUI"), ".get_shortest_distances_from() did not return 0 for the start point")

        self.assertEqual(90, result.get("Library"),
                         ".get_shortest_distances_from() did return a wrong distance for a direct neighbor")
        self.assertEqual(240, result.get("Chat"),
                         ".get_shortest_distances_from() did return a wrong distance for a direct neighbor")
        self.assertEqual(135, result.get("Teichwerk"),
                         ".get_shortest_distances_from() did return a wrong distance for a direct neighbor")
        self.assertEqual(175, result.get("SP1"),
                         ".get_shortest_distances_from() did return a wrong distance for a direct neighbor")

        self.assertEqual(305, result.get("SP3"),
                         ".get_shortest_distances_from() did return a wrong distance for a 2-step reachable point")
        self.assertEqual(415, result.get("Parking"),
                         ".get_shortest_distances_from() did return a wrong distance for a 2-step reachable point")
        self.assertEqual(355, result.get("Bank"),
                         ".get_shortest_distances_from() did return a wrong distance for a 2-step reachable point")

        self.assertEqual(560, result.get("Bella Casa"),
                         ".get_shortest_distances_from() did return a wrong distance for a 3-step reachable point")
        self.assertEqual(505, result.get("KHG"),
                         ".get_shortest_distances_from() did return a wrong distance for a 3-step reachable point")
        self.assertEqual(455, result.get("Porter"),
                         ".get_shortest_distances_from() did return a wrong distance for a 3-step reachable point")

        self.assertEqual(558, result.get("Spar"),
                         ".get_shortest_distances_from() did return a wrong distance for a 4-step reachable point")
        self.assertEqual(535, result.get("LIT"),
                         ".get_shortest_distances_from() did return a wrong distance for a 4-step reachable point")
        self.assertEqual(525, result.get("Open Lab"),
                         ".get_shortest_distances_from() did return a wrong distance for a 4-step reachable point")

    def test_steps_for_shortest_paths_from_JKH(self):
        jku_map = JKUMap()
        result = jku_map.get_steps_for_shortest_paths_from(jku_map.find_vertex("JKH"))

        self.assertEqual(17, len(result),
                         ".get_steps_for_shortest_paths_from() returned a map with a wrong number of entries.")
        self.assertEqual(0, result.get("JKH"),
                         ".get_steps_for_shortest_paths_from() did not return 0 for the start point")
        self.assertEqual(1, result.get("Papaya"),
                         ".get_steps_for_shortest_paths_from() did return wrong step count for reachable point")
        self.assertEqual(2, result.get("Castle"),
                         ".get_steps_for_shortest_paths_from() did return wrong step count for reachable point")

        self.assertEqual(-1, result.get("LUI"),
                         ".get_steps_for_shortest_paths_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Library"),
                         ".get_steps_for_shortest_paths_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Chat"),
                         ".get_steps_for_shortest_paths_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Teichwerk"),
                         ".get_steps_for_shortest_paths_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("SP1"),
                         ".get_steps_for_shortest_paths_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("SP3"),
                         ".get_steps_for_shortest_paths_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Parking"),
                         ".get_steps_for_shortest_paths_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Bank"),
                         ".get_steps_for_shortest_paths_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Bella Casa"),
                         ".get_steps_for_shortest_paths_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("KHG"),
                         ".get_steps_for_shortest_paths_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Porter"),
                         ".get_steps_for_shortest_paths_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Spar"),
                         ".get_steps_for_shortest_paths_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("LIT"),
                         ".get_steps_for_shortest_paths_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Open Lab"),
                         ".get_steps_for_shortest_paths_from() did not return -1 for a non-reachable point")

    def test_steps_for_shortest_paths_from_LUI(self):
        jku_map = JKUMap()
        result = jku_map.get_steps_for_shortest_paths_from(jku_map.find_vertex("LUI"))

        self.assertEqual(17, len(result),
                         ".get_steps_for_shortest_paths_from() returned a map with a wrong number of entries.")
        self.assertEqual(-1, result.get("Castle"),
                         ".get_steps_for_shortest_paths_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("Papaya"),
                         ".get_steps_for_shortest_paths_from() did not return -1 for a non-reachable point")
        self.assertEqual(-1, result.get("JKH"),
                         ".get_steps_for_shortest_paths_from() did not return -1 for a non-reachable point")

        self.assertEqual(0, result.get("LUI"),
                         ".get_steps_for_shortest_paths_from() did not return 0 for the start point")

        self.assertEqual(1, result.get("Library"),
                         ".get_steps_for_shortest_paths_from() did not return 1 for a direct neighbor")
        self.assertEqual(1, result.get("Chat"),
                         ".get_steps_for_shortest_paths_from() did not return 1 for a direct neighbor")
        self.assertEqual(1, result.get("Teichwerk"),
                         ".get_steps_for_shortest_paths_from() did not return 1 for a direct neighbor")
        self.assertEqual(1, result.get("SP1"),
                         ".get_steps_for_shortest_paths_from() did not return 1 for a direct neighbor")

        self.assertEqual(2, result.get("SP3"),
                         ".get_steps_for_shortest_paths_from() did not return 2 for a 2-step reachable point")
        self.assertEqual(2, result.get("Parking"),
                         ".get_steps_for_shortest_paths_from() did not return 2 for a 2-step reachable point")
        self.assertEqual(2, result.get("Bank"),
                         ".get_steps_for_shortest_paths_from() did not return 2 for a 2-step reachable point")

        self.assertEqual(3, result.get("Bella Casa"),
                         ".get_steps_for_shortest_paths_from() did not return 3 for a 3-step reachable point")
        self.assertEqual(3, result.get("KHG"),
                         ".get_steps_for_shortest_paths_from() did not return 3 for a 3-step reachable point")
        self.assertEqual(3, result.get("Porter"),
                         ".get_steps_for_shortest_paths_from() did not return 3 for a 3-step reachable point")

        self.assertEqual(4, result.get("Spar"),
                         ".get_steps_for_shortest_paths_from() did not return 4 for a 4-step reachable point")
        self.assertEqual(4, result.get("LIT"),
                         ".get_steps_for_shortest_paths_from() did not return 4 for a 4-step reachable point")
        self.assertEqual(4, result.get("Open Lab"),
                         ".get_steps_for_shortest_paths_from() did not return 4 for a 4-step reachable point")

    def test_shortest_path_from_to_none_parameter(self):
        jku_map = JKUMap()

        with self.assertRaises(ValueError) as cm:
            jku_map.get_shortest_path_from_to(None, jku_map.find_vertex("LUI"))
        self.assertTrue(isinstance(cm.exception, ValueError), ".get_shortest_path_from_to() did not throw an expected "
                                                              "ValueError when None was passed as parameter")

        with self.assertRaises(ValueError) as cm:
            jku_map.get_shortest_path_from_to(jku_map.find_vertex("LUI"), None)
        self.assertTrue(isinstance(cm.exception, ValueError), ".get_shortest_path_from_to() did not throw an expected "
                                                              "ValueError when None was passed as parameter")

        with self.assertRaises(ValueError) as cm:
            jku_map.get_shortest_path_from_to(None, None)
        self.assertTrue(isinstance(cm.exception, ValueError),
                        ".get_shortest_path_from_to() did not throw an expected ValueError when None was passed as "
                        "parameter")

    def test_shortest_path_from_to_same_parameter(self):
        jku_map = JKUMap()

        with self.assertRaises(ValueError) as cm:
            jku_map.get_shortest_path_from_to(jku_map.find_vertex("LUI"), jku_map.find_vertex("LUI"))
        self.assertTrue(isinstance(cm.exception, ValueError), ".get_shortest_path_from_to() did not throw an expected "
                                                              "ValueError when the same vertex was passed for both "
                                                              "parameters")

    def test_steps_for_shortest_paths_from_none_parameter(self):
        jku_map = JKUMap()

        with self.assertRaises(ValueError) as cm:
            jku_map.get_steps_for_shortest_paths_from(None)
        self.assertTrue(isinstance(cm.exception, ValueError), ".get_steps_for_shortest_paths_from() did not throw an "
                                                              "expected ValueError when None was passed as parameter")

    def test_shortest_distances_from_none_parameter(self):
        jku_map = JKUMap()

        with self.assertRaises(ValueError) as cm:
            jku_map.get_shortest_distances_from(None)
        self.assertTrue(isinstance(cm.exception, ValueError), ".get_shortest_distances_from() did not throw an "
                                                              "expected ValueError when None was passed as parameter")


if __name__ == '__main__':
    unittest.main()
