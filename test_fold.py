# from sklearn.model_selection import train_test_split
# import torch
# import torch.nn as nn
# from torch_geometric.loader import DataLoader
# import random


from sklearn.model_selection import KFold


# f_ad_result,list_ad = merge_bitext('/kaggle/input/ad-cn-118/AD118')
# f_cn_result,_ = merge_bitext('/kaggle/input/ad-cn-118/CN118')
# f_result = f_ad_result+f_cn_result
# # print(list_ad[77])
data_list = [1]*232
k = 5  # 设置折数
kf = KFold(n_splits=k, shuffle=True, random_state=32)  # 创建KFold对象
# 
fold_indice = list(kf.split(data_list[:116]))
test_data_index = 4
test_index = fold_indice[test_data_index][1]
# print(test_index)
train_index = []
for i in range(5):
    if i != test_data_index:
        train_index.extend(fold_indice[i][1])
# train_data
ad_data = data_list[:116]
train_ad_data = [ad_data[i] for i in train_index]
test_ad_data = [ad_data[i] for i in test_index]
ad_data = data_list[:116]
train_cn_data = [ad_data[i] for i in train_index]
test_cn_data = [ad_data[i] for i in test_index]
train_data = train_ad_data+train_cn_data
test_data = test_ad_data+test_cn_data
# print(len(train_ad_data))
# print(len(test_cn_data))
print(train_index)
print(test_index)
# [  3   4   5   9  10  11  19  24  34  35  42  43  54  62  65  71  81  82  87  88  89 101 106]