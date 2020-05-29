import unittest
from Binary_Search_Tree import Binary_Search_Tree

class Binary_Search_Tree_Tester(unittest.TestCase):

  def setUp(self):
      self.__string_list = Binary_Search_Tree()

  def test_empty_tree_string(self):
      self.assertEqual('[ ]', str(self.__string_list), 'Empty list should print as "[ ]"')

  def test_insert_right_right_imbalance(self):
      self.__string_list.insert_element(2)
      self.__string_list.insert_element(1)
      self.__string_list.insert_element(4)
      self.__string_list.insert_element(3)
      self.__string_list.insert_element(6)
      returned=self.__string_list.insert_element(5)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6 ]', str(self.__string_list))
      self.assertEqual('[ 1, 3, 2, 5, 6, 4 ]', str(self.__string_list.post_order()))
      self.assertEqual('[ 4, 2, 1, 3, 6, 5 ]', str(self.__string_list.pre_order()))


  def test_insert_left_left_imbalance(self):
      self.__string_list.insert_element(5)
      self.__string_list.insert_element(6)
      self.__string_list.insert_element(3)
      self.__string_list.insert_element(4)
      self.__string_list.insert_element(1)
      returned=self.__string_list.insert_element(2)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6 ]', str(self.__string_list))
      self.assertEqual('[ 2, 1, 4, 6, 5, 3 ]', str(self.__string_list.post_order()))
      self.assertEqual('[ 3, 1, 2, 5, 4, 6 ]', str(self.__string_list.pre_order()))

  def test_insert_right_left_imbalance(self):
      self.__string_list.insert_element(2)
      self.__string_list.insert_element(1)
      self.__string_list.insert_element(5)
      self.__string_list.insert_element(6)
      self.__string_list.insert_element(4)
      returned=self.__string_list.insert_element(3)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6 ]', str(self.__string_list))
      self.assertEqual('[ 1, 3, 2, 6, 5, 4 ]', str(self.__string_list.post_order()))
      self.assertEqual('[ 4, 2, 1, 3, 5, 6 ]', str(self.__string_list.pre_order()))

  def test_insert_left_right_imbalce(self):
      self.__string_list.insert_element(5)
      self.__string_list.insert_element(6)
      self.__string_list.insert_element(2)
      self.__string_list.insert_element(1)
      self.__string_list.insert_element(3)
      returned=self.__string_list.insert_element(4)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6 ]', str(self.__string_list))
      self.assertEqual('[ 1, 2, 4, 6, 5, 3 ]', str(self.__string_list.post_order()))
      self.assertEqual('[ 3, 2, 1, 5, 4, 6 ]', str(self.__string_list.pre_order()))

  def test_remove_right_right_imbalance(self):
      self.__string_list.insert_element(2)
      self.__string_list.insert_element(1)
      self.__string_list.insert_element(4)
      self.__string_list.insert_element(0)
      self.__string_list.insert_element(3)
      self.__string_list.insert_element(6)
      self.__string_list.insert_element(5)
      returned=self.__string_list.remove_element(0)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6 ]', str(self.__string_list))
      self.assertEqual('[ 1, 3, 2, 5, 6, 4 ]', str(self.__string_list.post_order()))
      self.assertEqual('[ 4, 2, 1, 3, 6, 5 ]', str(self.__string_list.pre_order()))


  def test_remove_left_left_imbalance(self):
      self.__string_list.insert_element(5)
      self.__string_list.insert_element(6)
      self.__string_list.insert_element(3)
      self.__string_list.insert_element(7)
      self.__string_list.insert_element(4)
      self.__string_list.insert_element(1)
      self.__string_list.insert_element(2)
      returned=self.__string_list.remove_element(7)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6 ]', str(self.__string_list))
      self.assertEqual('[ 2, 1, 4, 6, 5, 3 ]', str(self.__string_list.post_order()))
      self.assertEqual('[ 3, 1, 2, 5, 4, 6 ]', str(self.__string_list.pre_order()))

  def test_remove_right_left_imbalance(self):
      self.__string_list.insert_element(2)
      self.__string_list.insert_element(1)
      self.__string_list.insert_element(5)
      self.__string_list.insert_element(0)
      self.__string_list.insert_element(6)
      self.__string_list.insert_element(4)
      self.__string_list.insert_element(3)
      returned=self.__string_list.remove_element(0)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6 ]', str(self.__string_list))
      self.assertEqual('[ 1, 3, 2, 6, 5, 4 ]', str(self.__string_list.post_order()))
      self.assertEqual('[ 4, 2, 1, 3, 5, 6 ]', str(self.__string_list.pre_order()))

  def test_remove_left_right_imbalce(self):
      self.__string_list.insert_element(5)
      self.__string_list.insert_element(6)
      self.__string_list.insert_element(2)
      self.__string_list.insert_element(7)
      self.__string_list.insert_element(1)
      self.__string_list.insert_element(3)
      self.__string_list.insert_element(4)
      returned=self.__string_list.remove_element(7)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6 ]', str(self.__string_list))
      self.assertEqual('[ 1, 2, 4, 6, 5, 3 ]', str(self.__string_list.post_order()))
      self.assertEqual('[ 3, 2, 1, 5, 4, 6 ]', str(self.__string_list.pre_order()))


  def test_insert_empty(self):
      returned=self.__string_list.insert_element(4)
      self.assertEqual('[ 4 ]', str(self.__string_list))
      self.assertEqual('[ 4 ]', str(self.__string_list.post_order()))
      self.assertEqual('[ 4 ]', str(self.__string_list.pre_order()))

  def test_insert_smallest_val_tree_height_1(self):
      self.__string_list.insert_element(4)
      returned=self.__string_list.insert_element(2)
      self.assertEqual('[ 2, 4 ]', str(self.__string_list))
      self.assertEqual('[ 4, 2 ]', str(self.__string_list.pre_order()))
      self.assertEqual('[ 2, 4 ]', str(self.__string_list.post_order()))


  def test_insert_largest_val_tree_height_1(self):
      self.__string_list.insert_element(4)
      returned=self.__string_list.insert_element(6)
      self.assertEqual('[ 4, 6 ]', str(self.__string_list))
      self.assertEqual('[ 4, 6 ]', str(self.__string_list.pre_order()))
      self.assertEqual('[ 6, 4 ]', str(self.__string_list.post_order()))


  def test_insert_smallest_val_tree_height_3(self):
      self.__string_list.insert_element(4)
      self.__string_list.insert_element(6)
      self.__string_list.insert_element(2)
      self.__string_list.insert_element(3)
      self.__string_list.insert_element(5)
      self.__string_list.insert_element(7)
      returned=self.__string_list.insert_element(1)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7 ]', str(self.__string_list))
      self.assertEqual('[ 4, 2, 1, 3, 6, 5, 7 ]', str(self.__string_list.pre_order()))
      self.assertEqual('[ 1, 3, 2, 5, 7, 6, 4 ]', str(self.__string_list.post_order()))

  def test_insert__largest_val_tree_height_3(self):
      self.__string_list.insert_element(4)
      self.__string_list.insert_element(6)
      self.__string_list.insert_element(2)
      self.__string_list.insert_element(3)
      self.__string_list.insert_element(5)
      self.__string_list.insert_element(1)
      returned=self.__string_list.insert_element(7)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7 ]', str(self.__string_list))
      self.assertEqual('[ 4, 2, 1, 3, 6, 5, 7 ]', str(self.__string_list.pre_order()))
      self.assertEqual('[ 1, 3, 2, 5, 7, 6, 4 ]', str(self.__string_list.post_order()))

  def test_insert_middle_val_tree_height_3(self):
      self.__string_list.insert_element(4)
      self.__string_list.insert_element(6)
      self.__string_list.insert_element(2)
      self.__string_list.insert_element(5)
      self.__string_list.insert_element(1)
      self.__string_list.insert_element(7)
      returned=self.__string_list.insert_element(3)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7 ]', str(self.__string_list))
      self.assertEqual('[ 4, 2, 1, 3, 6, 5, 7 ]', str(self.__string_list.pre_order()))
      self.assertEqual('[ 1, 3, 2, 5, 7, 6, 4 ]', str(self.__string_list.post_order()))

  def test_insert_same_value(self):
      self.__string_list.insert_element(3)
      with self.assertRaises(ValueError):
          returned = self.__string_list.insert_element(3)
      self.assertEqual('[ 3 ]', str(self.__string_list))

  def test_remove_empty(self):
      with self.assertRaises(ValueError):
          returned = self.__string_list.remove_element(3)
      self.assertEqual('[ ]', str(self.__string_list))

  def test_remove_unkown_val_tree_height_3(self):
      self.__string_list.insert_element(4)
      self.__string_list.insert_element(6)
      self.__string_list.insert_element(2)
      self.__string_list.insert_element(3)
      self.__string_list.insert_element(5)
      self.__string_list.insert_element(1)
      self.__string_list.insert_element(7)
      with self.assertRaises(ValueError):
        returned=self.__string_list.remove_element(10)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7 ]', str(self.__string_list))

  def test_remove_root_tree_height_1(self):
      self.__string_list.insert_element(4)
      returned=self.__string_list.remove_element(4)
      self.assertEqual('[ ]', str(self.__string_list))

  def test_remove_root_tree_height_3(self):
      self.__string_list.insert_element(4)
      self.__string_list.insert_element(6)
      self.__string_list.insert_element(2)
      self.__string_list.insert_element(3)
      self.__string_list.insert_element(5)
      self.__string_list.insert_element(1)
      self.__string_list.insert_element(7)
      returned=self.__string_list.remove_element(4)
      self.assertEqual('[ 1, 2, 3, 5, 6, 7 ]', str(self.__string_list))
      self.assertEqual('[ 5, 2, 1, 3, 6, 7 ]', str(self.__string_list.pre_order()))
      self.assertEqual('[ 1, 3, 2, 7, 6, 5 ]', str(self.__string_list.post_order()))

  def test_remove_smallest_val_tree_height_3(self):
      self.__string_list.insert_element(4)
      self.__string_list.insert_element(6)
      self.__string_list.insert_element(2)
      self.__string_list.insert_element(3)
      self.__string_list.insert_element(5)
      self.__string_list.insert_element(1)
      self.__string_list.insert_element(7)
      returned=self.__string_list.remove_element(1)
      self.assertEqual('[ 2, 3, 4, 5, 6, 7 ]', str(self.__string_list))
      self.assertEqual('[ 4, 2, 3, 6, 5, 7 ]', str(self.__string_list.pre_order()))
      self.assertEqual('[ 3, 2, 5, 7, 6, 4 ]', str(self.__string_list.post_order()))

  def test_remove_largest_val_tree_height_3(self):
      self.__string_list.insert_element(4)
      self.__string_list.insert_element(6)
      self.__string_list.insert_element(2)
      self.__string_list.insert_element(3)
      self.__string_list.insert_element(5)
      self.__string_list.insert_element(1)
      self.__string_list.insert_element(7)
      returned=self.__string_list.remove_element(7)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6 ]', str(self.__string_list))
      self.assertEqual('[ 4, 2, 1, 3, 6, 5 ]', str(self.__string_list.pre_order()))
      self.assertEqual('[ 1, 3, 2, 5, 6, 4 ]', str(self.__string_list.post_order()))

  def test_remove_middle_tree_height_3(self):
      self.__string_list.insert_element(4)
      self.__string_list.insert_element(6)
      self.__string_list.insert_element(2)
      self.__string_list.insert_element(3)
      self.__string_list.insert_element(5)
      self.__string_list.insert_element(1)
      self.__string_list.insert_element(7)
      returned=self.__string_list.remove_element(3)
      self.assertEqual('[ 1, 2, 4, 5, 6, 7 ]', str(self.__string_list))
      self.assertEqual('[ 4, 2, 1, 6, 5, 7 ]', str(self.__string_list.pre_order()))
      self.assertEqual('[ 1, 2, 5, 7, 6, 4 ]', str(self.__string_list.post_order()))

  def test_remove_node_with_two_children(self):
      self.__string_list.insert_element(4)
      self.__string_list.insert_element(6)
      self.__string_list.insert_element(2)
      self.__string_list.insert_element(3)
      self.__string_list.insert_element(5)
      self.__string_list.insert_element(1)
      self.__string_list.insert_element(7)
      returned=self.__string_list.remove_element(2)
      self.assertEqual('[ 1, 3, 4, 5, 6, 7 ]', str(self.__string_list))
      self.assertEqual('[ 4, 3, 1, 6, 5, 7 ]', str(self.__string_list.pre_order()))
      self.assertEqual('[ 1, 3, 5, 7, 6, 4 ]', str(self.__string_list.post_order()))

  def test_remove_node_with_no_children(self):
      self.__string_list.insert_element(1)
      self.__string_list.insert_element(7)
      self.__string_list.insert_element(6)
      self.__string_list.insert_element(5)
      self.__string_list.insert_element(4)
      self.__string_list.insert_element(3)
      self.__string_list.insert_element(2)
      returned=self.__string_list.remove_element(2)
      self.assertEqual('[ 1, 3, 4, 5, 6, 7 ]', str(self.__string_list))



  def test_get_height_empty(self):
      self.assertEqual(0, self.__string_list.get_height())

  def test_get_height_after_removal(self):
      self.__string_list.insert_element(1)
      self.__string_list.insert_element(5)
      self.__string_list.insert_element(6)
      self.__string_list.insert_element(7)
      self.__string_list.insert_element(4)
      self.__string_list.insert_element(3)
      self.__string_list.insert_element(2)
      returned=self.__string_list.remove_element(3)
      self.assertEqual(3,self.__string_list.get_height())

  def test_get_height_after_insert(self):
      self.__string_list.insert_element(1)
      self.__string_list.insert_element(5)
      self.__string_list.insert_element(6)
      self.__string_list.insert_element(7)
      self.__string_list.insert_element(4)
      self.__string_list.insert_element(3)
      returned=self.__string_list.insert_element(2)
      self.assertEqual(4,self.__string_list.get_height())

if __name__ == '__main__':
    unittest.main()
