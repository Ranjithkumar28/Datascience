#!/usr/bin/env python
# coding: utf-8

# ### The questions for the exercises are given above the cells and the expected output is given below the cell. Please type the code inserting a new cell below the question because if you run the expected output cell the output would vanish! Happy learning! 

# ## Exercise Question 1: Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list
# 
# For example: List = [54, 44, 27, 79, 91, 41]

# In[1]:





# In[1]:


sample_lst = [34, 54, 67, 89, 11, 43, 94]
print("Original List", sample_lst)

# Removed the 4th element from the list
rmv_ele = sample_lst[4]
sample_lst.remove(rmv_ele)
print("List After removing element at index 4", sample_lst)

# Inserted the value at the index 2
sample_lst.insert(2, rmv_ele)
print("List after Adding element at index 2", sample_lst)

# Appended the value at the end of the list
sample_lst.append(rmv_ele)
print("List after Adding element at last", sample_lst)


# ## Exercise Question 2: Given a two list of equal size create a list of unique elements from both the lists into a seperate list

# In[10]:





# In[2]:


frst_lst = [2, 3, 4, 5, 6, 7, 8]
sec_lst = [4, 9, 16, 25, 36, 49, 64]
print("First list", frst_lst)
print("Second list", sec_lst)

# Merge two list using extend method
frst_lst.extend(sec_lst)

# Converting it set to get unique values and then convert it back to list
output = list(set(frst_lst))
print("Output", output)

# Alternative method 
unique_lst = list(set(frst_lst + sec_lst))
print("Alternative Method Output", unique_lst)


# ## Exercise Question 3: Remove duplicate from a list and create a tuple and find the minimum and maximum number (Hint: Try Functions Min() and Max() ) 

# In[11]:





# In[4]:


orig_lst = [87, 52, 44, 53, 54, 87, 52, 53]
print("Original list", orig_lst)

# Get unique values
unique_lst = list(set(orig_lst))
print("Unique list", unique_lst)

# Converting list to tuple
tuple_lst = tuple(unique_lst)
print("Tuple", tuple_lst)

# Get Min Values
min_val = min(tuple_lst)
print("Min value", min_val)

# Get Max Values
max_val = max(tuple_lst)
print("Max value", max_val)


# ## Exercise Question 4: Display the each word in the string Count the number of words in a string and display it (Including the white spaces) 

# In[19]:


#Printing each words seperately 
a = "what's up?"
print(*a)


# In[18]:





# In[ ]:


str = "Welcome to Python"
print("The sample string:", str)
print("Printing each words seperately:", *str)

# Print the length of the string
print("The Length of the string:", len(str))


# ##  Exercise Question 5: Write a Python program to access dictionary keys element by index. i.e. Use indexing methods to print the first key

# In[27]:





# In[7]:


sample_lst = [['physics',80],['math',90],['chemistry',86]]

# Convert list to dict
print("The dictionary is:", dict(sample_lst))
      
# To access the key element by the index
print("The key element accesed by index:", sample_lst[0][0])

# Alternate Method  

dict = {'physics': 80, 'math': 90, 'chemistry': 86};
print("The key element accesed by index:", list(dict.keys())[0])

