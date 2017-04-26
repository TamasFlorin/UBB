import unittest
from domain.custom import Iterable
from domain.entities import Person
from domain.custom import sort
from domain.custom import filter

class TestCustom(unittest.TestCase):
    def test_iterable(self):
        it = Iterable()
        
        # test adding items
        it[0] = 0
        it[1] = 1

        self.assertEqual(it[0],0,"First item should be 0.")
        self.assertEqual(len(it),2,"Iterable length should be 2.")

        # test delete items
        del it[1]
        self.assertEqual(len(it),1,"Iterable length should be 1")

        # test iterable functions
        it[1] = 3
        it[2] = 2
        item = next(it)
        item = next(it)

        self.assertEqual(item,(1,3),"Item should be (1,3).")

        iterator = iter(it)

        item = next(iterator)

        self.assertEqual(item,(0,0),"Item should be (0,0)")

        self.assertTrue(0 in it,"Result should be true.")

        self.assertEqual(str(it),"[0,3,2]","String representation should be [0,3,2].")

    def test_sort(self):
        list = [4,3,2,1]
        sort(list)
        self.assertEqual(list,[1,2,3,4],"The list should be in sorted order.")

    def test_filter(self):
        list = [1,2,3,4,5]
        list = filter(lambda x: x>2,list)

        self.assertEqual(list,[3,4,5],"The list should be [3,4,5]")

        

if __name__ == '__main__':
    unittest.main()
