


"""

- why FP ?

    ==> makes code is compact & concise
 
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# imperative style  ( what + how )

"""
evens = []
for number in numbers:
    if number%2 == 0:
        evens.append(number)

print(evens)

odds = []
for number in numbers:
    if number%2 != 0:
        odds.append(number)

print(odds)



greater_than_five = []
for number in numbers:
    if number > 5:
        greater_than_five.append(number)

print(greater_than_five)

"""

# --------------------------------------------------
"""
def filter(inp_list,f):
    out_list=[]
    for number in  inp_list:
        if f(number):
            out_list.append(number)

    return out_list;


# declarative => ( what )   a.k.a Functional Programming
evens=filter(numbers,lambda number: number%2 == 0)
print(evens)

odds=filter(numbers,lambda number: number%2 != 0)
print(odds)

greater_than_five=filter(numbers,lambda number: number> 5)
print(greater_than_five)

"""

"""

Functional Programming Concepts
    
    - Pure Functions
    - Higher Order Functions
    - Immutability

"""

# what  is pure-function ?

# a function which is not changing out-side world

# advantages of pure function :

# - for same input , we always same results
# - will not surprise users
# - easy to test
# - easy to distribute the execution on multiple cores & computers ( phase- 4 , data sceince )

"""
import math

print(math.sqrt(2))
print(math.sqrt(2))

import random;

print(random.randint(1,100))

"""
"""
global_var=1

def  do_something(inp):
      # global  global_var
      # global_var += 10   # side-effect with global
      result=global_var + inp;
      return  result;

print(do_something(10))
print(do_something(10))
print(do_something(10))
print(do_something(20))

"""


"""

    - Higher Order Functions ( HOF )
    
     by function composition, 
     with smaller function(s) we can build complex functions

"""

def log():
    print("logging...")
def sec():
    print("sec...")
def computation():
    print("computation..")
def wrap_log(f):
    def new_f():
        log();
        f();
    return new_f
def wrap_sec(f):
    def new_f():
        sec();
        f();
    return new_f
comp_with_log=wrap_log(computation)
comp_with_log_with_sec=wrap_sec(comp_with_log)
comp_with_log_with_sec()


"""
- Immutability
    => to make change , create new
"""

