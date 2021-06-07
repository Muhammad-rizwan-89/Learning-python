#!/usr/bin/env python
# coding: utf-8

# In[36]:


# learning List

list_1 = ["a",'b','c','d','e','f']

print(list_1)
print(list_1[2])
print(list_1[2:3])
print([-1])

# how to add  a value in the list

list_1.append('new')
print(list_1)

# how to add a value to a perticular index of a list

list_1[0] = "Mustafa"
print(list_1)

# how to delete a value in the list

del list_1[:3]
print(list_1)

# how to mearge 2 list and create a 3 list contaning all the values of both the list
print(list_1)
print(list_2)
list_2 = [1,2,3,4,5,6]

list_3 = list_1 + list_2

print(list_3)

# how to use multiply operator in a list

multi_list = [1,2,3,4,5]
print(multi_list * 3)

# how to know the length of the List
randomeList = [12,12,4,23,23,23,3,214,12,3123,134,13,312,312,3]
randomeList1= [12,12,4]
print(len(randomeList))
print(len(randomeList1))


# In[37]:


# what is tuple and how to use tuples

t1 = (1,1,1,1,1,1,1)
print(t1)

# we use tupple becauese we dont want to add/update or delete 
# the values we want the values to be constant through out the project

# t1.append(3)
# t1[0] = 5

    
# how to know the length of the Tuple
randomeTuple = (12,12,4,23,23,23,3,214,12,3123,134,13,312,312,3)
randomeTuple1= (12,12,4)
print(len(randomeTuple))
print(len(randomeTuple1))


# In[60]:


# maps why do we need this data type and what purpose it surve 
# we use maps only if we want the data in key value pair unlike
# the list or tuple they dont have this functionallity 

carModel = {
    'brand': "Ford",
    'model': 'Mustang',
    'year': 1994,
}

print(carModel)


# Key must be unique if the key is not unique the dict will count the last key value


carModel1= {
    'brand': "Ford",
    'model': 'Mustang',
    'year': 1994,
    'brand': "Honda",
    'model': 'City',
    'year': 2021,
    'repaired': False

}
print(carModel1)

# how to know the length of dict

print(len(carModel1))

# we can pass any data type in the dict as values but not the keys 

randomeDic = {
      "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(randomeDic)


print(type(randomeDic))

# how to print a specific key value from a dic
print(randomeDic['year'])
print(randomeDic['brand'])
print(randomeDic['colors'])
print(randomeDic['colors'][1])

# some functions of dic

print(randomeDic.get('year'))
print(randomeDic.keys())
print(randomeDic.values())
print(randomeDic.items())


# change or update the values of dic


randomeDic['year'] = 2000
print(randomeDic)

randomeDic.update({'year': 2021})
print(randomeDic)

randomeDic.update({'new': False})
print(randomeDic)

# how to delete the key value pair

randomeDic.pop('new')
print(randomeDic)

# nested dic
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily.keys())


# In[ ]:




