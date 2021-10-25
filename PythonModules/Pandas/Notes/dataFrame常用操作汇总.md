目录

1.dataframe行列筛选

2.dataframe遍历行列

3.dataframe新增行列

4.drop删除指定行列

5.dataframe修改行列值

6.merge连接列

7.append插入行

8.concat合并列或插入行

9.跨表update

1.dataframe行列筛选
(1)df[] 按索引标签和位置序号选取行或列
df[0:1] 根据位置序号选取第一行
df[:2] 根据位置序号选取前两行
df[:'a'] 根据index标签选取第一行
df['a':'b'] 根据index标签选取前两行
df[[True,True,False]] 选取前两行
df['name'] 选取name列，返回series
df[['name','age']] 选取name,age两列，返回dataframe
df[lambda df: df.columns[0]] 选取第一列
df[lambda df: df.columns[:2]] 选取1至2列

(2)df.loc[] 按索引标签选取行和列
loc[]只能使用索引标签，不能使用位置序号，通过便签索引切边进行筛选时，前闭后闭
df.loc['a',:] 选取索引为'a'的行
df.loc[['a','b','c'],:] 选取索引为'a'或'b'或'c'的行
df.loc['a':'c', :] 选取从'a'到'c'的所有行（包括'c'行）,超过索引行不报错，返回全部行，
df.loc[:,'name'] 选取'name'列
df.loc[:,['name','age']] 选取'name'，'age'列
df.loc[:,'name':'addr'] 选取'name'至'addr'列，包括'addr'列
df.loc[:,[True,True,False]] 选取前两行
df.loc['a',['name','addr']] 选择'a'行的'name'与'addr'列数据
df.loc['a','name':'addr'] 选择'a'行的'name'至'addr'列数据
df.loc[['a','c'],['name''addr']] 选择'a','c'行的'name','addr'列数据
df.loc['a':'c','name':'addr'] 选择'a'至'c'行的'name'至'addr'列数据

(3)df.iloc[] 按位置序号选取行和列
只能使用位置序号，不能使用索引标签，通过位置序号进行筛选时，前闭后开
df.iloc[1, :] 选取第2行
df.iloc[:3, :] 选取前3行
df.iloc[[1,3,5],:] 选取第2行、第4行、第6行
df.iloc[[True,True,False], :] 通过布尔数组选取前2行
df.iloc[:, 1] 选取第2列
df.iloc[:, 0:3] 选取前3列
df.iloc[:, [0,2,3]] 选取第1列、第3列和第4列
df.iloc[:,[True,True,False]] 通过布尔数组选取前2列
df.iloc[1, [0,2,3]] 选取第2行的第1列、第3列、第4列
df.iloc[:3, :3] 选取前3行的前3列

(4)df.at[] 只能按索引标签选取单元格
df.at['b','name'] 选取b行的name列

(5)df.iat[] 只能按位置序号选取单元格
df.iat[1,0] 选取第2行第1列
list1=[['B1', '2019-12-01', 3], ['B2', '2019-12-01', 8],[None, '2019-12-02', 4],['B2',None, 5]]
data=pd.DataFrame(list1,columns=('asin','date','qty'))

(1)df[df['col']]用==,>等比较运算符
df[df['age']>28] 选取所有age大于30的行
df[[age>28 for age in df['age']]] 选取所有age大于30的行
df[(df['age']>20) & (df['sex']=='male')] 选取出所有age大于20，且sex为male的行
df[(df['age']==20) | (df['age']==32)] 选取出所有age为20或32的行
new_data=data[data['asin']=='B1']
new_data=data.loc[data['asin']=='B1']
df[(df['sex'] == 'Female') & (df['total_bill'] > 20)]
df[(df['sex'] == 'Female') | (df['total_bill'] > 20)]
df[df['total_bill'].isin([21.01, 23.68, 24.59])]
df[-(df['sex'] == 'Male')]
df[-df['total_bill'].isin([21.01, 23.68, 24.59])]

(2)df[df['col']]选出空值或非空值行
data[data[0].isna()] 选取第1列为nan的行
data[data[0].notna()] 选取第1列不为nan的行
data[data[0].isnull()] 选取第1列为nan的行
data[data[0].notnull()] 选取第1列不为nan的行
df2=df[df['search_frequency_rank'].notna()]
df2=df[df['search_frequency_rank'].isna()]
#某列空值的行(包括nan)
data=data[data['asin'].isnull()]
data=data[(data['asin'].isnull()) & (data['date'].isnull())]
#某列非空的行(包括nan)
data=data[data['asin'].notnull()]
data=data[data['asin'].notnull() & data['date'].notnull()]

(3)df[df['col'].isin()]用isin条件筛选
new_data=data[data['Sourcing Status'].isin(['Dropped','In JIRA - 2018'])]
new_data=data.loc[data['Sourcing Status'].isin(['Dropped','In JIRA - 2018'])]

(4)df[df['col'].str.contains]模糊匹配行
#筛选包括有B,注意有nan会报错,可用notnull()去除nan行
df=data[data['asin'].str.contains("B")]
#筛选包括有n的 或 有i的
df=data[data['asin'].str.contains("B|1")]
s3=pd.Series(['len','jack','win','lily','tom'],index=range(5))
s4=s3[s3.str.contains("n")] #筛选包括有n的，区分大小写
s4=s3[s3.str.contains("n|i")] #筛选包括有n的 或 有i的
s4 = s3[s3.str.contains('|'.join(['i','n']))] #join写法

(5)df.loc[] 方式
df.loc[df['age']>30,:] 选取所有age大于30的行
df.loc[df.loc[:,'age']>30, :] 选取所有age大于30的行
df.loc[lambda df:df['age'] > 30, :] 用callable对象选取age大于30的所有行
df.loc[df['age']>30,['name','age']] 输出年龄大于30的人的姓名和年龄
df.loc[(df['name']=='Mike') | (df['name']=='Marry'),['name','age']] 输出行名为‘Mike’或‘Marry’的姓名和年龄

(6)df.query()方式
df.query('a > b') 选出a列值大于b列值的行
df.query('age > 28') 选取所有age大于28的行
df.query('sex=="male"') 选取所有sex为male的行
df.query('sex==["male","female"]') 选取所有sex为male和female的行
df.query('sex!="male"') 选取所有sex不为male的行
df.query('age < 30 and revenue < 20000') 选出age小于30且revenue小于20000的行
df.query('age<30 or revenue >20000') 选出age小于30中revenue大于20000的行
df.query('A< B & B < C') 选出A列值小B列值,且B列值小C列值的列
df.query('A< B and B < C') 选出A列值小B列值,且B列值小C列值的列
df.query('A < B < C') 选出A列值小B列值,且B列值小C列值的列
df.query('["yj", "zs"] in addr') 选出addr为yj或zs的行
df.query('["yj", "zs"] not in addr') 选出addr不为yj和zs的行
df.query('age < @avg_age') 选出age小于avg_age的行,avg_age为变量，调用时前面加上@
df.query('not OUT') 选出OUT列为false的行，其中OUT的值只能为True或False

(7)where函数筛选
DataFrame.where(cond, other=nan, inplace=False, axis=None, level=None, try_cast=False, raise_on_error=True)
import numpy as np, pandas as pd
s = pd.Series(range(5))
print(s.where(s > 2))
2.dataframe遍历行列
list1=[['B1', '2019-12-01', 3], ['B2', '2019-12-01', 8],['A1', '2019-12-02', 4],['A2','2019-12-09', 5]]
data=pd.DataFrame(list1,columns=('asin','date','qty'))
(1)按行遍历iterrows()

iterrows() 按行遍历，返回(index, Series)对，通过row[name]访问元素

for index, row in data.iterrows():
print(index,row.tolist())

# 输出每行的索引值

# 0 ['B1', '2019-12-01', 3]

(2)按行遍历itertuples()

itertuples() 按行遍历，比iterrows()效率高，通过getattr(row, 'date'))访问元素

for row in data.itertuples():
print(row)
print(getattr(row, 'asin'), getattr(row, 'date')) # name与age为列名
#Pandas(Index=0, asin='B1', date='2019-12-01', qty=3)

# B1 2019-12-01

(3)按列遍历iteritems()

iteritems() 按列遍历，返回(列名, Series)对，row[index]访问元素

for column_name, row in data.iteritems():
print(column_name,row.tolist())
#asin ['B1', 'B2', 'A1', 'A2']
#date ['2019-12-01', '2019-12-01', '2019-12-02', '2019-12-09']
#qty [3, 8, 4, 5]
(4)按index遍历行

for index in data.index:
print(data.loc[index].tolist())
#['B1', '2019-12-01', 3]
#['B2', '2019-12-01', 8]
#['A1', '2019-12-02', 4]
#['A2', '2019-12-09', 5]
(5)按column遍历列

for column in data.columns:
print(data[column].tolist())

#['B1', 'B2', 'A1', 'A2']
#['2019-12-01', '2019-12-01', '2019-12-02', '2019-12-09']
#[3, 8, 4, 5]
3.dataframe新增行列
(1)整列赋单值

data['five']=9
(2)由已知列生成新列

data['qty2'] = data['qty']**3 #单列运算生成
df['col']=df['col1']+df['col2'] #多列运算生成
(3)使用df.apply函数

def padn(a,b):
if a >= 10000 and b=='male':
return 'yes'
elif a>8000 and b=='female':
return 'yes'
else:
return 'no'

df['fh']=df.apply(lambda x: padn(x.revenue,x.sex), axis = 1)
df['col3'] = df.apply(lambda x: x['col1'] + 2 * x['col2'], axis=1)
(4)使用df.map函数

1)使用自定义函数
def square(x):
return (x ** 2)
data['qty2'] = data['qty'].map(square)

2)使用匿名函数
data['qty2'] = data['qty'].map(lambda x: x**2)
(5)使用df.assign函数

df = pd.DataFrame({'temp_c': [17.0, 25.0]},index=['Portland', 'Berkeley'])
df.assign(temp_f=lambda x: x.temp_c * 9 / 5 + 32)
#等同 df.assign(temp_f=df['temp_c'] * 9 / 5 + 32)

df.assign(temp_f=lambda x: x['temp_c'] * 9 / 5 + 32,temp_k=lambda x: (x['temp_f'] + 459.67) * 5 / 9)

# temp_c temp_f temp_k

# Portland 17.0 62.6 290.15

# Berkeley 25.0 77.0 298.15

s=pd.Series([11,12,13],name='S')
data=np.arange(21,24)
df=pd.DataFrame({'A':[31,32,33],'B':[41,42,43]})
fun=lambda x:x.A+x.B
df.assign(C=fun,D=df.A+df.B,E=s,F=data)

# A B C D E F

# 0 31 41 72 72 11 21

# 1 32 42 74 74 12 22

# 2 33 43 76 76 13 23

(6)使用df.applymap函数

#用法与apply相似，但作用于所有列
df = pd.DataFrame([[1, 2.12], [3.356, 4.567]])
df.applymap(lambda x: x**2)
4.drop删除指定行列
drop(labels, axis=0, level=None, inplace=False, errors='raise')
(1)删除行
#删除单行
data=data.drop('Ohio',axis =0)
#删除多行
data=data.drop(['Ohio','Colorado'],axis =0)
#删除a和b行
df.drop(['a','b'],inplace=True)

#删除指定条件行
df_uk.drop(df_uk[df_uk['sku']==''].index)

(2)删除列
#删除单列
data=data.drop('Ohio',axis =1)
#删除多列
data=data.drop(['Ohio','Colorado'],axis =1)

(3)使用del函数
del data['two'] #two为列名 只可以删除单列
5.dataframe修改行列值
df.values[i][j]= xxx  #其中i是行号，j是列号，都是从0开始
df.values[1]=12  # 把第2行数据设为12
df['a'] = 12  # 如果指定的列名不存在，会新增列

1)使用ix函数
df_obj.ix[1:3，[1,3]]=1 #所选位置数据替换为1

2)修改具体元素值
data['four'][1]=50 #注意行名在先

3)修改列值
data['three']=1

4)修改行值
data[2:]=1 #把第3行及以后行的值设为1

