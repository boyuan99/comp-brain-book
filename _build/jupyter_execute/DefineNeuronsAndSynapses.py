#!/usr/bin/env python
# coding: utf-8

# # Define Neurons and Synapses

# One of the most essential approaches to studying brain dynamics is building a dynamic model and doing simulation. In this example, we will define a neuron and a synapse, which are crucial components in a brain circuit.

# In[1]:


import compbrain as cb
from compbrain import neurons, synapses
import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_notebook

output_notebook()


# ## Define a Neuron

# We can simply define a neuron by its biological neuron model. The following neuron is a [Morris-Lecar](https://en.wikipedia.org/wiki/Morris%E2%80%93Lecar_model) model. Remember, in <font color=deeppink>Compbrain</font> we need to give each neuron a unique name(in one single circuit).

# In[2]:


n1 = neurons.MorrisLecarNeuron('n1')


# If we don't give the neuron a specific set of parameters, the model will use the default parameters. The neuron has the following attributes:

# In[3]:


n1.__dict__


# We can specify parameters as follow:

# In[4]:


n1 = neurons.MorrisLecarNeuron('n1', params=dict(V_1=-15.0, 
                                                 V_2=2.0, 
                                                 V_3=-45.0, 
                                                 V_4=0.8,
                                                 phi=0.0005, 
                                                 C=1, 
                                                 dt=1e-4, 
                                                 offset=60,
                                                 E_L=-50.0, 
                                                 E_Ca=120.0,
                                                 E_K=-75.0,
                                                 g_L=0.1,
                                                 g_Ca=2.0, 
                                                 g_K=7.0,))


# Or just specify the parameters we want to change from the default:

# In[5]:


n1 = neurons.MorrisLecarNeuron('n1', params=dict(V_1=-15.0, 
                                                 phi=0.0004))


# We can see the difference from before the modification

# In[6]:


n1.params


# ## Define a synapse

# We can define a synapse as above with different models. Also, the synapses' names should be unique. But unlike the neuron models, when instantiating a synaptic object we have to specify both the presynaptic and postsynaptic neurons. (Usually a synapse will only have no presynaptic neurons, such as `injected current`, but no postsynaptic neurons, in which case we can leave the subsequent synapses undefined for that neuron)
# 
# 
# In the following example, we will define a `injected current` synapse.
# 
# <u>*Notice*</u>: 
# 
# * In <font color=deeppink>Compbrain</font> all of the injection currents will be presented as `inject current` synapses.
# 
# * Both presynaptic neuron and postsynaptic neuron inputs should be `String`!
# 
# * Only one presynaptic neuron and one postsynaptic neuron can be declared in a synapse, however, you can define multiple synapses between neurons.

# In[7]:


s1 = synapses.InjectCurrent('s1', 'None', 'n1')


# In[8]:


s1.__dict__


# If we don't give any specific type of input current, the default current will look like:

# In[9]:


p = figure(height=300, title='Default injected current')
p.line(s1.t, s1.current, line_color='skyblue', line_width=3)
show(p)


# We can give a specific input intensity:

# In[10]:


s1 = synapses.InjectCurrent('s1', None, n1, intensity=10)


# In[11]:


p = figure(height=300, title='Default injected current')
p.line(s1.t, s1.current, line_color='skyblue', line_width=3)
show(p)


# If you want to set more complex inputs, you can do so in the configuration

# In[ ]:




