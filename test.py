import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QLabel

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('勾选按钮示例')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.checkbox = QCheckBox('我同意使用条款', self)
        self.checkbox.stateChanged.connect(self.checkbox_changed)
        layout.addWidget(self.checkbox)

        self.label = QLabel('您是否同意使用条款？', self)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def checkbox_changed(self, state):
        if state == 2:  # 选中状态
            self.label.setText('您同意使用条款')
        else:  # 未选中状态
            self.label.setText('您是否同意使用条款？')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())
