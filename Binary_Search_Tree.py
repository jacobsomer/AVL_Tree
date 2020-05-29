class Binary_Search_Tree:


  class __BST_Node:


    def __init__(self, value):
      self.value = value
      self.left=None
      self.right=None
      self.height=1
      return


  def __init__(self):
      self.__root = None
      self.__height=0
      self.__size=0

  def __balanced(self,t):
      def __check_imbalance(root):   #checks for the imbalance of the root
          if root.height==1:  #if leaf node
              return "balanced"
          if root.left is None:
              left_height=0
          if root.right is None:#if child is none, child height is 0
              right_height=0
          if root.left is not None:   #else, child height is height attribute
              left_height=root.left.height
          if root.right is not None:
              right_height=root.right.height
          if left_height-right_height<2 and left_height-right_height>=0:
              return "balanced"
          if right_height-left_height<2 and right_height-left_height>=0:
              return "balanced"
          elif left_height-right_height==2:
              return "left"
          elif right_height-left_height==2:
              return "right"

      def __sub_check_imbalance(root):  #check the imbalance of a subroot of an already imbalanced tree
          if root.left is None:
              left_height=0
          if root.right is None:
              right_height=0
          if root.left is not None:
              left_height=root.left.height
          if root.right is not None:
              right_height=root.right.height
          if left_height-right_height==1:   #if subroot imbalance is greater than 1
              return "left"
          elif right_height-left_height==1:
              return "right"

      def __rotate_right(root):    #this method works the same as rotate left but opposite sides
          def __get_height(root):           #private method to recursively keep track of the height
              root_height=0
              if root.right is None and root.left is None:          #if a leaf node, height is 1
                  root_height=1
              elif root.left is not None and root.right is None:   #if only has a left child, height is left child's height+1
                  root_height=root.left.height+1
              elif root.right is not None and root.left is None:    #if only has a right child, height is right child's height+1
                  root_height=root.right.height+1
              elif root.right is not None and root.left is not None:     #if two children, height is larger child's height +1
                  if root.right.height > root.left.height:
                      root_height=root.right.height+1
                  elif root.left.height > root.right.height:
                      root_height=root.left.height+1
                  elif root.left.height == root.right.height:
                      root_height= root.left.height+1
              root.height=root_height
              return root
          new_root=root.left
          aux_root=None
          if new_root.right is not None:
              aux_root=new_root.right
              new_root.right=root
              new_root.right.left=aux_root
          else:
              new_root.right=root
              new_root.right.left=aux_root
          new_root.right=__get_height(new_root.right)
          new_root=__get_height(new_root)
          return new_root

      def __rotate_left(root):
          def __get_height(root):           #private method to recursively keep track of the height
              if root is None:
                  return root
              root_height=0
              if root.right is None and root.left is None:          #if a leaf node, height is 1
                  root_height=1
              elif root.left is not None and root.right is None:   #if only has a left child, height is left child's height+1
                  root_height=root.left.height+1
              elif root.right is not None and root.left is None:    #if only has a right child, height is right child's height+1
                  root_height=root.right.height+1
              elif root.right is not None and root.left is not None:     #if two children, height is larger child's height +1
                  if root.right.height > root.left.height:
                      root_height=root.right.height+1
                  elif root.left.height > root.right.height:
                      root_height=root.left.height+1
                  elif root.left.height == root.right.height:
                      root_height= root.left.height+1
              root.height=root_height
              return root
          new_root=root.right         #right node becomes the new root node
          aux_root=None
          if new_root.left is not None:    #if we need to switch the left child of the new root node
              aux_root=new_root.left
              new_root.left=root
              new_root.left.right=aux_root   #rotate and reattatch the new child node
          else:
              new_root.left=root
              new_root.left.right=aux_root
          new_root.left=__get_height(new_root.left)
          new_root=__get_height(new_root)
          return new_root
      if t is None:
          return t
      elif __check_imbalance(t)=="balanced":
          return t
      elif __check_imbalance(t)=="left" and __sub_check_imbalance(t.left)=="left":   #leftleft
          t= __rotate_right(t)
          return t
      elif __check_imbalance(t)=="left" and __sub_check_imbalance(t.left)=="right":  #leftright
          t.left=__rotate_left(t.left)
          t=__rotate_right(t)
          return t
      elif __check_imbalance(t)=="right" and __sub_check_imbalance(t.right) =="left": #rightleft
           t.right=__rotate_right(t.right)
           t=__rotate_left(t)
           return t
      elif __check_imbalance(t)=="right" and __sub_check_imbalance(t.right) =="right": #rightright
          t=__rotate_left(t)
          return t






  def insert_element(self, value):

       def __recursive_ins(val, root):
           if root is None:                                     #base case; if we need to create a new tree
               root = Binary_Search_Tree.__BST_Node(val)
           elif root.value > val:                               #recursive case; if we need recur go left
               root.left = __recursive_ins(val, root.left)
           elif root.value < val:                               #recursive case; if we need to recur right
               root.right = __recursive_ins(val, root.right)
           elif root.value==val:                                #if the val already exists
               raise ValueError                                 #raise an error
           root = self.__get_height(root)
           return self.__balanced(root)
       self.__root=__recursive_ins(value,self.__root)           #recursively return the root node of the newly created tree
       self.__size+=1                                           #update size
       return self.__root


  def __get_height(self, root):           #private method to recursively keep track of the height
      root_height=0
      if root.right is None and root.left is None:          #if a leaf node, height is 1
          root_height=1
      elif root.left is not None and root.right is None:   #if only has a left child, height is left child's height+1
          root_height=root.left.height+1
      elif root.right is not None and root.left is None:    #if only has a right child, height is right child's height+1
          root_height=root.right.height+1
      elif root.right is not None and root.left is not None:     #if two children, height is larger child's height +1
          if root.right.height > root.left.height:
              root_height=root.right.height+1
          elif root.left.height > root.right.height:
              root_height=root.left.height+1
          elif root.left.height == root.right.height:
              root_height= root.left.height+1
      root.height=root_height
      return root                                         #return root in the recursive function with the updated height


  def remove_element(self, value):

      def __find_min(root):              #find the minimum value to replace a removed node with two children
          if root.left is None:   #base case: can't go any more left
              return root
          else:
              return __find_min(root.left)  #recursive case


      def __recursive_remove(val,root):  #recursive removal method
          if root is None:              #if value is not in tree, raise error
              raise ValueError
          elif val==root.value:                 #base case; if we have reached the value we want
              if root.left is None and root.right is None:      #if no children, simply remove
                  root=None
              elif root.left is None and root.right is not None:  #if one child, replace node with that child
                  root=root.right
              elif root.right is None and root.left is not None:
                  root=root.left
              else:                                            #if two children, find minimum of right child and replace that node's vaue with current
                  replacement_node=__find_min(root.right)
                  root.value=replacement_node.value
                  root.right=__recursive_remove(replacement_node.value,root.right)
          elif root.value>val:                       #recursive case; keep searching for val on the left
              root.left=__recursive_remove(val,root.left)
              root=self.__get_height(root)   #update height
          elif root.value<val:                         #recursive case; keep searching for on the right
              root.right=__recursive_remove(val, root.right)
              root=self.__get_height(root)   #update height
          return self.__balanced(root)

      self.__root = __recursive_remove(value,self.__root)
      self.__size-=1        #update size
      return self.__root

  def to_list(self):
      my_list=[]
      def recursive_in_order(list,root):    #private method for inorder traversal
            #initialize list
          if root:           #if the root exists
              recursive_in_order(list,root.left)  #left, root, right
              list.append(root.value)
              recursive_in_order(list,root.right)
          return list   #return list of traversal
      outcome= recursive_in_order(my_list,self.__root)
      return outcome



  def in_order(self):

      def __recursive_in_order(root):    #private method for inorder traversal
          my_list=''        #initialize string
          if root:           #if the root exists
              my_list=my_list + __recursive_in_order(root.left)   #left, root, right
              my_list=my_list + str(root.value)+ ', '
              my_list=my_list + __recursive_in_order(root.right)
          my_list= my_list
          return my_list   #return string of traversal

      if self.__root is None:    #if empty
            outcome = "[ ]"
      elif self.__size == 1:      #if only one node
            outcome = "[ " + str(self.__root.value) + " ]"
      else:                             #concatenate a string of all the values
            outcome= "[ " +str(__recursive_in_order(self.__root))[:-2] + " ]"
      return outcome


  def pre_order(self):

      def __recursive_pre_order(root):  #recursive preorder see in_order(self) for more detailed explanation
          my_list=''
          if root:
              my_list=my_list + str(root.value)+ ', '        #root, left, right
              my_list=my_list + __recursive_pre_order(root.left)
              my_list=my_list + __recursive_pre_order(root.right)
          my_list= my_list
          return my_list

      if self.__root is None:
            outcome = "[ ]"
      elif self.__size == 1:
            outcome = "[ " + str(self.__root.value) + " ]"
      else:
            outcome= "[ " +str(__recursive_pre_order(self.__root))[:-2] + " ]"
      return outcome


  def post_order(self):

      def __recursive_post_order(root): #recursive post order see in_order(self) for more detailed explanation
          my_list=''
          if root:
              my_list=my_list + __recursive_post_order(root.left)  #left, right, root
              my_list=my_list + __recursive_post_order(root.right)
              my_list=my_list + str(root.value)+ ', '
          my_list= my_list
          return my_list

      if self.__root is None:
            outcome = "[ ]"
      elif self.__size == 1:
            outcome = "[ " + str(self.__root.value) + " ]"
      else:
            outcome= "[ " +str(__recursive_post_order(self.__root))[:-2] + " ]"
      return outcome


  def get_height(self):
      if self.__root is None:  #if empty, return 0
          return 0
      else:                    #else return height
          return self.__root.height


  def __str__(self):
      return self.in_order()   #return the contents of the tree in order

  def aux(self):
      def __display_aux(root):
           if root.right is None and root.left is None:
               line = '%s' % root.value
               width = len(line)
               height = 1
               middle = width // 2
               return [line], width, height, middle

           # Only left child.
           elif root.right is None:
               lines, n, p, x = __display_aux(root.left)
               s = '%s' % root.value
               u = len(s)
               first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
               second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
               shifted_lines = [line + u * ' ' for line in lines]
               return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

           # Only right child.
           elif root.left is None:
               lines, n, p, x = __display_aux(root.right)
               s = '%s' % root.value
               u = len(s)
               first_line = s + x * '_' + (n - x) * ' '
               second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
               shifted_lines = [u * ' ' + line for line in lines]
               return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

           # Two children.
           left, n, p, x = __display_aux(root.left)
           right, m, q, y = __display_aux(root.right)
           s = '%s' % root.value
           u = len(s)
           first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
           second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
           if p < q:
               left += [n * ' '] * (q - p)
           elif q < p:
               right += [m * ' '] * (p - q)
           zipped_lines = zip(left, right)
           lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
           return lines, n + m + u, max(p, q) + 2, n + u // 2
      lines, _, _, _ = __display_aux(self.__root)
      for line in lines:
          print(line)



if __name__ == '__main__':
    import random  #for the aux function
    tree=Binary_Search_Tree()
    tree.insert_element(68)
    tree.insert_element(85)
    tree.insert_element(26)
    tree.insert_element(15)
    tree.insert_element(3)
    tree.insert_element(40)
    tree.insert_element(90)
    tree.insert_element(95)
    tree.insert_element(75)
    tree.insert_element(7)

    tree.insert_element(92)
    tree.insert_element(87)
    tree.insert_element(79)

    tree.insert_element(70)
    tree.insert_element(81)
    tree.insert_element(18)
    tree.insert_element(72)
    tree.aux()
    print(tree.to_list())
