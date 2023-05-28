#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Question 1:Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given
    range 0 and n.


# In[1]:


class itrate:
    def __init__(self,n):
        self.n  = n
    
    def divisible(self):
        for i in range(0, self.n):
            if i%7==0 and i>0:
                print(i)


# In[2]:


a = itrate(100)
a.divisible()


# In[ ]:


Question 2: Write a program to compute the frequency of the words from the input. The outputshould output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or
Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1


# In[3]:


input_string = str(input("Enter the string: ")).split()
frequency_check = sorted(set(input_string))

for i in frequency_check:
    print("{}:{}".format(i,input_string.count(i)))


# In[ ]:


Question 3: Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" 
        which can print "Male" for Male class and "Female" for Female class.


# In[6]:


class person:
    def getgender(self):
        pass

class male(person):
    def getgender(self):
        return "male"

class female(person):
    def getgender(self):
        return "female"
    
m = male()
print(m.getgender())
f = female()
print(f.getgender())


# In[ ]:


Question 4: Please write a program to generate all sentences where subject is in ["I", "You"] and 
    verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].


# In[7]:


subject = ["I", "You"]
verb = ["Play", "Love"]
objects = ["Hockey","Football"]

for i in subject:
    for j in verb:
        for k in objects:
            print("{} {} {}".format(i,j,k))


# In[ ]:


Question 5: Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".


# In[9]:


import zlib


# In[13]:


s= 'hello world!hello world!hello world!hello world!'.encode()
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))


# In[ ]:


Question 6: Please write a binary search function which searches an item in a sorted list. 
    The function should return the index of element to be searched in the list.


# In[14]:


def binary_search(l,n):
    low = 0
    high = len(l)-1

    
    while low<=high:
        mid = (low+high)//2
        
        if l[mid]<n:
            low = mid+1
        elif l[mid]>n:
            high = mid-1
        else:
            return mid
    return "element not in list"


# In[15]:


l = [12,4,2,31,21]
l.sort()
print(l)
binary_search(l,2)


# In[16]:


binary_search(l,5)


# In[ ]:




