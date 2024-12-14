import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 创建复选框
        self.checkBox = QCheckBox('启用选项', self)
        self.checkBox.stateChanged.connect(self.onCheckBoxChanged)

        # 创建一个标签用于显示复选框的状态
        self.label = QLabel('状态：未选中', self)

        # 将复选框和标签添加到布局中
        layout.addWidget(self.checkBox)
        layout.addWidget(self.label)

        # 设置窗口的布局
        self.setLayout(layout)

        # 设置窗口标题和大小
        self.setWindowTitle('PyQt5 复选框示例')
        self.setGeometry(300, 300, 250, 150)

    def onCheckBoxChanged(self, state):
        # 检测复选框的状态并更新标签
        if state == Qt.Checked:
            self.label.setText('状态：已选中')
        else:
            self.label.setText('状态：未选中')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
