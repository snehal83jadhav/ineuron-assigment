#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Write a Python program to Extract Unique values dictionary values?
d = {'511':'Vishnu','512':'Vishnu','513':'Ram','514':'Ram','515':'sita'}
l = []
for val in d.values():
    if val in l:
        continue
    else:
        l.append(val)
        
print(l)  


# In[2]:


#2. Write a Python program to find the sum of all items in a dictionary?
d = {'a':[200,101],'b':[202,103],'c':[204,105]}
l = []
for i in d.values():
    for j in i:
        l.append(j)
print(sum(l))
        


# In[3]:


#3. Write a Python program to Merging two Dictionaries?
d1 = {'a':100,'b':200,'c':300}
d2 = {'d':400,'e':500,'f':600}
d2.update(d1)
d2


# In[4]:


#4. Write a Python program to convert key-values list to flat dictionary?
l = ['a',100,'b',200,'c',300,'d',400,'e',500,'f',600]
l1= []
l2= []
for i in range(0,len(l),2):
    l1.append(l[i])

for j in range(1,len(l),2):
    if j not in l1:
        l2.append(l[j])
#print(l1)
#print(l2)

d = dict(zip(l1,l2))
print("List {} to \n Dictionary {}".format(l,d))


# In[6]:


#5. Write a Python program to insertion at the beginning in OrderedDict?
from collections import OrderedDict


# In[7]:


d = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500, 'f': 600}
od = OrderedDict(d)
print(od)
od['g'] = 700
print(od)
od.move_to_end('g', False)
print(od)


# In[8]:


#6. Write a Python program to check order of character in string using OrderedDict()?
unordered = {'a': 1000, 'f': 200, 'd': 300, 'c': 400, 'b': 500, 'e': 600}
print(unordered)
od = OrderedDict(sorted(unordered.items()))
print(od)


# In[9]:


#7. Write a Python program to sort Python Dictionaries by Key or Value?
d = {'a': 1000, 'f': 200, 'd': 300, 'c': 400, 'b': 500, 'e': 600}
sort = sorted(d.items())

print("Sorted by key: ",sort)


# In[ ]:




