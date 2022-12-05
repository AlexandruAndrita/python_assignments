import unittest

#from ad2_ai.assignment03.example01.skeleton.chaining_hash_node import ChainingHashNode
#from ad2_ai.assignment03.example01.skeleton.chaining_hash_set import ChainingHashSet

from chaining_hash_node import ChainingHashNode
from chaining_hash_set import ChainingHashSet


class TestChainingHashSet(unittest.TestCase):
    def insert(self, test_set, key):
        return test_set.insert(int(key))

    def contains(self, test_set, key):
        return test_set.contains(int(key))

    def remove(self, test_set, key):
        return test_set.remove(int(key))

    def fill_set_with_chaining(self):
        test_set = [ChainingHashNode(11), ChainingHashNode(12), ChainingHashNode(13),
                    ChainingHashNode(14), ChainingHashNode(15), ChainingHashNode(5),
                    ChainingHashNode(6), ChainingHashNode(7), ChainingHashNode(8),
                    ChainingHashNode(9), ChainingHashNode(10)]

        test_set[3].next = ChainingHashNode(25)
        test_set[3].next.next = ChainingHashNode(36)

        test_set[6].next = ChainingHashNode(17)

        return test_set

    def fill_set_without_chaining(self):
        return [ChainingHashNode(11), ChainingHashNode(12), ChainingHashNode(13),
                ChainingHashNode(14), ChainingHashNode(15), ChainingHashNode(5),
                ChainingHashNode(6), ChainingHashNode(7), ChainingHashNode(8),
                ChainingHashNode(9), ChainingHashNode(10)]

    def clone(self, orig_set):
        clone_set = [ChainingHashNode()] * len(orig_set)
        for i in range(0, len(orig_set)):
            if orig_set[i] is not None:
                clone_set[i] = ChainingHashNode(orig_set[i].key)
                cur_set = orig_set[i].next
                cur_clone = clone_set[i]
                while cur_set is not None:
                    cur_clone.next = ChainingHashNode(cur_set.key)
                    cur_set = cur_set.next
                    cur_clone = cur_clone.next
                i += 1
        return clone_set

    def test_size_without_chaining(self):
        ex_caught = None
        try:
            stud_set = ChainingHashSet(capacity=11)
            self.assertEqual(stud_set.get_table_size(), 0, ".get_table_size() of empty hash set returned " + str(
                stud_set.get_table_size()) + " but should be 0")

            self.assertTrue(self.insert(stud_set, 5), ".insert(5) returned False but should be True. ")
            self.assertEqual(1, stud_set.get_table_size(), ".get_table_size() of empty hash set returned " + str(
                stud_set.get_table_size()) + " but should be 1")

            self.assertTrue(self.insert(stud_set, 6), ".insert(6) returned False but should be True ")
            self.assertEqual(2, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 2 ")

            self.assertTrue(self.insert(stud_set, 7), ".insert(7) returned False but should be True. ")
            self.assertEqual(3, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 3. ")

            self.assertTrue(self.insert(stud_set, 8), ".insert(8) returned False but should be True. ")
            self.assertEqual(4, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 4. ")

            self.assertTrue(self.insert(stud_set, 9), ".insert(9) returned False but should be True. ")
            self.assertEqual(5, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 5. ")

            self.assertTrue(self.insert(stud_set, 10), ".insert(10) returned False but should be True. ")
            self.assertEqual(6, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 6. ")

            self.assertTrue(self.insert(stud_set, 11), ".insert(11) returned False but should be True. ")
            self.assertEqual(7, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 7. ")

            self.assertTrue(self.insert(stud_set, 12), ".insert(12) returned False but should be True. ")
            self.assertEqual(8, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 8. ")

            self.assertTrue(self.insert(stud_set, 13), ".insert(13) returned False but should be True. ")
            self.assertEqual(9, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 9. ")

            self.assertTrue(self.insert(stud_set, 14), ".insert(14) returned False but should be True. ")
            self.assertEqual(10, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 10. ")

            self.assertTrue(self.insert(stud_set, 15), ".insert(15) returned False but should be True. ")
            self.assertEqual(11, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 11. ")

        except Exception as e:
            ex_caught = e
        self.assertIsNone(ex_caught, "Some unhandled exception raised during testing: " + str(ex_caught))

    def test_size_with_chaining(self):
        ex_caught = None
        try:
            stud_set = ChainingHashSet(capacity=11)
            self.assertEqual(stud_set.get_table_size(), 0, ".get_table_size() of empty hash set returned " + str(
                stud_set.get_table_size()) + " but should be 0")

            self.assertTrue(self.insert(stud_set, 5), ".insert(5) returned False but should be True. ")
            self.assertEqual(1, stud_set.get_table_size(), ".get_table_size() of empty hash set returned " + str(
                stud_set.get_table_size()) + " but should be 1")

            self.assertTrue(self.insert(stud_set, 6), ".insert(6) returned False but should be True ")
            self.assertEqual(2, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 2 ")

            self.assertTrue(self.insert(stud_set, 7), ".insert(7) returned False but should be True. ")
            self.assertEqual(3, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 3. ")

            self.assertTrue(self.insert(stud_set, 8), ".insert(8) returned False but should be True. ")
            self.assertEqual(4, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 4. ")

            self.assertTrue(self.insert(stud_set, 9), ".insert(9) returned False but should be True. ")
            self.assertEqual(5, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 5. ")

            self.assertTrue(self.insert(stud_set, 10), ".insert(10) returned False but should be True. ")
            self.assertEqual(6, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 6. ")

            self.assertTrue(self.insert(stud_set, 11), ".insert(11) returned False but should be True. ")
            self.assertEqual(7, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 7. ")

            self.assertTrue(self.insert(stud_set, 12), ".insert(12) returned False but should be True. ")
            self.assertEqual(8, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 8. ")

            self.assertTrue(self.insert(stud_set, 13), ".insert(13) returned False but should be True. ")
            self.assertEqual(9, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 9. ")

            self.assertTrue(self.insert(stud_set, 14), ".insert(14) returned False but should be True. ")
            self.assertEqual(10, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 10. ")

            self.assertTrue(self.insert(stud_set, 15), ".insert(15) returned False but should be True. ")
            self.assertEqual(11, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 11. ")

            self.assertTrue(self.insert(stud_set, 25), ".insert(25) returned False but should be True. ")
            self.assertEqual(12, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 12. ")

            self.assertTrue(self.insert(stud_set, 36), ".insert(36) returned False but should be True. ")
            self.assertEqual(13, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 13. ")

            self.assertTrue(self.insert(stud_set, 17), ".insert(17) returned False but should be True. ")
            self.assertEqual(14, stud_set.get_table_size(),
                             ".get_table_size() returned " + str(stud_set.get_table_size()) + " but should be 14. ")

        except Exception as e:
            ex_caught = e
        self.assertIsNone(ex_caught, "Some unhandled exception raised during testing: " + str(ex_caught))

    def test_insert_without_chaining(self):
        ex_caught = None
        try:
            stud_set = ChainingHashSet(capacity=11)

            self.assertTrue(self.insert(stud_set, 5), ".insert(5) returned False on empty hash table but must be True.")

            self.assertTrue(self.insert(stud_set, 7), ".insert(7) returned False but should be True. ")

            self.assertTrue(self.insert(stud_set, 8), ".insert(8) returned False but should be True. ")

            self.assertTrue(self.insert(stud_set, 9), ".insert(9) returned False but should be True. ")

            self.assertTrue(self.insert(stud_set, 10), ".insert(10) returned False but should be True. ")

            self.assertTrue(self.insert(stud_set, 6), ".insert(6) returned False but should be True ")

            self.assertTrue(self.insert(stud_set, 11), ".insert(11) returned False but should be True. ")

            self.assertTrue(self.insert(stud_set, 12), ".insert(12) returned False but should be True. ")

            self.assertTrue(self.insert(stud_set, 13), ".insert(13) returned False but should be True. ")

            self.assertTrue(self.insert(stud_set, 14), ".insert(14) returned False but should be True. ")

            self.assertTrue(self.insert(stud_set, 15), ".insert(15) returned False but should be True. ")

            hash_table = stud_set.get_hash_table()

            # Index 0
            self.assertEqual(11, hash_table[0].key,
                             "hash table incorrect after multiple inserts. Expected 11 at index 0 but did not find it. ")
            self.assertEqual(None, hash_table[0].next,
                             "hash table incorrect after multiple inserts. .next at index 0 should be None but was not. ")
            # Index 1
            self.assertEqual(12, hash_table[1].key,
                             "hash table incorrect after multiple inserts. Expected 12 at index 1 but did not find "
                             "it.  ")
            self.assertEqual(None, hash_table[1].next,
                             "hash table incorrect after multiple inserts. .next at index 1 should be None but was not.  ")
            # Index 2
            self.assertEqual(13, hash_table[2].key,
                             "hash table incorrect after multiple inserts. Expected 13 at index 2 but did not find it.  ")
            self.assertEqual(None, hash_table[2].next,
                             "hash table incorrect after multiple inserts. .next at index 2 should be None but was not. ")
            # index5
            self.assertEqual(5, hash_table[5].key,
                             "hash table incorrect after multiple inserts. Expected 5 at index 5 but did not find it.")
            self.assertEqual(None, hash_table[5].next,
                             "hash table incorrect after multiple inserts. .next at index 5 should be None but was not. ")
            # Index 6
            self.assertEqual(6, hash_table[6].key,
                             "hash table incorrect after multiple inserts. Expected 6 at index 6 but did not find it. ")
            self.assertEqual(None, hash_table[6].next,
                             "hash table incorrect after multiple inserts. .next at index 6 should be None but was not.  ")

            # Index 3
            self.assertEqual(14, hash_table[3].key,
                             "hash table incorrect after multiple inserts. Index 3 should be 14 but was not.  ")
            self.assertEqual(None, hash_table[3].next,
                             "hash table incorrect after multiple inserts. .next at index 3 should be None but was not.  ")

            # Index 4
            self.assertEqual(15, hash_table[4].key,
                             "hash table incorrect after multiple inserts. Index 4 should be 15 but was not.  ")
            self.assertEqual(None, hash_table[4].next,
                             "hash table incorrect after multiple inserts. .next at index 4 should be None but was not. ")

            # Index 7
            self.assertEqual(7, hash_table[7].key,
                             "hash table incorrect after multiple inserts. Index 7 should be 7 but was not.  ")
            self.assertEqual(None, hash_table[7].next,
                             "hash table incorrect after multiple inserts. .next at index 7 should be None but was not.  ")

            # Index 8
            self.assertEqual(8, hash_table[8].key,
                             "hash table incorrect after multiple inserts. Index 8 should be 8 but was not.  ")
            self.assertEqual(None, hash_table[8].next,
                             "hash table incorrect after multiple inserts. .next at index 8 should be None but was not.  ")

            # Index 9
            self.assertEqual(9, hash_table[9].key,
                             "hash table incorrect after multiple inserts. Index 9 should be 9 but was not.  ")
            self.assertEqual(None, hash_table[9].next,
                             "hash table incorrect after multiple inserts. .next at index 9 should be None but was not.  ")

            # Index 10
            self.assertEqual(10, hash_table[10].key,
                             "hash table incorrect after multiple inserts. Index 10 should be 10 but was not.  ")
            self.assertEqual(None, hash_table[10].next,
                             "hash table incorrect after multiple inserts. .next at index 10 should be None but was not.  ")

        except Exception as e:
            ex_caught = e
        self.assertIsNone(ex_caught, "Some unhandled exception raised during testing: " + str(ex_caught))

    def test_struct_insert_with_chaining(self):
        ex_caught = None
        try:
            stud_set = ChainingHashSet(capacity=11)

            self.assertTrue(self.insert(stud_set, 5), ".insert(5) returned False on empty hash table but must be True.")

            self.assertTrue(self.insert(stud_set, 7), ".insert(7) returned False but should be True. ")

            self.assertTrue(self.insert(stud_set, 8), ".insert(8) returned False but should be True. ")

            self.assertTrue(self.insert(stud_set, 9), ".insert(9) returned False but should be True. ")

            self.assertTrue(self.insert(stud_set, 10), ".insert(10) returned False but should be True. ")

            self.assertTrue(self.insert(stud_set, 6), ".insert(6) returned False but should be True ")

            self.assertTrue(self.insert(stud_set, 11), ".insert(11) returned False but should be True. ")

            self.assertTrue(self.insert(stud_set, 12), ".insert(12) returned False but should be True. ")

            self.assertTrue(self.insert(stud_set, 13), ".insert(13) returned False but should be True. ")

            self.assertTrue(self.insert(stud_set, 14), ".insert(14) returned False but should be True. ")

            self.assertTrue(self.insert(stud_set, 15), ".insert(15) returned False but should be True. ")

            self.assertTrue(self.insert(stud_set, 25), ".insert(25) returned False but should be True. ")

            self.assertTrue(self.insert(stud_set, 36), ".insert(36) returned False but should be True. ")

            self.assertTrue(self.insert(stud_set, 17), ".insert(17) returned False but should be True. ")

            hash_table = stud_set.get_hash_table()

            # Index 0
            self.assertEqual(11, hash_table[0].key,
                             "hash table incorrect after multiple inserts. Expected 11 at index 0 but did not find it.  ")
            self.assertEqual(None, hash_table[0].next,
                             "hash table incorrect after multiple inserts. .next at index 0 should be None but was not. ")
            # Index 1
            self.assertEqual(12, hash_table[1].key,
                             "hash table incorrect after multiple inserts. Expected 12 at index 1 but did not find it.  ")
            self.assertEqual(None, hash_table[1].next,
                             "hash table incorrect after multiple inserts. .next at index 1 should be None but was not.  ")
            # Index 2
            self.assertEqual(13, hash_table[2].key,
                             "hash table incorrect after multiple inserts. Expected 13 at index 2 but did not find it.  ")
            self.assertEqual(None, hash_table[2].next,
                             "hash table incorrect after multiple inserts. .next at index 2 should be None but was not.  ")
            # index5
            self.assertEqual(5, hash_table[5].key,
                             "hash table incorrect after multiple inserts. Expected 5 at index 5 but did not find it. ")
            self.assertEqual(None, hash_table[5].next,
                             "hash table incorrect after multiple inserts. .next at index 5 should be None but was not. ")
            # Index 6 (chaining)
            self.assertEqual(6, hash_table[6].key,
                             "hash table incorrect after multiple inserts. Expected 6 at index 6 but did not find it. ")
            self.assertEqual(17, hash_table[6].next.key,
                             "hash table incorrect after multiple inserts. .next at index 6 should be 17 but was not.  ")
            self.assertEqual(None, hash_table[6].next.next,
                             "hash table incorrect after multiple inserts. .next.next at index 6 should be None but was not.  ")

            # Index 3 (chaining)
            self.assertEqual(14, hash_table[3].key,
                             "hash table incorrect after multiple inserts. Index 3 should be 14 but was not.  ")
            self.assertEqual(25, hash_table[3].next.key,
                             "hash table incorrect after multiple inserts. .next at index 3 should be 25 but was not.  ")
            self.assertEqual(36, hash_table[3].next.next.key,
                             "hash table incorrect after multiple inserts. .next.next at index 3 should be 36 but was not.  ")
            self.assertEqual(None, hash_table[3].next.next.next,
                             "hash table incorrect after multiple inserts. .next.next.next at index 3 should be None but was not.  ")

            # Index 4
            self.assertEqual(15, hash_table[4].key,
                             "hash table incorrect after multiple inserts. Index 4 should be 15 but was not. ")
            self.assertEqual(None, hash_table[4].next,
                             "hash table incorrect after multiple inserts. .next at index 4 should be None but was not.  ")

            # Index 7
            self.assertEqual(7, hash_table[7].key,
                             "hash table incorrect after multiple inserts. Index 7 should be 7 but was not. ")
            self.assertEqual(None, hash_table[7].next,
                             "hash table incorrect after multiple inserts. .next at index 7 should be None but was not.  ")

            # Index 8
            self.assertEqual(8, hash_table[8].key,
                             "hash table incorrect after multiple inserts. Index 8 should be 8 but was not.  ")
            self.assertEqual(None, hash_table[8].next,
                             "hash table incorrect after multiple inserts. .next at index 8 should be None but was not.  ")

            # Index 9
            self.assertEqual(9, hash_table[9].key,
                             "hash table incorrect after multiple inserts. Index 9 should be 9 but was not.  ")
            self.assertEqual(None, hash_table[9].next,
                             "hash table incorrect after multiple inserts. .next at index 9 should be None but was not.  ")

            # Index 10
            self.assertEqual(10, hash_table[10].key,
                             "hash table incorrect after multiple inserts. Index 10 should be 10 but was not.  ")
            self.assertEqual(None, hash_table[10].next,
                             "hash table incorrect after multiple inserts. .next at index 10 should be None but was not.  ")

        except Exception as e:
            ex_caught = e
        self.assertIsNone(ex_caught, "Some unhandled exception raised during testing: " + str(ex_caught))

    def test_clear_with_chaining(self):
        ex_caught = None
        try:
            stud_set = ChainingHashSet()
            sol_set = self.fill_set_with_chaining()
            stud_set.set_hash_table(self.clone(sol_set))
            self.assertTrue(stud_set.get_table_size() > 0,
                            ".get_table_size() returned incorrect value after set_hash_table() ")
            stud_set.clear()
            hash_table = stud_set.get_hash_table()
            self.assertEqual(0, stud_set.get_table_size(),
                             ".get_table_size() returned incorrect value after .clear()  ")

            for i in range(0, len(hash_table)):
                self.assertEqual(None, hash_table[i], "hash table at index " + str(
                    i) + "must be None after .clear() but was not ")

        except Exception as e:
            ex_caught = e
        self.assertIsNone(ex_caught, "Some unhandled exception raised during testing: " + str(ex_caught))

    def test_clear_without_chaining(self):
        ex_caught = None
        sol_set = self.fill_set_without_chaining()
        stud_set = ChainingHashSet()
        try:
            stud_set.set_hash_table(self.clone(sol_set))

            self.assertTrue(stud_set.get_table_size() > 0,
                            ".get_table_size() returned incorrect value after set_hash_table()")
            stud_set.clear()
            hash_table = stud_set.get_hash_table()
            self.assertEqual(0, stud_set.get_table_size(),
                             ".get_table_size() returned incorrect value after .clear()")

            for i in range(0, len(hash_table)):
                self.assertEqual(None, hash_table[i], "hash table at index " + str(
                    i) + "must be None after .clear() but was not")

        except Exception as e:
            ex_caught = e
        self.assertIsNone(ex_caught, "Some unhandled exception raised during testing: " + str(ex_caught))

    def test_size_remove_without_chaining(self):
        ex_caught = None
        sol_set = self.fill_set_without_chaining()
        try:
            stud_set = ChainingHashSet(capacity=1)
            sol_copy = self.clone(sol_set)
            stud_set.set_hash_table(sol_copy)

            # /*remove non chained node*/
            self.assertTrue(stud_set.remove(11), ".remove(11) returned False but must be True ")

            self.assertEqual(10, stud_set.get_table_size(),
                             ".get_table_size() returned wrong size (" + str(stud_set.get_table_size()) + ") on " +
                             "remove key 11 but should be " + str(10))

            # /*remove at end of chaining list*/
            self.assertTrue(stud_set.remove(12), ".remove(17) returned False but must be True ")
            self.assertEqual(9, stud_set.get_table_size(),
                             ".get_table_size() returned wrong size")

            # /*remove in mid of chaining list*/
            self.assertTrue(stud_set.remove(13), ".remove(25) returned False but must be True ")

            self.assertEqual(8, stud_set.get_table_size(),
                             ".get_table_size() returned wrong size ")

            # /*remove beginning of chaining list*/
            self.assertTrue(stud_set.remove(14), ".remove(14) returned False but must be True ")
            self.assertEqual(7, stud_set.get_table_size(),
                             ".get_table_size() returned wrong size")

        except Exception as e:
            ex_caught = e
        self.assertIsNone(ex_caught, "Some unhandled exception raised during testing: " + str(ex_caught))

    def test_size_remove_with_chaining(self):
        ex_caught = None
        sol_set = self.fill_set_with_chaining()
        try:
            stud_set = ChainingHashSet()
            sol_copy = self.clone(sol_set)
            stud_set.set_hash_table(sol_copy)

            # /*remove chained node*/
            print(stud_set.get_table_size())
            self.assertTrue(stud_set.remove(17), ".remove(17) returned False but must be True ")

            self.assertEqual(13, stud_set.get_table_size(),
                             ".get_table_size() returned wrong size (" + str(stud_set.get_table_size()) + ") on " +
                             "remove key 17 but should be " + str(13))

            # /*remove at end of chaining list*/
            self.assertTrue(stud_set.remove(36), ".remove(36) returned False but must be True ")
            self.assertEqual(12, stud_set.get_table_size(),
                             ".get_table_size() returned wrong size")

            # /*remove in mid of chaining list*/
            self.assertTrue(stud_set.remove(25), ".remove(14) returned False but must be True ")

            self.assertEqual(11, stud_set.get_table_size(),
                             ".get_table_size() returned wrong size")

        except Exception as e:
            ex_caught = e
        self.assertIsNone(ex_caught, "Some unhandled exception raised during testing: " + str(ex_caught))

    def test_struct_remove_without_chaining(self):
        ex_caught = None
        sol_set = self.fill_set_without_chaining()
        try:
            stud_set = ChainingHashSet(capacity=1)
            sol_copy = self.clone(sol_set)
            stud_set.set_hash_table(sol_copy)

            self.assertTrue(stud_set.remove(11), ".remove(11) returned False but must be True ")
            stud_nodes = stud_set.get_hash_table()

            self.assertEqual(None, stud_nodes[0],
                             "incorrect node at index 0 after .remove(11) must be None but was not.")

            self.assertTrue(stud_set.remove(12), ".remove(12) returned False but must be True ")
            stud_nodes = stud_set.get_hash_table()
            self.assertEqual(None, stud_nodes[1],
                             "incorrect node at index 1 after .remove(12) must be None but was not.")

            self.assertTrue(stud_set.remove(13), ".remove(13) returned False but must be True ")
            stud_nodes = stud_set.get_hash_table()
            self.assertEqual(None, stud_nodes[2],
                             "incorrect node at index 2 after .remove(13) must be None but was not.")

            # /*remove beginning of chaining list*/
            self.assertTrue(stud_set.remove(14), ".remove(14) returned False but must be True ")
            stud_nodes = stud_set.get_hash_table()
            self.assertEqual(None, stud_nodes[3],
                             "incorrect node at index 3 after .remove(14) must be None but was not.")
        except Exception as e:
            ex_caught = e
        self.assertIsNone(ex_caught, "Some unhandled exception raised during testing: " + str(ex_caught))

    def test_struct_remove_with_chaining(self):
        ex_caught = None
        sol_set = self.fill_set_with_chaining()
        try:
            stud_set = ChainingHashSet(capacity=1)
            sol_copy = self.clone(sol_set)
            stud_set.set_hash_table(sol_copy)

            self.assertTrue(stud_set.remove(17), ".remove(17) returned False but must be True ")

            stud_nodes = stud_set.get_hash_table()

            self.assertEqual(None, stud_nodes[6].next,
                             "incorrect node at index 6 after .remove(17) must be None but was not.")
            self.assertEqual(6, stud_nodes[6].key,
                             "incorrect node at index 6 after .remove(17) must be 6 but was not.")

            # /*remove in mid of chaining list*/
            self.assertTrue(stud_set.remove(25), ".remove(25) returned False but must be True on hash set ")
            stud_nodes = stud_set.get_hash_table()
            self.assertEqual(14, stud_nodes[3].key,
                             "incorrect node at index 3 after .remove(25) must be 14 but was not.")
            self.assertEqual(36, stud_nodes[3].next.key,
                             "incorrect node at index 3.next after .remove(25) must be 36 but was not.")
            self.assertEqual(None, stud_nodes[3].next.next,
                             "incorrect node at index 3.next.next after .remove(25) must be None but was not.")

            # /*remove beginning of chaining list*/
            self.assertTrue(stud_set.remove(14), ".remove(14) returned False but must be True ")
            stud_nodes = stud_set.get_hash_table()
            self.assertEqual(36, stud_nodes[3].key,
                             "incorrect node at index 3 after .remove(14) " + " must be 36 but was not.")
            self.assertEqual(None, stud_nodes[3].next,
                             "incorrect node at index 3.next after .remove(14) " + " must be None but was not.")

        except Exception as e:
            ex_caught = e
        self.assertIsNone(ex_caught, "Some unhandled exception raised during testing: " + str(ex_caught))

    def test_contains_with_chaining(self):
        sol_set = self.fill_set_with_chaining()
        stud_set = ChainingHashSet(capacity=1)
        ex_caught = None
        try:

            sol_copy = self.clone(sol_set)
            stud_set.set_hash_table(sol_copy)

            self.assertTrue(stud_set.contains(11), ".contains(11) returned False but must be True  ")
            self.assertTrue(stud_set.contains(12), ".contains(12) returned False but must be True  ")
            self.assertTrue(stud_set.contains(13), ".contains(13) returned False but must be True  ")
            self.assertTrue(stud_set.contains(14), ".contains(14) returned False but must be True  ")
            self.assertTrue(stud_set.contains(15), ".contains(15) returned False but must be True  ")
            self.assertTrue(stud_set.contains(5), ".contains(5) returned False but must be True  ")
            self.assertTrue(stud_set.contains(6), ".contains(6) returned False but must be True  ")
            self.assertTrue(stud_set.contains(7), ".contains(7) returned False but must be True  ")
            self.assertTrue(stud_set.contains(8), ".contains(8) returned False but must be True  ")
            self.assertTrue(stud_set.contains(9), ".contains(9) returned False but must be True  ")
            self.assertTrue(stud_set.contains(10), ".contains(10) returned False but must be True  ")
            self.assertTrue(stud_set.contains(25), ".contains(25) returned False but must be True  ")
            self.assertTrue(stud_set.contains(36), ".contains(36) returned False but must be True  ")
            self.assertTrue(stud_set.contains(17), ".contains(17) returned False but must be True  ")
            self.assertFalse(stud_set.contains(18), ".contains(18) returned True but must be False  ")

        except Exception as e:
            ex_caught = e
        self.assertIsNone(ex_caught, "Some unhandled exception raised during testing: " + str(ex_caught))

    def test_contains_without_chaining(self):
        ex_caught = None
        sol_set = self.fill_set_without_chaining()
        try:
            stud_set = ChainingHashSet(capacity=1)
            sol_copy = self.clone(sol_set)
            stud_set.set_hash_table(sol_copy)

            self.assertTrue(stud_set.contains(11), ".contains(11) returned False but must be True  ")
            self.assertTrue(stud_set.contains(12), ".contains(12) returned False but must be True  ")
            self.assertTrue(stud_set.contains(13), ".contains(13) returned False but must be True  ")
            self.assertTrue(stud_set.contains(14), ".contains(14) returned False but must be True  ")
            self.assertTrue(stud_set.contains(15), ".contains(15) returned False but must be True  ")
            self.assertTrue(stud_set.contains(5), ".contains(5) returned False but must be True  ")
            self.assertTrue(stud_set.contains(6), ".contains(6) returned False but must be True  ")
            self.assertTrue(stud_set.contains(7), ".contains(7) returned False but must be True  ")
            self.assertTrue(stud_set.contains(8), ".contains(8) returned False but must be True  ")
            self.assertTrue(stud_set.contains(9), ".contains(9) returned False but must be True  ")
            self.assertTrue(stud_set.contains(10), ".contains(10) returned False but must be True  ")
        except Exception as e:
            ex_caught = e
        self.assertIsNone(ex_caught, "Some unhandled exception raised during testing: " + str(ex_caught))

    def test_insert_false(self):

        stud_set = ChainingHashSet(11)
        self.assertTrue(self.insert(stud_set, 5), "insert(5) returned false but must be true")
        self.assertFalse(self.insert(stud_set, 5), "insert(5) returned true but must be false")
        self.assertTrue(self.insert(stud_set, 16), "insert(16) returned false but must be true")
        self.assertFalse(self.insert(stud_set, 16), "insert(16) returned true but must be false")

    def test_remove_non_existing(self):
        stud_set = ChainingHashSet(11)
        self.assertFalse(stud_set.remove(1), "remove(1) on empty hash table returned true but must be false")

    def test_contains_false(self):
        stud_set = ChainingHashSet(11)
        self.assertFalse(stud_set.contains(1), "contains(1) on empty hash table returned true but must be false")

    def test_get_hash_table(self):
        stud_set = ChainingHashSet(capacity=11)
        hash_table = stud_set.get_hash_table()
        for n in hash_table:
            self.assertIsNone(n)

    def test_insert_with_chaining(self):
        stud_set = ChainingHashSet(capacity=11)
        self.assertEqual(0, stud_set.get_table_size())

        self.assertTrue(self.insert(stud_set, 5))
        self.assertEqual(1, stud_set.get_table_size())

        self.assertTrue(self.insert(stud_set, 6))
        self.assertEqual(2, stud_set.get_table_size())

        self.assertTrue(self.insert(stud_set, 11))
        self.assertEqual(3, stud_set.get_table_size())

        self.assertTrue(self.insert(stud_set, 12))
        self.assertEqual(4, stud_set.get_table_size())

        self.assertTrue(self.insert(stud_set, 13))
        self.assertEqual(5, stud_set.get_table_size())

        self.assertTrue(self.insert(stud_set, 17))
        self.assertEqual(6, stud_set.get_table_size())

        # check content
        hash_table = stud_set.get_hash_table()
        # Index 0
        self.assertEqual(11, hash_table[0].key)
        self.assertEqual(None, hash_table[0].next)
        # Index 1
        self.assertEqual(12, hash_table[1].key)
        self.assertEqual(None, hash_table[1].next)
        # Index 2
        self.assertEqual(13, hash_table[2].key)
        self.assertEqual(None, hash_table[2].next)
        # Index 3
        self.assertEqual(None, hash_table[3])
        # Index 4
        self.assertEqual(None, hash_table[4])
        # Index 5
        self.assertEqual(5, hash_table[5].key)
        self.assertEqual(None, hash_table[5].next)
        # Index 6 (chaining)
        self.assertEqual(6, hash_table[6].key)
        self.assertIsNotNone(hash_table[6].next)
        self.assertEqual(17, hash_table[6].next.key)
        self.assertEqual(None, hash_table[6].next.next)
        # Index 7
        self.assertEqual(None, hash_table[7])
        # Index 8
        self.assertEqual(None, hash_table[8])
        # Index 9
        self.assertEqual(None, hash_table[9])
        # Index 10
        self.assertEqual(None, hash_table[10])


if __name__ == '__main__':
    unittest.main()
