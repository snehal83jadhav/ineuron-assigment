#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. How do you distinguish between shutil.copy() and shutil.copytree()?
 shutil.copytree() will copy entire folder like branchers of trees (all files in it)
 whereas shutil.copy() will copy only single folder

get_ipython().set_next_input('2. What function is used to rename files');get_ipython().run_line_magic('pinfo2', 'files')
First import os module then use os.rename() to rename a file.

get_ipython().set_next_input('3. What is the difference between the delete functions in the send2trash and shutil modules');get_ipython().run_line_magic('pinfo', 'modules')
send2trash sends file to recycle bin and shutil module deletes file permanantly.


# In[5]:


#4.ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?
#to open or write to a zipfile we use 'w' as second argument similar to file objects open()
import zipfile as zf
a = zf.ZipFile("abc.zip",'w')
a.close()


# In[3]:


#5. Create a programme that searches a folder tree for files with a certain file extension 
#(such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
import os
import shutil
import os, shutil

def search_and_copy(folder, extensions, destFolder):
    folder = os.path.abspath(folder)
    destFolder = os.path.abspath(destFolder)
    print('searching --> {} for {} file'.format(folder,extensions))
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            name, extension = os.path.splitext(filename)
            if extension in extensions:
                fileAbsPath = foldername + os.path.sep + filename
                print('Coping', fileAbsPath, 'to', destFolder)
                shutil.copy(fileAbsPath, destFolder)

extensions = ['.pdf','.jpg']
folder = 'randomfolder'
destFolder = 'destination'
search_and_copy(folder, extensions, destFolder)


# In[ ]:





# In[ ]:




