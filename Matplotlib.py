#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install matplotlib')


# In[4]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


import numpy as np


# In[6]:


x = np.arange(0,10)


# In[7]:


y = np.arange(11,21)


# In[8]:


x


# In[9]:


y


# In[31]:


plt.scatter(x,y,c="r")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("graph in 2D")
plt.savefig("test.png")


# In[29]:


y = x*x


# In[13]:


y


# In[14]:


x


# In[24]:


plt.plot(x,y ,c ='r')


# In[70]:


plt.plot(x,y,'b*',linestyle = "dashed",linewidth = 2,markersize = "10")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("2d diagram")


# In[77]:


plt.subplot(2,2,1)
plt.plot(x,y,"r--")
plt.xlabel("X axis")
plt.ylabel( "Y axis")

plt.subplot(2,2,2)
plt.plot(x,y,"b--")
plt.xlabel("X axis")
plt.ylabel ( "Y axis")

plt.subplot(2,2,3)
plt.plot(x,y,"g--")
plt.xlabel("X axis")
plt.ylabel( "Y axis")

plt.subplot(2,2,4)
plt.plot(x,y,"y--")
plt.xlabel("X axis")
plt.ylabel( "Y axis")


# In[88]:


x1 = [1,2,3,4,5]
y1 = [11,12,13,14,15]

x2 = [3,14,15,16]
y2 = [4,6,12,15]
plt.bar(x1,y1,color = "g")
plt.bar(x2,y2,)


# In[91]:


a = np.array([12,23,26,15,32,31,37,3,32,42,42,12,25,41,36,56,51])
plt.hist(a)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




