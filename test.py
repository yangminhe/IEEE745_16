import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

def create_button(layout, text, row, column, rowspan=1, colspan=1):
    """创建一个按钮并添加到布局中"""
    button = QPushButton(text)
    layout.addWidget(button, row, column, rowspan, colspan)
    return button

app = QApplication(sys.argv)
window = QWidget()

# 创建一个网格布局
layout = QGridLayout()

# 使用封装的函数创建按钮并添加到布局中
create_button(layout, 'Button 1', 0, 0)  # 添加到第0行第0列
create_button(layout, 'Button 2', 0, 1)  # 添加到第0行第1列
create_button(layout, 'Button 3', 1, 0, 1, 2)  # 从第1行第0列开始，跨越1行2列
create_button(layout, 'Button 4', 0, 4)  # 添加到第0行第4列
create_button(layout, 'Button 5', 2, 0, 2, 5)  # 添加到第2行第0列，跨越2行5列

window.setLayout(layout)
window.setGeometry(300, 300, 300, 200)
window.setWindowTitle('Grid Layout')
window.show()

sys.exit(app.exec_())
