
# coding: utf-8

# In[338]:


import requests
import pandas as pd
import json
import yaml
from datetime import date


# In[292]:


with open("EPI_SERVER.yaml", 'r') as stream:
    try:
        env_vars = pd.DataFrame(yaml.safe_load(stream))
        print(env_vars)
    except yaml.YAMLError as exc:
        print(exc)


# In[297]:


password = env_vars.iloc[0, 0]
username = env_vars.iloc[1, 0]


# In[369]:


req_url = 'https://api.campaign.episerver.net/rest/252186639077/recipients/252186639082/count'
r = requests.get(req_url , 
                 auth=(username, password))

req_df = pd.DataFrame(r.json())
count = req_df["count"][0]
today = date.today().strftime("%d/%m/%Y")


# In[407]:


master_df = pd.DataFrame(columns = ["date", "count"])


# In[408]:


append_df = pd.DataFrame({"date": [today], "count": [count]})


# In[418]:


master_df = master_df.append(append_df)


# In[419]:


print(master_df)

