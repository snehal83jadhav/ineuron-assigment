#!/usr/bin/env python
# coding: utf-8

# In[1]:



#1. Assign the value 7 to the variable guess_me. Then, write the conditional tests (if, else, and elif) to print the string 'too low' if guess_me is less than 7, 'too high' if greater than 7, and 'just right' if equal to 7.
def guess_me(guess_me):
    if guess_me < 7:
        print('too Low')
    elif guess_me > 7:
        print('too High')
    else:
        print('just Right')

guess_me(guess_me=7)
guess_me(guess_me=5)
guess_me(guess_me=15)


# In[2]:



#2. Assign the value 7 to the variable guess_me and the value 1 to the variable start. Write a while loop that compares start with guess_me. Print too low if start is less than guess me. If start equals guess_me, print 'found it!' and exit the loop. If start is greater than guess_me, print 'oops' and exit the loop. Increment start at the end of the loop

guess_me = 7
start = 1
while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it')
        break
    else:
        print('oops')
        break
    start += 1


# In[ ]:


3. Print the following values of the list [3, 2, 1, 0] using a for loop.


# In[5]:


list=[3,2,1,0]
for i in list:
    print(i)


# In[6]:



#4. Use a list comprehension to make a list of the even numbers in range(10)

print([x for x in range(10+1) if x%2==0 ])


# In[7]:



#5. Use a dictionary comprehension to create the dictionary squares. 
#Use range(10) to return the keys, and use the square of each key as its value.

# Method 1
print(dict([(x,pow(x,2)) for x in range(10)]))
# Method 2
print({x:x**2 for x in range(10)})


# In[8]:



#6. Construct the set odd from the odd numbers in the range using a set comprehension (10).

print({x for x in range(10) if x%2 !=0})


# In[9]:


#7. Use a generator comprehension to return the string 'Got ' and a number for the numbers in range(10). 
#Iterate through this by using a for loop

gen_com = ('Got_'+str(x) for x in range(10))
for ele in gen_com:
    print(ele)


# In[13]:


#8. Define a function called good that returns the list ['Harry', 'Ron', 'Hermione'].
def good():
    x=['Harry', 'Ron', 'Hermione']
    return x
print(good())


# In[14]:



#10. Define an exception called OopsException. Raise this exception to see what happens. Then write the code to catch this exception and print 'Caught an oops'.

class OopsException(Exception):
    pass

def test(input):
    if input <0:
        raise OopsException(a)
try:
    test(-100)
except Exception as e:
    print('Caught in Oops ->',e)


# In[15]:



#11. Use zip() to make a dictionary called movies that pairs these lists: titles = ['Creature of Habit', 'Crewel Fate'] and plots = ['A nun turns into a monster', 'A haunted yarn shop'].

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
output = dict(zip(titles,plots))
print(output)


# In[ ]:




