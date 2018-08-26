import itchat
itchat.login()
# 爬取自己好友的相关信息，返回一个json文件
friends = itchat.get_friends(update = True)[0:]

# 初始化计数器
male = female = other = 0
# friends[0]是自己的信息，所以应该从friends[1]开始
for person in friends[1:]:
    sex = person["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
# 计算朋友的总数
total = len(friends[1:])
# 打印出自己的好友性别比例
malecol=round(float(male)/total*100,2)
femalecol=round(float(female)/total*100,2)
othercol=round(float(other)/total*100,2)
print("您共有%d个好友"%(total))
print('男性朋友：%.2f%%' %(malecol)+'\n'+'女性朋友:%.2f%%' % (femalecol)+'\n'+'性别不明的好友：%.2f%%' %(othercol))

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# #解决中文乱码不显示问题
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题
map = {
    'Female': (femalecol, '#7199cf'),
    'Male': (malecol, '#4fc4aa'),
    'other': (othercol, '#e1a7a2')
}

fig = plt.figure(num=1,figsize=(5, 5))  # 整体图的大小
ax = fig.add_subplot(111)  # 添加一个子图
ax.set_title('Gender of friends')
xticks = np.arange(3) + 0.15  # 生成x轴每个元素的位置
bar_width = 0.5  # 定义柱状图每个柱的宽度
names = map.keys()  # 获得x轴的值
values = [x[0] for x in map.values()]  # y轴的值
colors = [x[1] for x in map.values()]  # 对应颜色

bars = ax.bar(xticks, values, width=bar_width, edgecolor='none')  # 画柱状图，横轴是x的位置，纵轴是y，定义柱的宽度，同时设置柱的边缘为透明
ax.set_ylabel('Proprotion')  # 设置标题
ax.set_xlabel('Gender')
ax.set_xticks(xticks)  # x轴每个标签的具体位置
ax.set_xticklabels(names)  # 设置每个标签的名字
ax.set_xlim([bar_width / 2 - 0.5, 3 - bar_width / 2])  # 设置x轴的范围
ax.set_ylim([0, 100])  # 设置y轴的范围
for bar, color in zip(bars, colors):
    bar.set_color(color)  # 给每个bar分配指定的颜色
    height = bar.get_height()  # 获得高度并且让字居上一点
    plt.text(bar.get_x() + bar.get_width() / 4., height, '%.2f%%' % float(height))  # 写值

# 画饼状图
fig1 = plt.figure(num=2,figsize=(5, 5))  # 整体图的标题
ax = fig1.add_subplot(111)
ax.set_title('Pie chart')
labels = ['{}\n{} %'.format(name, value) for name, value in zip(names, values)]
ax.pie(values, labels=labels, colors=colors)  # 并指定标签和对应颜色



# 用来爬取各个变量
def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable


# 调用函数得到各个变量，并把数据存到csv文件中，保存到桌面
NickName = get_var('NickName')
Sex = get_var('Sex')
Province = get_var('Province')
City = get_var('City')
Signature = get_var('Signature')


cities = set(City)  # 去重
citysarray = []
for item in cities:
    citysarray.append((item, City.count(item)))  # 获取个数


def by_num(p):
    return p[1]


citiesdsored = sorted(citysarray, key=by_num, reverse=True)  # 根据个数排序

# 画图
figcity = plt.figure(figsize=(10, 5))  # 整体图的标题
axcity = figcity.add_subplot(111)  # 添加一个子图
axcity.set_title('City')
xticks = np.linspace(0.5, 20, 20)  # 生成x轴每个元素的位置
bar_width = 0.8  # 定义柱状图每个柱的宽度
cities = []
values = []
count = 0
for item in citiesdsored:
    if item[0]=="":
        cities.append("未知")
    else:
        cities.append(item[0])
    values.append(item[1])
    count = count + 1
    if count >= 20:
        break

colors = ['#FFEC8B', '#FFE4C4', '#FFC125', '#FFB6C1', '#CDCDB4', '#CDC8B1', '#CDB79E', '#CDAD00', '#CD96CD', '#CD853F',
          '#C1FFC1', '#C0FF3E', '#BEBEBE', '#CD5C5C', '#CD3700', '#CD2626', '#8B8970', '#8B6914', '#8B5F65',
          '#8B2252']  # 对应颜色

bars = axcity.bar(xticks, values, width=bar_width, edgecolor='none')
axcity.set_ylabel('人数')  # 设置标题
axcity.set_xlabel('城市')
axcity.set_xticks(xticks)  # x轴每个标签的具体位置
axcity.set_xticklabels(cities)  # 设置每个标签的名字
axcity.set_xlim(0, 20)  # 设置x轴的范围
axcity.set_ylim([0, 200])  # 设置y轴的范围

for bar, color in zip(bars, colors):
    bar.set_color(color)  # 给每个bar分配指定的颜色
    height = bar.get_height()  # 获得高度并且让字居上一点
    plt.text(bar.get_x() + bar.get_width() / 4., height, '%.d' % float(height))  # 写值


pros = set(Province)  # 去重
prosarray = []
for item in pros:
    prosarray.append((item, Province.count(item)))  # 获取个数


def by_num(p):
    return p[1]


prosdsored = sorted(prosarray, key=by_num, reverse=True)  # 根据个数排序

# 画图
figpro = plt.figure(figsize=(10, 5))  # 整体图的标题
axpro = figpro.add_subplot(111)  # 添加一个子图
axpro.set_title('Province')
xticks = np.linspace(0.5, 20, 20)  # 生成x轴每个元素的位置
bar_width = 0.8  # 定义柱状图每个柱的宽度
pros = []
values = []
count = 0
for item in prosdsored:
    if item[0]=="":
        pros.append("未知")
    else:
        pros.append(item[0])
    values.append(item[1])
    count = count + 1
    if count >= 20:
        break

colors = ['#FFEC8B', '#FFE4C4', '#FFC125', '#FFB6C1', '#CDCDB4', '#CDC8B1', '#CDB79E', '#CDAD00', '#CD96CD', '#CD853F',
          '#C1FFC1', '#C0FF3E', '#BEBEBE', '#CD5C5C', '#CD3700', '#CD2626', '#8B8970', '#8B6914', '#8B5F65',
          '#8B2252']  # 对应颜色

bars = axpro.bar(xticks, values, width=bar_width, edgecolor='none')
axpro.set_ylabel('人数')  # 设置标题
axpro.set_xlabel('省份')
axpro.set_xticks(xticks)  # x轴每个标签的具体位置
axpro.set_xticklabels(pros)  # 设置每个标签的名字
axpro.set_xlim(0, 20)  # 设置x轴的范围
axpro.set_ylim([0, 200])  # 设置y轴的范围

for bar, color in zip(bars, colors):
    bar.set_color(color)  # 给每个bar分配指定的颜色
    height = bar.get_height()  # 获得高度并且让字居上一点
    plt.text(bar.get_x() + bar.get_width() / 4., height, '%.d' % float(height))  # 写值



# 保存数据
from pandas import DataFrame

data = {'NickName': NickName, 'Sex': Sex, 'Province': Province, 'City': City, 'Signature': Signature}
frame = DataFrame(data)

frame.to_csv('data.csv', index=True,encoding="utf_8_sig")
plt.show()