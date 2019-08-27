#!/usr/bin/env python
# coding: utf-8

# # Calculadora

# In[7]:


def suma (a,b):
    c=a+b
    return c


# In[8]:


def resta (a,b):
    c=a-b
    return c


# In[9]:


def multi (a,b):
    c=a*b
    return c


# In[10]:


def divi (a,b):
    c=a/b
    return c


# In[6]:


a=int(input("Dame un numero positivo "))
b=int(input("Dame otro numero positivo "))
print("La suma es: ", suma(a,b))
print("La resta es: ", resta(a,b))
print("La multiplicación es: ", multi(a,b))
print("La división es: ", divi(a,b))


# In[ ]:




