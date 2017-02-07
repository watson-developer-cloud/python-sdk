
# coding: utf-8

# In[4]:

import sys
import os
sys.path.append(os.path.join(os.getcwd(),'..'))
import watson_developer_cloud
import watson_developer_cloud.nlu.features.v1 as features


# In[3]:

nlu = watson_developer_cloud.NaturalLanguageUnderstandingV1(version='2016-01-23',
                                                            username='USERNAME',
                                                            url='https://gateway-s.watsonplatform.net/natural-language-understanding/api',
                                                            password='PASSWORD')


# In[6]:

nlu.analyze(text='this is my experimental text.  Bruce Banner is the Hulk and Bruce Wayne is BATMAN! Superman fears not Banner, but Wayne.',
            features=[features.Entities(), features.Keywords()])


# In[ ]:



