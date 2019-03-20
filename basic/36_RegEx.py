#!/usr/bin/env python
# coding: utf-8

# # Python 正则表达 RegEx

# ## 导入模块

# In[ ]:


import re


# ## 简单 Python 匹配

# In[2]:


# matching string
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print(pattern1 in string)    
print(pattern2 in string)    


# ## 用正则寻找配对

# In[3]:


# regular expression
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print(re.search(pattern1, string))  
print(re.search(pattern2, string)) 


# ## 匹配多种可能 使用 []

# In[4]:


# multiple patterns ("run" or "ran")
ptn = r"r[au]n"       
print(re.search(ptn, "dog runs to cat"))    


# ## 匹配更多种可能

# In[6]:


# continue
print(re.search(r"r[A-Z]n", "dog runs to cat"))     
print(re.search(r"r[a-z]n", "dog runs to cat"))     
print(re.search(r"r[0-9]n", "dog r2ns to cat"))     
print(re.search(r"r[0-9a-z]n", "dog runs to cat"))  


# ## 特殊种类匹配

# ### 数字

# In[7]:


# \d : decimal digit
print(re.search(r"r\dn", "run r4n"))                
# \D : any non-decimal digit
print(re.search(r"r\Dn", "run r4n"))                


# ### 空白

# In[8]:


# \s : any white space [\t\n\r\f\v]
print(re.search(r"r\sn", "r\nn r4n"))               
# \S : opposite to \s, any non-white space
print(re.search(r"r\Sn", "r\nn r4n"))               


# ### 所有字母数字和"_"

# In[9]:


# \w : [a-zA-Z0-9_]
print(re.search(r"r\wn", "r\nn r4n"))               
# \W : opposite to \w
print(re.search(r"r\Wn", "r\nn r4n"))               


# ### 空白字符

# In[10]:


# \b : empty string (only at the start or end of the word)
print(re.search(r"\bruns\b", "dog runs to cat"))    
# \B : empty string (but not at the start or end of a word)
print(re.search(r"\B runs \B", "dog   runs  to cat"))  


# ### 特殊字符 任意字符

# In[11]:


# \\ : match \
print(re.search(r"runs\\", "runs\ to me"))          
# . : match anything (except \n)
print(re.search(r"r.n", "r[ns to me"))              


# ### 句尾句首

# In[12]:


# ^ : match line beginning
print(re.search(r"^dog", "dog runs to cat"))        
# $ : match line ending
print(re.search(r"cat$", "dog runs to cat"))       


# ### 是否

# In[13]:


# ? : may or may not occur
print(re.search(r"Mon(day)?", "Monday"))            
print(re.search(r"Mon(day)?", "Mon"))               


# ## 多行匹配

# In[14]:


# multi-line
string = """
dog runs to cat.
I run to dog.
"""
print(re.search(r"^I", string))                     
print(re.search(r"^I", string, flags=re.M)) 


# ## 0或多次

# In[15]:


# * : occur 0 or more times
print(re.search(r"ab*", "a"))                       
print(re.search(r"ab*", "abbbbb"))                  


# ## 1或多次

# In[16]:


# + : occur 1 or more times
print(re.search(r"ab+", "a"))                       
print(re.search(r"ab+", "abbbbb"))                  


# ## 可选次数

# In[17]:


# {n, m} : occur n to m times
print(re.search(r"ab{2,10}", "a"))                  
print(re.search(r"ab{2,10}", "abbbbb"))             


# ## group 组

# In[18]:


# group
match = re.search(r"(\d+), Date: (.+)", "ID: 021523, Date: Feb/12/2017")
print(match.group())                                
print(match.group(1))                               
print(match.group(2))                               


# In[19]:


match = re.search(r"(?P<id>\d+), Date: (?P<date>.+)", "ID: 021523, Date: Feb/12/2017")
print(match.group('id'))                            
print(match.group('date'))                          


# ## 寻找所有匹配 

# In[20]:


# findall
print(re.findall(r"r[ua]n", "run ran ren"))         


# In[21]:


# | : or
print(re.findall(r"(run|ran)", "run ran ren"))      


# ## 替换

# In[22]:


# re.sub() replace
print(re.sub(r"r[au]ns", "catches", "dog runs to cat"))     


# ## 分裂

# In[23]:


# re.split()
print(re.split(r"[,;\.]", "a;b,c.d;e"))             


# ## compile

# In[24]:


# compile
compiled_re = re.compile(r"r[ua]n")
print(compiled_re.search("dog ran to cat"))     

