#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Create an assert statement that throws an AssertionError if the variable spam is a negative integer.
def check_neg(spam):
    assert spam>0 , "enter positive number"
    
check_neg(-1)


# In[ ]:


#2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the 
#same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the ame, and 'goodbye' 
#and 'GOODbye' are also considered the same).
def assert_stat(eggs, bacon):
    eggs = eggs.lower()
    bacon = bacon.lower()
    assert eggs==bacon, "Enter same words"
    
eggs = "goodbye"
bacon = "GOODbye"
assert_stat(eggs,bacon)
def assert_stat(eggs, bacon):
    
    assert eggs==bacon, "Enter same words and also check the lower and upper case"
    
eggs = "goodbye"
bacon = "GOODbye"
assert_stat(eggs,bacon)


# In[ ]:


#3. Create an assert statement that throws an AssertionError every time.
def always_error():
    assert False, "Assertion statement everytime"


# In[ ]:


always_error()


# In[ ]:


#4. What are the two lines that must be present in your software in order to call logging.debug()?
import logging
logging.basicConfig(filename = 'trial.txt',level = logging.DEBUG, format = '%(asctime)s - %(message)s - %(levelname)s')
logging.debug('Start')
logging.debug('End')


# In[ ]:


#5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a
#file named programLog.txt?


# In[ ]:


logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format='%(message)s - %(asctime)s - %(levelname)s')


# In[ ]:


logging.debug("Snehal test message")


# In[ ]:


logging.debug('This is a test message.')


# In[ ]:


get_ipython().set_next_input('6. What are the five levels of logging');get_ipython().run_line_magic('pinfo', 'logging')
LEVELS OF LOGGING:
                1. Debug
                2. INFO
                3. WARNINGS
                4. ERROR
                5. CRITICAL


# In[ ]:


get_ipython().set_next_input('7. What line of code would you add to your software to disable all logging messages');get_ipython().run_line_magic('pinfo', 'messages')
logging.disable = True


# In[ ]:


get_ipython().set_next_input('8.Why is using logging messages better than using print() to display the same message');get_ipython().run_line_magic('pinfo', 'message')
print is used when you want to display any particular message or help whereas logging is used to record all events like 
error, info, debug messages, timestamps.


# In[ ]:


get_ipython().set_next_input('9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger');get_ipython().run_line_magic('pinfo', 'debugger')
Step Over:
         This button will step over i.e. it will execute that line but result returned without debugging.
Step In:
       This button helps entering debugger and start debugging line by line.
Step Out:
        This breaks out of the debugger.


# In[ ]:


10.After you click Continue, when will the debugger stop ?
This will cause the program to continue running normally, without pausing for debugging  untill it is completed.


# In[ ]:


get_ipython().set_next_input('11. What is the concept of a breakpoint');get_ipython().run_line_magic('pinfo', 'breakpoint')
this will help step line by line through the code.