5)链式赋值采用loc
df1.loc[df1.A<0.3, 'B'] = 1 #正常运行，而df1[df1.A<0.3]['B'] = 1会报SettingWithCopyWarning，且值不会修改
6.merge连接列
(1)merge语法说明
DataFrame.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
left 参与合并的左侧DataFrame
right 参与合并的右侧DataFrame
how 连接方式：'inner'（默认）；还有，'outer'、'left'、'right'
on 用于连接的列名，必须同时存在于左右两个DataFrame对象中，如果位指定，则以left和right列名的交集作为连接键
left_on 左侧DataFarme中用作连接键的列
right_on 右侧DataFarme中用作连接键的列
left_index 将左侧的行索引用作其连接键
right_index 将右侧的行索引用作其连接键
sort 根据连接键对合并后的数据进行排序，默认为True。有时在处理大数据集时，禁用该选项可获得更好的性能
suffixes 字符串值元组，用于追加到重叠列名的末尾，默认为（'_x','_y'）.例如，左右两个DataFrame对象都有'data'，则结果中就会出现'data_x'，'data_y'
copy 设置为False，可以在某些特殊情况下避免将数据复制到结果数据结构中。默认总是赋值

(2)merge连接样例
df=df1.merge(df2,on='name',how='left')
df=df1.merge(df2,left_on='name',right_on='name',how='left')
df=pd.merge(df1,df2,on=['key1','key2'],how='outer') #全连接，多键值连接
df=pd.merge(A_df, B_df, how='left', left_on=['A_c1','c2'], right_on = ['B_c1','c2']) #全连接，多键值连接

df = pd.merge(df1, df2, how='left', on='name') #左连接，关连列名相同
df = pd.merge(df1, df2, how='inner', on='name') #内连接，关连列名相同
df = pd.merge(df1, df2, how='outer', on='name') #全连接，关连列名相同
df = pd.merge(df1, df2, how='left', left_on='name1',right_on='name2') #左连接，关连列名不相同
df = pd.merge(df1, df2, how='inner', left_on='name1',right_on='name2') #内连接，关连列名不相同
7.append插入行
DataFrame.append(self, other, ignore_index=False, verify_integrity=False, sort=None)

# other：DataFrame、series、dict、list这样的数据结构

# ignore_index：默认值为False，如果为True则不使用index标签

# verify_integrity ：默认值为False，如果为True当创建相同的index时会抛出ValueError的异常

# sort：boolean，默认是None，该属性在pandas的0.23.0的版本才存在。

df1=pd.DataFrame([['B1','2019-12-01',3],['B2','2019-12-01',8]],columns=('asin','date','qty'))
df2=pd.DataFrame([['A1','2019-12-02',4],[None,None,5]],columns=('asin','date','qty'))
df=df1.append(df2, ignore_index=True)
8.concat合并列或插入行
(1)语法
pandas.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False, keys=None, levels=None,names=None, verify_integrity=False, copy=True)
axis=0, 对行操作 ，
axis=1，对列操作
join='outer', 连接各个数据，
join='inner'，只取各个数据的公共部分
join_axes=[df1.index]，保留与df1的行标签一样的数据，配合axis=1一起用 ，join_axes=[df1.columns]，保留与df1的列标签一样的数据，不要添加axis=1
ignore_index=False, 保留原索引，ignore_index=True，忽略原索引并生成新索引
keys=['x', 'y', 'z'] 对组成的每个df重新添加个索引
(2)插入行
df1=pd.DataFrame([['B1','2019-12-01',3],['B2','2019-12-01',8]],columns=('asin','date','qty'))
df2=pd.DataFrame([['A1','2019-12-02',4],[None,None,5]],columns=('asin','date','qty'))
df = pd.concat([df1,df2],axis=0)
(3)合并列（按序合并，非连接)
df1=pd.DataFrame([['B1','2019-12-01',3],['B2','2019-12-01',8]],columns=('asin','date','qty'))
df2=pd.DataFrame({'order_num':[50,56]})
df = pd.concat([df1,df2],axis=1)

asin        date  qty  order_num
0   B1  2019-12-01    3         50
1   B2  2019-12-01    8         56


9.跨表update
(1)语法
df.update(other, join='left', overwrite=True, filter_func=None, raise_conflict=False)
用另一个DataFrame中的非NA值进行就地修改
other：DataFrame，至少有一个匹配的索引/列标签;Series必设name属性
join：{'left'}仅实现左连接，保留原始对象的索引和列
overwrite =True：处理重叠键(行索引)非NA值：

* True：覆盖原始df值
* False：仅更新原始df中na的值

(2)案例
df = pd.DataFrame({'A': [11, 12, 13],'B': [14, 15, 16]})
new_df = pd.DataFrame({'B': [21, 22,23],'C': [24, 25, 26]})
df.update(new_df)

A B
0 11 21
1 12 22
2 13 23
