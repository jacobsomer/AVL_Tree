from Binary_Search_Tree import Binary_Search_Tree
class Fraction:

  def __init__(self, numerator, denominator):
    # use caution here... In most languages, it is not a good idea to
    # raise an exception from a constructor. Python is a bit different
    # and it shouldn't cause a problem here.
    if denominator == 0:
      raise ZeroDivisionError
    self.__n = numerator
    self.__d = denominator
    self.__reduce()

  @staticmethod
  def gcd(n, d):
    while d != 0:
      t = d
      d = n % d
      n = t
    return n

  def __reduce(self):
    if self.__n < 0 and self.__d < 0:
      self.__n = self.__n * -1
      self.__d = self.__d * -1

    divisor = Fraction.gcd(self.__n, self.__d)
    self.__n = self.__n // divisor
    self.__d = self.__d // divisor

  def __add__(self, addend):
    num = self.__n * addend.__d + self.__d * addend.__n
    den = self.__d * addend.__d
    return Fraction(num, den)

  def __sub__(self, subtrahend):
    num = self.__n * subtrahend.__d - self.__d * subtrahend.__n
    den = self.__d * subtrahend.__d
    return Fraction(num, den)

  def __mul__(self, multiplicand):
    num = self.__n * multiplicand.__n
    den = self.__d * multiplicand.__d
    return Fraction(num, den)

  def __truediv__(self, divisor):
    if divisor.__n == 0:
      raise ZeroDivisionError
    num = self.__n * divisor.__d
    den = self.__d * divisor.__n
    return Fraction(num, den)

  def __lt__(self, other):
      if self.__n/self.__d<other.__n/other.__d:
          return True
      else:
          return False
    #TODO replace pass with your implementation,
    #returning True if self is less than other and
    #False otherwise.

  def __gt__(self, other):
      if self.__n/self.__d>other.__n/other.__d:
          return True
      else:
          return False
    #TODO replace pass with your implementation,
    #returning True if self is greater than other and
    #False otherwise.

  def __eq__(self, other):
      if self.__n/self.__d==other.__n/other.__d:
          return True
      else:
          return False
    #TODO replace pass with your implementation,
    #returning True if self equal to other and
    #False otherwise. Note that fractions are
    #stored in reduced form.

  def to_float(self):
    #this is safe because we don't allow a
    #zero denominator
    return self.__n / self.__d

  def __str__(self):
    return str(self.__n) + '/' + str(self.__d)

  # the __repr__ method is similar to __str__, but is called
  # when Python wants to display these objects in a container like
  # a Python list.
  def __repr__(self):
    return str(self)

if __name__ == '__main__':
    f1=Fraction(1,2)
    f2=Fraction(75,23)
    f3=Fraction(34,4)
    f4=Fraction(314,34)
    f5=Fraction(3,4)
    f6=Fraction(2,7)
    f7=Fraction(400,3)
    f8=Fraction(21,2)
    f9=Fraction(23,57)
    f10=Fraction(34,345)
    list=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]
    tree=Binary_Search_Tree()
    for item in list:
        tree.insert_element(item)
    print(tree.to_list())
    tree.aux()



  #TODO create a bunch of fraction objects and store them in an array.
  #Then insert each item from the array into a balanced BST.
  #Then get the in-order array representation of the BST using
  #the new to_list() method, which you must implement.
  #print the original and in-order traversal arrays to show that
  #the fractions have been sorted.
