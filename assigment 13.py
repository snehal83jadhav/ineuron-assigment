#!/usr/bin/env python
# coding: utf-8

# # Q.1. Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated
# sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

# In[2]:


D = [int(i) for i in input("Enter values:\n").split(',')]
C = 50
H = 30
E = []
for j in range(0,len(D)):
    Q = ((2*C*D[j])/H)**0.5
    E.append(Q)
print("Output:")
for k in range(0,len(E)):
    print(int(E[k]), end = ",")


# # Question 2:Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
# element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# In[4]:


x = int(input("Enter no of rows: "))
y = int(input("Enter no of columns: "))
mat = []
for i in range(x):
    row = []
    for j in range(y):
        row.append(i*j)
    mat.append(row)
    print(row)
print(mat)


# # Question 3:Write a program that accepts a comma separated sequence of words as input and prints thewords in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

# In[5]:


strings = [str(i) for i in input("Enter values:\n").split(',')]
strings.sort()
for k in strings:
    print(k, end = ",")


# # Question 4:Write a program that accepts a sequence of whitespace separated words as input and printsthe words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# In[6]:


words = [str(i) for i in input("Enter words:\n").split(' ')]
words.sort()
c = []
for k in words:
    c.append(k)
#print(c)
alphanum = []
for i in c:
    if i not in alphanum:
        alphanum.append(i)
print()
print("Alphanumerically sorted words are as follows:")
for j in alphanum:
    print(j,end = " ")


# # Question 5:Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# In[1]:


sentence = str(input("Enter sentense: "))
letters = 0
digits = 0

for i in sentence:
    if i.isalpha():
        letters = letters+1
    elif i.isdigit():
        digits = digits+1
    else:
        pass
     
print("LETTERS {} \n DIGITS {}".format(letters,digits))


# # Question 6:
# A website requires the users to input username and password to register. Write a program to
# check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them
# according to the above criteria. Passwords that match the criteria are to be printed, each
# separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

# In[1]:


passwords = [str(i) for i in input("Enter passwords:\n").split(",")]
spl_char = ["$","#","@"]
correctpass = []
for i in passwords:
    if (len(i)<6 or len(i)>12):
        continue
    if (i.isupper() or i.islower()):
        continue
    num = any(j.isdigit() for j in i)
    if (not num):
        continue
    spl = any(j in spl_char for j in i)
    if (not spl):
        continue
    
    correctpass.append(i)
print()
print("Correct password is: ")
for k in correctpass:
    print(k,end = " ")


# In[ ]:




