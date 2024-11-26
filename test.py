from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.button = QPushButton('点击我')
        self.button.clicked.connect(self.on_button_click)  # 连接点击事件到槽函数

        layout.addWidget(self.button)
        self.setLayout(layout)
    def on_button_click(self):
        print("按钮被点击了！")  # 处理按钮点击事件的代码

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
