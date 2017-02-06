
# coding: utf-8

# In[1]:

import sys
import os
sys.path.append(os.path.join(os.getcwd(),'..'))
import watson_developer_cloud


# In[2]:

nlu = watson_developer_cloud.NaturalLanguageUnderstandingV1(version='2016-01-23',
                                                            username='<USERNAME>',
                                                            password='<PASSWORD>')


# In[10]:

nlu.analyzeText(text='this is my experimental text.  Bruce Banner is the Hulk and Bruce Wayne is BATMAN! Superman fears not Banner, but Wayne.',features={'entities': {}})


# In[ ]:



