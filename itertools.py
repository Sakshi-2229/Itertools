# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 09:17:35 2023

@author: DELL
"""

lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

#we can write same method using list comprehension
lst=[num for num in range(0,20)]
print(lst)


names=['dada','mama','kaka']
lst1=[name.capitalize() for name in names]
print(lst1)

#list comprehension with if statment
def is_even(num):
    return num%2==0
lst=[
     num
     for num in range(10)
     if is_even(num)
     
     ]
print(lst)

#To create multiple digit number
lst=[f"{x}{y}"
     for x in range(3)
     for y in range(3)
    
    ]
print(lst)

#set comprehension
lst={
     x
     for x in range(3)
     }
print(lst)

#dictionaries comprehension
dict={x:x*x
      for x in range(3)
      
      }
print(dict)


#Generator 
#It is another way of creating iterators
#in a asimple way where
#it uses the keyword "yeild"
#instead of returning it is defined function
#Generators are implemented using a function
gen=(x
     for x in range(3)
     )
print(gen)
for num in gen:
    print(num)
 
    
#next() to access the values one by one
gen=(x
     for x in range(3)
     )
next(gen)

gen=(x for x in range(3))
next(gen)
next(gen)

#Function which will return multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)
    
#now instead of using for loop we can write next
gen=range_even(6)
next(gen)
next(gen)

#Chainingg Generators
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
    
passwords=["not-good","give'm-pass","00100=100"]
for password in hide(lengths(passwords)):
    print(password)
    
#Printing list with index
lst=["Milk","Egg","Bread"]
for index in range(len(lst)):
    print(f"{index+1} {lst[index]}")
    
#same code can be implemented using enumerate
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")
    
#use of zip function
name=['dada','mama','kaka']
info=[2222,3333,4444]
for nm,inf in zip(name,info):
    print(nm,inf)
    
#Use of zip function with mis match list
name=['dada','mama','kaka','baba']
info=[2222,3333,4444]
for nm,inf in zip(name,info):
    print(nm,inf)
    
#zip_longest
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[2222,3333,4444]
for nm,inf in zip_longest(name,info):
    print(nm,inf)
#use of fill value instead of None    
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[2222,3333,4444]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)
    
#use of all(),if all the values are true
lst=[2,3,6,8,9]
if all(lst):
    print("all values are true")
else:
    print("useless")
    
lst=[2,3,6,0,8,9]
if all(lst):
    print("all values are true")
else:
    print("useless")
    #there should not be null values