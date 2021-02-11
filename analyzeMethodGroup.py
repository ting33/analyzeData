import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('/Users/zhouya/Desktop/testData/supermarket.csv',encoding='gbk',parse_dates=['成交时间'])
# print(data.info())
#哪些类别的商品比较畅销
catagory=data.groupby('类别ID')['销量'].sum().reset_index()
catagoryTop10=catagory.sort_values(by='销量',ascending=False)
print(catagoryTop10.head(10))

#哪些上商品比较畅销
# goods=data.groupby('商品ID')['销量'].sum().reset_index().sort_values(by='销量',ascending=False)
#方法二：用数据透视表
goods=pd.pivot_table(data,index='商品ID',values='销量',aggfunc='sum').reset_index().sort_values(by='销量',ascending=False)
print(goods.head(10))

#不同门店的销售额占比
data['销售额']=data['销量']*data['单价']
shopData=data.groupby('门店编号')['销售额'].sum()
ratio=shopData/data['销售额'].sum()
print(ratio)

#哪些时间段是超市的客流高峰期
data['小时']=data['成交时间'].map(lambda x:int(x.strftime("%H")))
traffic=data[['小时','订单ID']].drop_duplicates()
traffic_hour=traffic.groupby('小时')['订单ID'].count()
print(traffic_hour)
plt.plot(traffic_hour)
plt.show()
