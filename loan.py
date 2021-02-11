import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('/Users/zhouya/Desktop/testData/loan.csv',encoding='gbk')
print(data.info())
#填充缺失值
data=data.fillna({'月收入':data['月收入'].mean()})
print(data.info())
#收入和坏账率有啥关系  对连续值分析时一般都会离散化，将连续值进行区间切分
cut_bins=[0.500,1000,15000,20000,100000]
income_cut=pd.cut(data['月收入'],cut_bins)
all_income_user=data['好坏客户'].groupby(income_cut).count()
bad_income_user=data['好坏客户'].groupby(income_cut).sum()
bad_rate=bad_income_user/all_income_user
print(bad_rate)

