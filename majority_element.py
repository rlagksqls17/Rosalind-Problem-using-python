# -*- coding: utf-8 -*-
"""Majority_Element.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n5ch_NWYvnYHkO83IvJelEQwHAW_Wzta
"""

from scipy.stats import mode

def Clear_data_list(a):
    return [list(map(int, (data.replace("\n", '')).split(" "))) for data in a]

f = open('/content/drive/MyDrive/workspace/rosalind_maj (1).txt', 'r')
get_list = f.readline().replace('\n', "").split(' ')
m = get_list[1] # 각 리스트의 요소 개수
data_list = f.readlines()
f.close()

clear_list = Clear_data_list(data_list) # 정제한 데이터들을 DataFrame으로 변환

answer_list = []
for L in clear_list:
    if int(mode(L).count) > int(int(m)/2): 
      answer_list.append(int(mode(L).mode))
    else:
        answer_list.append(-1)

g = open('/content/drive/MyDrive/workspace/answer.txt', 'w')
for i in answer_list:
    g.write(str(i))
    g.write(" ")
g.close()