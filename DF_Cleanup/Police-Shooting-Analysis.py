#!/usr/bin/env python
# coding: utf-8

# In[82]:


import pandas as pd
import numpy as np


# In[83]:


DataSet1 = "datasets_2647_4395_PoliceKillingsUS.csv"
DataSet1 = pd.read_csv(DataSet1)

#Rename all DataSet1 columns to match Dataset2
Renamed_DataSet1 = DataSet1.rename(columns={"city":"City","state":"State","name":"Victim's name",
                                   "age":"Victim's age", "gender":"Victim's gender","race":"Victim's race", "signs_of_mental_illness":"Symptoms of mental illness?","armed":"Unarmed", "manner_of_death": "Cause of death", "threat_level": "Alleged Threat Level (Source: WaPo)", "flee": "Fleeing (Source: WaPo)","body_camera": "Body Camera (Source: WaPo)", "date":"Date of Incident (month/day/year)"})
Renamed_DataSet1


# In[84]:


Renamed_DataSet1.info()


# In[85]:


#Read in Dataset2
DataSet2 = "police_killings_new.csv"
DataSet2 = pd.read_csv(DataSet2)
DataSet2


# In[86]:


DataSet2.info()


# In[87]:


#Change "Unknown" age to NaN
DataSet2.loc[DataSet2["Victim's age"]=="Unknown", "Victim's age"] = np.nan


# In[88]:


#Change "40s" age to 40
DataSet2.loc[DataSet2["Victim's age"]=="40s", "Victim's age"] = 40


# In[89]:


#Transfor data type to float to match DataSet1 data type
DataSet2["Victim's age"]=DataSet2["Victim's age"].astype(float)


# In[90]:


#Concatenate the 2 Datasets
concat_df = pd.concat([Renamed_DataSet1, DataSet2 ], sort=False)
concat_df


# In[91]:


#Drop strange colums at the end of Df
concat_df = concat_df.drop(columns=concat_df.columns[29:])


# In[92]:


#check columns and data types
concat_df.info()


# In[93]:


#Drop unused columns
concat_df = concat_df.drop(columns=["WaPo ID (If included in WaPo database)", "URL of image of victim", "Off-Duty Killing?","Geography (via Trulia methodology based on zipcode population density: http://jedkolko.com/wp-content/uploads/2015/05/full-ZCTA-urban-suburban-rural-classification.xlsx )", "Link to news article or photo of official document" ])


# In[94]:


#Remove duplicates based on Name, City, and State
concat_df = concat_df.drop_duplicates(subset = ["Victim's name","City", "State"])


# In[95]:


concat_df.info()


# In[96]:


#Rename final columns for consistency to enter in DB
New_df = concat_df.rename(columns={"id":"ID", "Victim's name": "Name", "Victim's age": "Age", "Cause of death": "Death_cause", "Unarmed": "Armed", "Victim's gender": "Gender", "Victim's race": "Race", "Symptoms of mental illness?": "Mental_illness", "Alleged Threat Level (Source: WaPo)": "Threat_level", "Fleeing (Source: WaPo)": "Fleeing", "Body Camera (Source: WaPo)": "Body_camera", "Date of Incident (month/day/year)": "Date", "Street Address of Incident": "Address", "Agency responsible for death": "Agency", "A brief description of the circumstances surrounding the death": "Description", "Official disposition of death (justified or other)": "Disposition_of_death", "Criminal Charges?": "Criminal_charges", "Alleged Weapon (Source: WaPo)": "Alleged_weapon"})             


# In[97]:


#Check new column names
New_df.info()


# In[98]:


#Normalize the data en columns. Homogeneous data


# In[99]:


#Cleanup Mental Illness column
New_df["Mental_illness"].value_counts()


# In[100]:


#Change "True" values to "Yes" for normalization, etc
New_df.loc[New_df["Mental_illness"]==True, "Mental_illness"] = "Yes"


# In[101]:


New_df.loc[New_df["Mental_illness"]==False, "Mental_illness"] = "No"


# In[102]:


