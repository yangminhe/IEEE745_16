import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()  # 主垂直布局
        self.setLayout(self.layout)

        self.add_button = QPushButton("添加")
        self.add_button.clicked.connect(self.add_horizontal_box)  # 连接按钮点击事件
        self.layout.addWidget(self.add_button)  # 将添加按钮加入布局

    def add_horizontal_box(self):
        horizontal_layout = QHBoxLayout()  # 创建水平布局
        line_edit = QLineEdit()  # 创建输入框
        send_button = QPushButton("发送")  # 创建发送按钮

        horizontal_layout.addWidget(line_edit)  # 将输入框加入水平布局
        horizontal_layout.addWidget(send_button)  # 将发送按钮加入水平布局
        
        self.layout.addLayout(horizontal_layout)  # 将水平布局加入主布局
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('动态添加控件示例')
    window.show()
    sys.exit(app.exec_())
