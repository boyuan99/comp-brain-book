#!/usr/bin/env python
# coding: utf-8

# # Define Circuits

# The simulation of brain dynamics in <font color=deeppink>Compbrain</font> is implemented in the `Circuit` class, which means that we should enter the neurons and synapses into a circuit after we have defined them

# In[1]:


import compbrain as cb
from compbrain import neurons, synapses, core
import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.layouts import row, column

output_notebook()


# ## Prepare Components

# In[2]:


n1 = neurons.MorrisLecarNeuron('n1')
s1 = synapses.InjectCurrent('s1', "None", 'n1', intensity=5)


# Now we can feed the neuron and the synapse into our circuit.
# 
# <u>_Notice_</u>:
# 
# * The inputs should be **lists** of neurons and synapses

# In[3]:


c1 = core.Circuit([n1], [s1])


# In[4]:


c1.neurons, c1.synapses


# In[5]:


c1.neurons[0].name, c1.synapses[0].name


# In[6]:


c1.neurons[0].states, c1.synapses[0].states


# We haven't executed the simulation yet, so we can see the states of neurons are just their initial values, in the next step, we will learn how to execute the circuit one step forward.

# ## Execute The Circuit One Step Forward

# In[7]:


c1.execute_step()


# In[8]:


c1.neurons[0].states


# From the states of the neuron above, the circuit succeeded in executing one step forward, let's check the synapse:

# In[9]:


c1.synapses[0].states


# The `injected current` synapse has not yet changed, because the above circuit has only been executed one step forward. Let's execute one more step. 

# In[10]:


c1.execute_step()


# In[11]:


c1.synapses[0].states


# ## Execute The Circuit in The Entire Time Series

# We have learned how to execute the circuit one step forward, in <font color=deeppink>Compbrain</font> we also have the function that can help us execute the whole circuit in the entire time series.
# 
# First, we need to define a time array:

# In[12]:


t = np.arange(0, 1, 1e-4)


# Then we should clear the executed outcomes of the above steps

# In[13]:


c1.reset_circuit()


# Now we are ready to execute the whole circuit:

# In[14]:


c1.execute_circuit(t)


# In[15]:


p1 = figure(height=300, title='Neuron V response')
p1.line(t, c1.neurons[0].states['V'], line_color='skyblue', line_width=3)

p2 = figure(height=300, title='N outcome')
p2.line(t, c1.neurons[0].states['N'], line_color='skyblue', line_width=3)

p3 = figure(height=300, title='Current Input')
p3.line(t, c1.synapses[0].states['I_ext'], line_color='orange', line_width=3)

show(column(p1, p2, p3))


# In[ ]:




