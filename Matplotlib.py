
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
#This allows me to see the plots inside the jupyter notebook


# In[4]:


#if i wasn't using jupyter notebook i would add .show() at the end of my commands


# In[5]:


import numpy as np
x = np.linspace(0,5,11)
y = x **2


# In[6]:


x


# In[7]:


y


# In[8]:


plt.plot(x,y)
# i would put plt.show() here to print the plot if i wasn't in jupyter notebook


# In[9]:


plt.plot(x,y,'r')


# In[10]:


plt.plot(x,y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')


# In[11]:


plt.subplot(1,2,1)
plt.plot(x,y, 'r')

plt.subplot(1,2,2)
plt.plot(y,x, 'b')


# In[12]:


# switching gears to the object orriented method


# In[13]:


fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')


# In[14]:


fig = plt.figure()

axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3]) 
#all of these axes must be between 0 and 1 and it is a percentage
axes1.plot(x,y)
axes2.plot(y,x,'r')
axes1.set_title('Bigger plot')
axes2.set_title('Smaller plot')


# In[15]:


fig,axes = plt.subplots(nrows=3, ncols=2)
plt.tight_layout() 
#the second call keeps the plots from overlapping 


# In[16]:


fig,axes = plt.subplots(nrows=1, ncols=2)

for current_ax in axes:
    current_ax.plot(x,y)


# In[17]:


fig,axes = plt.subplots(nrows=1, ncols=2)

axes[0].plot(x,y)
axes[0].set_title('First Plot')
axes[1].plot(y,x)
axes[1].set_title('Second Plot')


# In[18]:


#next up if figure size and dpi


# In[19]:


fig = plt.figure(figsize=(3,2),dpi=100)
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)


# In[20]:


fig = plt.figure(figsize=(8,2),dpi=100)
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)


# In[36]:


fig = plt.figure(figsize=(8,2))
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2,label='x squared')
ax.plot(x,x**3,label='x cubed')

ax.legend(loc=0)
#ax.legend looks for any labels and puts it on the gaph 
#loc tells where the legend should go, 0 will put the legend in the optimal location


# In[23]:


fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8,2))
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()


# In[24]:


fig


# In[27]:


fig.savefig('my_picture.png', dpi=200)


# In[28]:


#it supports many file types such as png and jpeg


# In[37]:


#part 3 below


# In[59]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y, color='orange', linewidth=5, alpha=0.5, marker='o', markersize=20,
       markerfacecolor='blue', markeredgewidth=3) 
#linewidth can also be used as lw
#alpha affects transparency 
#linestyle or ls lets you add line types such as dash or stpes etc.

ax.set_xlim([0,3])
ax.set_ylim([0,12.5])


# In[60]:


plt.scatter(x,y)


# In[62]:


from random import sample 
data = sample(range(1,1000), 100)
plt.hist(data)

