"""
字符串常用操作

Version: 0.1
Author: 子梁
Date: 2019-12-10
"""
str1 = 'hello,world!'
print('字符串的长度是:',len(str1))
print('单词首字母大写:',str1.title())
print('字符串大写:',str1.upper())

print('字符串是否大写:',str1.isupper())
print('字符串是否以hello开头',str1.startswith('hello'))
print('字符串是否以hello结尾',str1.endswith('hello'))
str2 = '- \u9a86\u660a'
str3 = str1.title() + ' ' + str2.lower()
print(str3)
