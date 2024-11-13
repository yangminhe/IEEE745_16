import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

app = QApplication(sys.argv)
window = QWidget()

# 创建一个网格布局
layout = QGridLayout()

# 创建按钮并添加到布局中
button1 = QPushButton('Button 1')
layout.addWidget(button1, 0, 0)  # 添加到第0行第0列

button2 = QPushButton('Button 2')
layout.addWidget(button2, 0, 1)  # 添加到第0行第1列


# 你可以调整部件跨越的行数和列数
button3 = QPushButton('Button 3')
layout.addWidget(button3, 1, 0, 1, 2)  # 从第1行第0列开始，跨越1行2列

button4 = QPushButton('Button 4')
layout.addWidget(button4, 0, 4)  # 添加到第0行第0列

button5 = QPushButton('Button 5')
layout.addWidget(button5, 2, 0,2,5)  # 添加到第0行第0列


window.setLayout(layout)
window.setGeometry(300, 300, 300, 200)
window.setWindowTitle('Grid Layout')
window.show()

sys.exit(app.exec_())