New_df.loc[New_df["Mental_illness"]=="unknown", "Mental_illness"] = "Unknown"


# In[103]:


New_df.loc[New_df["Mental_illness"]=="Unknown ", "Mental_illness"] = "Unknown"


# In[104]:


#Cleanup Fleeing column
New_df["Fleeing"].value_counts()


# In[105]:


New_df.loc[New_df["Fleeing"]=="car", "Fleeing"] = "Car"


# In[106]:


New_df.loc[New_df["Fleeing"]=="foot", "Fleeing"] = "Foot"


# In[107]:


New_df.loc[New_df["Fleeing"]=="0", "Fleeing"] = "Other"


# In[108]:


New_df.loc[New_df["Fleeing"]=="not fleeing", "Fleeing"] = "Not fleeing"


# In[109]:


#Clean up Threat Level column. Looks good
New_df["Threat_level"].value_counts()


# In[110]:


#Armed -- How to proceed? It has too many categories
New_df["Armed"].value_counts()


# In[111]:


New_df["Age"].value_counts()


# In[144]:


New_df["Race"].value_counts()


# In[156]:


New_df.loc[New_df["Race"]=="W", "Race"] = "White"


# In[157]:


New_df.loc[New_df["Race"]=="B", "Race"] = "Black"


# In[158]:


New_df.loc[New_df["Race"]=="H", "Race"] = "Hispanic"


# In[159]:


New_df.loc[New_df["Race"]=="A", "Race"] = "Asian"


# In[160]:


New_df.loc[New_df["Race"]=="N", "Race"] = "Native American"


# In[161]:


New_df.loc[New_df["Race"]=="O", "Race"] = "Unknown race"


# In[162]:


New_df.loc[New_df["Race"]=="Unknown Race", "Race"] = "Unknown race"


# In[163]:


New_df["Race"].value_counts()


# In[154]:


New_df["Gender"].value_counts()


# In[152]:


New_df.loc[New_df["Gender"]=="M", "Gender"] = "Male"


# In[153]:


New_df.loc[New_df["Gender"]=="F", "Gender"] = "Female"


# In[123]:


New_df = concat_df.drop(columns=["Unnamed: 27", "id", "ID"])


# In[164]:


New_df["Gender"].value_counts()


# In[124]:


# #Rename final columns for consistency to enter in DB
# New_df = concat_df.rename(columns={"id":"ID", "Victim's name": "Name", "Victim's age": "Age", "Cause of death": "Death_cause", "Unarmed": "Armed", "Victim's gender": "Gender", "Victim's race": "Race", "Symptoms of mental illness?": "Mental_illness", "Alleged Threat Level (Source: WaPo)": "Threat_level", "Fleeing (Source: WaPo)": "Fleeing", "Body Camera (Source: WaPo)": "Body_camera", "Date of Incident (month/day/year)": "Date", "Street Address of Incident": "Address", "Agency responsible for death": "Agency", "A brief description of the circumstances surrounding the death": "Description", "Official disposition of death (justified or other)": "Disposition_of_death", "Criminal Charges?": "Criminal_charges", "Alleged Weapon (Source: WaPo)": "Alleged_weapon"})             


# In[125]:


New_df
#how to manage the NaNs?


# In[126]:


New_df.info()


# In[127]:


from sqlalchemy import create_engine
# import pymysql
from sqlalchemy import Column, Integer, String, Float


# In[146]:


engine = create_engine('postgresql://postgres:Bg2094695@localhost:5432/PoliceShootings')
# Base.metadata.create_all(engine)
New_df.to_sql('shootings', engine, if_exists='replace')


# In[147]:


engine.execute("SELECT * FROM shootings").fetchall()


# In[148]:


data = pd.read_sql('SELECT "ID" FROM "Shootings"', con=engine)
data.head()


# In[149]:


engine.execute('SELECT AVG("Age") FROM shootings').fetchall()


# In[167]:


engine.execute('SELECT "Race", COUNT("Race") FROM shootings GROUP BY "Race"').fetchall()


# In[ ]:




