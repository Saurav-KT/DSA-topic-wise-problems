import unittest
from singly_linked_list import SingleLinkedList

class TestLinkedList(unittest.TestCase):
    def test_insert_at_beginning(self):
        # Insert_at_beginning on an empty list
        print('Test: insert_at_beginning')

        linked_list = SingleLinkedList()
        linked_list.insert_at_beginning(5)
        linked_list.insert_at_beginning(10)
        self.assertEqual(linked_list.display_all(),[10,5])

       # Test: insert at_beginning on a None
        linked_list.insert_at_beginning(None)
        self.assertEqual(linked_list.display_all(), [10,5])


    def test_insert_at_end(self):
        print('Test: insert_at_end')
        linked_list= SingleLinkedList()
        linked_list.insert_at_beginning(5)
        linked_list.insert_at_end(20)
        self.assertEqual(linked_list.display_all(),[5,20])

    def test_insert_at_middle(self):
        print('Test: insert at middle')
        linked_list= SingleLinkedList()
        linked_list.insert_at_beginning(5) # Add at least one element first
        linked_list.insert_at_end(10)

        # Test valid insertion in middle
        linked_list.insert_at_specific_position(1,15)
        self.assertEqual(linked_list.display_all(),[5,15,10])

        # Test invalid positions(should raise IndexError)
        with self.assertRaises(IndexError):
            linked_list.insert_at_specific_position(position=-1,data=40) # Negative position

        with self.assertRaises(IndexError):
            linked_list.insert_at_specific_position(6,100) # Position beyond list length

    def test_search_element(self):
        print('Test: Search element')

        print('Test: find on an empty list')
        linked_list = SingleLinkedList()
        node = linked_list.search_element('a')
        self.assertEqual(node, None)

        print('Test: find a None')
        linked_list = SingleLinkedList()
        linked_list.insert_at_beginning(5)
        node = linked_list.search_element(None)
        self.assertEqual(node, None)

        print('Test: find general case with matches')
        linked_list = SingleLinkedList()
        linked_list.insert_at_beginning(5)
        linked_list.insert_at_beginning(10)
        linked_list.insert_at_beginning(15)
        data= linked_list.search_element(10)
        self.assertEqual(data,10)

        print('Test: find general case with no matches')
        data = linked_list.search_element(40)
        self.assertEqual(data, None)





def main():
    test=TestLinkedList()
    test.test_insert_at_beginning()
    test.test_insert_at_end()
    test.test_insert_at_middle()
if __name__ == '__main__':
    main()
