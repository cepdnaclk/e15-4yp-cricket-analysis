#!/usr/bin/env python
# coding: utf-8

# In[17]:


from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import numpy as np
import math


# In[18]:


match_data = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/SLP.csv')


# In[19]:


#print the dataset
match_data.head()


# In[20]:


del match_data["Innings ID"]
del match_data["Start Date"]
del match_data["Team"]
del match_data["Day_Night"]
del match_data["Home"]
del match_data["Ground"]
del match_data["Bat"]
del match_data["Toss"]
del match_data["Opposition"]
del match_data["p1"]
del match_data["p2"]
del match_data["p3"]
del match_data["p4"]
del match_data["p5"]
del match_data["p6"]
del match_data["p7"]
del match_data["p8"]
del match_data["p9"]
del match_data["p10"]
del match_data["p11"]


# In[21]:


match_data


# In[22]:


# convert our pandas dataframe into a list of lists,
player_combo = [] #list of lists match players and result
for i in range(0, 6):
    rowItem = []
    for j in range(0, 12):
        rowItem.append(str(match_data.values[i,j]))
    player_combo.append(rowItem)


# In[23]:


print(player_combo)


# In[24]:


#Creating the dataframe of frequent itemsets
te = TransactionEncoder()
te_ary = te.fit(player_combo).transform(player_combo)
match_df_freq = pd.DataFrame(te_ary, columns=te.columns_)


# In[25]:


#Define the minimum support and obtain the itemsets greater than the min support
#support = No. of times the required itemset occured / total no. of matches
match_sup = apriori(match_df_freq, min_support=0.1,use_colnames=True)
print(match_sup)


# In[26]:


#generate association rules
rules= association_rules(match_sup, metric="lift", min_threshold=1)


# In[27]:


#print the association rules
rules


# In[28]:


#remove the one itemsets
#obtain the final winning combinations
rules = rules[(rules['antecedents'].str.len() > 1)] #Here won_rules['antecedents'] is a frozenset


# In[29]:


rules


# In[30]:


#extract only the combinations occured at a winning match
position_won_rules = rules[(rules['consequents'] == {"won"})]


# In[31]:


position_won_rules


# In[32]:


#finding winning combinatios with positions
#removing same player combinations because of different postions
#example: remvove antecedents with [V Kohli3,V Kohli5]
#col_names = ["antecedents","consequents","antecedent support","consequent support","support","confidence","lift","leverage","conviction"]
#position_won_rules = pd.DataFrame(columns = col_names)

#i = 0
#for x in won_rules['antecedents']:
#    itemDup = [] # can have duplicates
#    itemSet = set() #without duplicates
#    for y in x:
#        y[:-1]#remove the last letter from the string
#        itemDup.append(y)
#        itemSet.add(y)
        
#    if len(itemDup) == len(itemSet):
#        position_won_rules = position_won_rules.append({'antecedents':won_rules.values[i,0],"consequents":won_rules.values[i,1],"antecedent support":won_rules.values[i,2],"consequent support":won_rules.values[i,3],"support":won_rules.values[i,4],"confidence":won_rules.values[i,5],"lift":won_rules.values[i,6],"leverage":won_rules.values[i,7],"conviction":won_rules.values[i,8]},ignore_index=True)
#    i = i + 1


# In[33]:


#sorting by confidence --- descending order
position_won_rules.sort_values(by ='confidence', ascending = False, inplace = True)


# In[34]:


position_won_rules


# In[35]:


#For example let's take the first rule
#if JJ Bumrah10, V Kohli3 then won
#112 no of matches have played by the indian team from 2015 to 2020
#here the support is 0.169643 = x/112
#therefore no. of times the antecedent occurs = 0.169643*112 = approx 19 = x
#confidence = 0.904762 = y/19
#No of times the correct rule occured from the 19 instances is = 0.904762*19 = aprox 17


# In[36]:


#sorting by support --- descending order
#position_won_rules.sort_values(by ='support', ascending = False, inplace = True)


# In[37]:


#position_won_rules


# In[38]:


import random
import matplotlib.pyplot as plt

support=position_won_rules['support']
confidence=position_won_rules['confidence']
 
plt.scatter(support, confidence,marker="*")
plt.xlabel('support')
plt.ylabel('confidence') 
plt.show()


# In[39]:


position_won_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SLP_won_rules.csv')


# In[40]:


won_2_rules = won_rules[(won_rules['antecedents'].str.len() == 2)]
won_2_rules


# In[41]:


won_2_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SLP_won2_rules.csv')


# In[42]:


won_3_rules = won_rules[(won_rules['antecedents'].str.len() == 3)]
won_3_rules


# In[43]:


won_3_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SLP_won3_rules.csv')


# In[44]:


won_4_rules = won_rules[(won_rules['antecedents'].str.len() == 4)]
won_4_rules


# In[45]:


won_4_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SLP_won4_rules.csv')


# In[46]:


won_5_rules = won_rules[(won_rules['antecedents'].str.len() == 5)]
won_5_rules


# In[47]:


won_5_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SLP_won5_rules.csv')


# In[48]:


won_6_rules = won_rules[(won_rules['antecedents'].str.len() == 6)]
won_6_rules


# In[49]:


won_6_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SLP_won6_rules.csv')


# In[50]:


won_7_rules = won_rules[(won_rules['antecedents'].str.len() == 7)]
won_7_rules


# In[51]:


won_7_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SLP_won7_rules.csv')


# In[52]:


won_8_rules = won_rules[(won_rules['antecedents'].str.len() == 8)]
won_8_rules


# In[53]:


won_8_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SLP_won8_rules.csv')


# In[54]:


won_9_rules = won_rules[(won_rules['antecedents'].str.len() == 9)]
won_9_rules


# In[55]:


won_9_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SLP_won9_rules.csv')


# In[56]:


won_10_rules = won_rules[(won_rules['antecedents'].str.len() == 10)]
won_10_rules


# In[57]:


won_10_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SLP_won10_rules.csv')


# In[58]:


won_11_rules = won_rules[(won_rules['antecedents'].str.len() == 11)]
won_11_rules


# In[59]:


won_11_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SLP_won11_rules.csv')


# In[ ]:




