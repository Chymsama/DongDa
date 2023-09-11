#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import re


# In[9]:


data_path ="D:\codegym3\\"
data_name = "house_price_Dống-Da_Hà-Nội_subdata.csv"

df= pd.read_csv(data_path+data_name)
df.head()


# In[7]:


df.shape


# In[8]:


df.dtypes


# Lọc ra các bản ghi bán nhà riêng tại phường Trung liệt hoặc phường Khâm Thiên

# không có cột ward_name

# Lọc các thông tin Địa chỉ, Giá, Hướng nhà, Hướng ban công của các bản ghi có giấy chứng nhận sổ đỏ và có 3 phòng ngủ trở lên.

# In[11]:


cau3 = (df['land_certificate']=='So do')& (df['bedroom']>=3)

df.loc[cau3,['price','house_direction','balcony_direction']]


# Với mỗi loại nhà đất, tính trung bình cộng giá cũng như giá lớn nhất và giá nhỏ nhất.

# In[14]:


x = df.groupby('property_type')['price'].agg(['mean','max','min'])

x.columns=['Trung bình giá', 'Giá lớn nhất', 'Giá nhỏ nhất']
print(x)


# Tính trung bình cộng số phòng ngủ, số phòng vệ sinh, số tầng của mỗi phường.

# In[ ]:


không có cột ward_name

