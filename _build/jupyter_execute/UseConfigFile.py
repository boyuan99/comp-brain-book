#!/usr/bin/env python
# coding: utf-8

# # Use config File to Form Circuit

# There are times when we need to define complex brain circuits that contain a large number of neurons and synapses, and it would be tedious to declare them all in code. In this case, we can use a config file to define the circuits. This not only facilitates debugging, but also reduces the amount of code

# In[1]:


import numpy as np
import yaml
import compbrain as cb
from compbrain import neurons, synapses
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.layouts import row, column, gridplot

output_notebook()


# ## Neurons Part

# The config part for neurons is shown below.
# 
# <u>_Structure_</u>:
# 
#     neuron model type:
#     
#         neuron name:
#         
#             param1:
#             
#             param2:
#             
#             ...
#             
#             paramn:

# ### Real Example

# In[2]:


with open('neurons_config_template.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)
    config_file.close()
    
print(yaml.dump(config['neurons']))


# ## Synapses Part

# The config part for synapses is shown below.
# 
# <u>_Structure_</u>:
# 
#     synapse model type:
#     
#         synapse name:
#         
#             presynapse name:
#             
#             postsynapse name:
#         
#             params:
#             
#                 param1:
#             
#                 param2:
# 
#                 ...
# 
#                 paramn:

# ### Real Example

# In[3]:


print(yaml.dump(config['synapses']))


# ## Other Parts

# In addition to neurons and synapses, we can also define some remaining parts, such as time series

# ### Real Examples

# In[4]:


print(yaml.dump(config['times']))


# ## Read Config File with Compbrain

# There are built-in methods defined in <font color=deeppink>Compbrain</font> to facilitate the reading of the config file

# In[5]:


neus, syns, t = cb.utils.read_cfg('neurons_config.yaml')


# We have gotten the neurons and synapses and time series defined in the config file, next step is feed them into a brain circuit and execute it to get the responses

# In[6]:


circuit = cb.core.Circuit(neus, syns)
circuit.execute_circuit(t, notebook=True)


# ### Circuit responses

# In[7]:


plots1 = list(range(8))
for i in range(8):
    plots1[i] = figure(height=200, width=240)
    plots1[i].line(t, neus[i].states['V'], line_width=2)
    
grid1 = gridplot([[plots1[0], plots1[1], plots1[2], plots1[3]], [plots1[4], plots1[5], plots1[6], plots1[7]]])
show(grid1)


# In[8]:


plots2 = list(range(12))
for i in range(6, 18):
    plots2[i-6] = figure(height=200, width=240)
    plots2[i-6].line(t, syns[i].states['I_syn'], line_width=2)
    
grid2 = gridplot([[plots2[0], plots2[1], plots2[2], plots2[3]], [plots2[4], plots2[5], plots2[6], plots2[7]], 
                 [plots2[8], plots2[9], plots2[10], plots2[11]]])
show(grid2)


# In[ ]:




