import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Simhei'] 
import matplotlib.pyplot as plt
import numpy as np

# Set data for the nodes and their relationships
nodes = {
    "瑞幸": 0.8,
    "茅台": 0.7,
    "股价": 0.6,
    "营收": 0.5,
    "高管": 0.4,
    "营销策略": 0.3,
    "财务造假": 0.2,
    "雷军": 0.1
}

import csv

# 请将下面的文件路径替换为你实际的CSV文件路径
file_path = 'keywords.txt'

keyword = []
with open(file_path, newline='',encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        # print(row)
        keyword.append(row)

keyword = keyword[:100]
nodes = {keyword[i][0]: float(keyword[i][1]) for i in range(len(list(keyword)))}

print(nodes)
# Initialize plot
fig, ax = plt.subplots(figsize=(8, 8))
# ax.set_facecolor('#CCE5FF')
plt.rcParams['axes.facecolor'] = 'lightblue'
# Add circles (nodes) based on the correlation strength
for node, strength in nodes.items():
    r = (1-strength) * 5  # Adjust the scaling factor as needed
    theta = np.random.rand() * 2 * np.pi
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.plot(x, y, 'o',markersize = 30,label=node)
    ax.text(x, y, node, ha='center', va='center', fontsize=12)
# color='red')
# for node, strength in nodes.items():
r = 0.55 * 5  # Adjust the scaling factor as needed
theta = np.linspace(0, 2*np.pi, 100)
x = r * np.cos(theta)
y = r * np.sin(theta)

ax.plot(x, y, label=node)

# Set aspect of the plot to be equal
ax.set_aspect('equal')

# Remove axes
plt.axis('off')

plt.show()
