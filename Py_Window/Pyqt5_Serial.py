import sys
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QComboBox, QPushButton, QMessageBox,
                             QTextEdit, QLineEdit, QGroupBox, QCheckBox)

class SerialPortApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.serial = None
        self.is_serial_open = False

    def initUI(self):
        self.setWindowTitle("串口调试助手")
        self.setGeometry(100, 100, 800, 600)  # 主窗口大小

        main_layout = QHBoxLayout(self)

        # 左侧设置区域
        settings_group = QGroupBox("COM口设置")
        settings_layout = QVBoxLayout()

        # 添加选择框和标签
        self.com_combo = QComboBox()
        self.update_com_ports()
        self.baudrate_combo = QComboBox()
        self.baudrate_combo.addItems(["9600", "115200", "57600", "38400", "19200"])
        self.databits_combo = QComboBox()
        self.databits_combo.addItems(["5", "6", "7", "8"])
        self.parity_combo = QComboBox()
        self.parity_combo.addItems(["无", "奇", "偶"])
        self.stopbits_combo = QComboBox()
        self.stopbits_combo.addItems(["1", "1.5", "2"])

        # 串口控制
        self.toggle_serial_button = QPushButton("打开串口")
        self.toggle_serial_button.clicked.connect(self.toggle_serial)
        
        
        # 将控件放置到设置布局
        settings_layout.addWidget(QLabel("COM口"))
        settings_layout.addWidget(self.com_combo)
        settings_layout.addWidget(QLabel("波特率"))
        settings_layout.addWidget(self.baudrate_combo)
        settings_layout.addWidget(QLabel("数据位"))
        settings_layout.addWidget(self.databits_combo)
        settings_layout.addWidget(QLabel("校验位"))
        settings_layout.addWidget(self.parity_combo)
        settings_layout.addWidget(QLabel("停止位"))
        settings_layout.addWidget(self.stopbits_combo)
        settings_layout.addWidget(self.toggle_serial_button)

        settings_group.setLayout(settings_layout)
        main_layout.addWidget(settings_group)

        # 中间显示区域
         # 中间显示区域
        display_group = QGroupBox("数据接收")
        display_layout = QVBoxLayout()
        self.display_box = QTextEdit()
        self.display_box.setReadOnly(True)
        display_layout.addWidget(self.display_box)

        # 添加清空接收框按钮
        clear_button = QPushButton("清空接收框")
        clear_button.clicked.connect(self.clear_display)
        
        display_layout.addWidget(clear_button)  # 将清空按钮添加到布局
        display_group.setLayout(display_layout)
        main_layout.addWidget(display_group)

        # 发送数据区域
        send_group = QGroupBox("发送区")
        send_layout = QVBoxLayout()
        send_input_layout = QHBoxLayout()

        self.send_input = QLineEdit()  
        self.send_input.setMinimumWidth(300)  # 设置最小宽度
        self.send_input.setMinimumHeight(200)  # 设置最小高度
        send_button = QPushButton("发送")
        send_button.clicked.connect(self.send_data)
        send_input_layout.addWidget(self.send_input)
        send_input_layout.addWidget(send_button)

        send_layout.addLayout(send_input_layout)
        send_group.setLayout(send_layout)
        main_layout.addWidget(send_group)



    def update_com_ports(self):
        ports = serial.tools.list_ports.comports()
        self.com_combo.clear()
        for port in ports:
            self.com_combo.addItem(port.device)

    def toggle_serial(self):
        if not self.is_serial_open:
            self.open_serial()
        else:
            self.close_serial()

    def open_serial(self):
        com_port = self.com_combo.currentText()
        baudrate = int(self.baudrate_combo.currentText())
        databits = int(self.databits_combo.currentText())
        parity = self.parity_combo.currentText()
        stopbits = float(self.stopbits_combo.currentText())

        parity_value = serial.PARITY_NONE
        if parity == "奇":
            parity_value = serial.PARITY_ODD
        elif parity == "偶":
            parity_value = serial.PARITY_EVEN

        stopbits_value = serial.STOPBITS_ONE
        if stopbits == 1.5:
            stopbits_value = serial.STOPBITS_ONE_POINT_FIVE
        elif stopbits == 2:
            stopbits_value = serial.STOPBITS_TWO

        try:
            self.serial = serial.Serial(
                port=com_port,
                baudrate=baudrate,
                bytesize=databits,
                parity=parity_value,
                stopbits=stopbits_value
            )
            self.is_serial_open = True
            self.toggle_serial_button.setText("关闭串口")
            self.toggle_serial_button.setStyleSheet("background-color: red;")
            QMessageBox.information(self, "成功", f"成功打开 {com_port}")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"无法打开串口: {str(e)}")

    def close_serial(self):
        if self.serial and self.serial.is_open:
            self.serial.close()
            self.is_serial_open = False
            self.toggle_serial_button.setText("打开串口")
            self.toggle_serial_button.setStyleSheet("")
            QMessageBox.information(self, "成功", "串口已关闭")
        else:
            QMessageBox.warning(self, "警告", "串口未打开")
    
    def send_data(self):
        if self.serial and self.serial.is_open:
            data = self.send_input.text()
            self.serial.write(data.encode('utf-8'))
            self.display_box.append(f"发送: {data}")
        else:
            QMessageBox.warning(self, "警告", "请先打开串口")
            
    def clear_display(self):
        self.display_box.clear()  # 清空接收框内容

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = SerialPortApp()
    window.show()
    sys.exit(app.exec_())
