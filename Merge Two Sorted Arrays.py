# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rP8rqgIP_qsg0F0-_EkJmJOAPsvUujIL
"""

f = open('/content/sample_data/rosalind_mer.txt', 'r')
num_A = f.readline().replace('\n', "")
list_A = f.readline().replace('\n', "").split(' ')
num_B = f.readline().replace('\n', "")
list_B = f.readline().replace('\n', "").split(' ')
f.close()

list_C = list_A + list_B
list_D = sorted(list(map(int, list_C)))

g = open('/content/drive/MyDrive/workspace/answer.txt', 'w')
for i in list_D:
    g.write(str(i))
    g.write(" ")
g.close()