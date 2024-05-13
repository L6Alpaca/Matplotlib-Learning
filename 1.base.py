import matplotlib.pyplot as plt
import random
from pylab import mpl

# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

# 0.准备数据
x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]
# 增加北京的温度数据
y_beijing = [random.uniform(1, 3) for i in x]

# 1.创建画布    figsize(长，宽)与x、y有多少项无关  dpi——清晰度（画质）
plt.figure(figsize=(20, 8), dpi=100)

# 2.绘制图像    plot(x,y)可补充color、linestyle等
plt.plot(x, y_shanghai)
#如果一个坐标系显示多个图像——多次plt.plot()
plt.plot(x,y_beijing,color = 'r', linestyle = "--")

# 2.1 添加x,y轴刻度
# 构造x,y轴刻度标签
x_ticks_label = ["11点{}分".format(i) for i in x]
y_ticks = range(40)

# 刻度显示
plt.xticks(x[::5], x_ticks_label[::5])
plt.yticks(y_ticks[::5])

# 2.2 添加网格显示    alpha表示网格颜色深浅，属于[0,1]
plt.grid(True, linestyle="--", alpha=0.5)
#linestyle supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'

# 2.3 添加描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("中午11点--12点某城市温度变化图", fontsize=20)    #fontsize表示字体大小

# 2.4 图像保存
plt.savefig("./test.png")   #*注意：plt.show()会释放figure资源，如果在显示图像之后保存图片将只能保存空图片  所以show前save

# 3.图像显示
plt.show()
