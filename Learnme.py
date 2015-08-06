#  tuple () vs list []
#  d = {'x': 1} dictionary ( hash table)
#  d['x'] is 1, dictionary order does not matter.
#  t[:3] start to 3

#  def multiparamfunc(x,y,z):
#      return x + y * z

#  def time(x,y=1, z=1):
#          return x * y - z
#  def factorial(x, check_less_than_zero=True):
#      if check_less_than_zero:
#          if x < 0:
#              raise Exception('ack!')
#      if x == 0:
#          return 1
#      return x * factorial(x-1)

#  pep 8





# print "hello world"
# learnpythonthehardway.org
# pythontutor.com

#  def times2(x):
#    return x * 2
 
#  def myFunc(x):
    

#    x = times2(x)
#    print x
#    myFunc(x)

# myFunc(8)

#  import functions as f 
#  can use f.functionName 

#  factoral 0 is 1

#  def factorial2(n):
#      return n * factorial2(n-1) if n > 0 else 1

#  x = 3

#  def wierd():
#      global x
#      x = x * 10
#      print x

#  def x1(x):
#      return x + 1
#  def x2(x):
#      return x + 2

#  def xmaster(f,x):
#      return f(x)

#  map(f.x1,l)


#   Anonymous function starts with lambda
#   single expression repeatively.

#   functions should be less than 20 lines as 
#   keeping track of a complicated function is hard
#   small functions being called by a master function is better

#  def p(s):
#      print s

#  def r(s):
#      print s,s,s,s

#  def print_alot(s):
#      p(s)
#      r(s)
#      p(s)


# #  Here's why it smells?
# #  codesmell
#  f.times(3,z=2)---


def summation(x):
    if x < 0:
        raise Exception("negative numbers are not allowed")
    # i=0
    # sum=0
    # while i <x:
    #     i += 1
    #     sum += i
       
    return sum (range(x+1))       