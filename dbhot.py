# 导入matplotlib库
import matplotlib.pyplot as plt

# 定义六个类别
categories = ["all", "car", "van", "bus", "truck", "bike", "motor"]

# 定义每个类别的两个数据
data1 = [0.76, 0.942, 0.987, 0.957, 0.739, 0.391, 0.543]
data2 = [0.778, 0.942, 0.98, 0.957, 0.759, 0.454, 0.579]

# 定义柱状图的宽度
width = 0.4

# 定义柱状图的位置
x1 = range(len(categories))
x2 = [i + width for i in x1]

# 绘制柱状图
plt.bar(x1, data1, width=width, label="Not Enabling img-weights")
plt.bar(x2, data2, width=width, label="Enabling img-weights")

# 设置横坐标的刻度和标签
plt.xticks([i + width/2 for i in x1], categories)

# 设置纵坐标的标签
plt.ylabel("mAP@0.5")

# 设置图例
plt.legend()

plt.savefig("val_mAP.png")
# 显示图形
plt.show()

# 短视频功能，开发了一个月
# 第二个功能，添加好友(修复bug)
# 商城功能 100%
>>>>>>> dev
