import sys
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QComboBox, QPushButton, QMessageBox,
                             QTextEdit, QLineEdit, QGroupBox, QGridLayout)


class SerialPortApp(QWidget):
    def __init__(self):
        super().__init__()
        self.serial = None
        self.is_serial_open = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle("串口调试助手")
        self.setGeometry(100, 100, 800, 600)

        main_layout = QHBoxLayout(self)
        main_layout.addWidget(self.create_settings_group())
        main_layout.addWidget(self.create_display_group())
        main_layout.addLayout(self.create_send_grid())

    def create_settings_group(self):
        settings_group = QGroupBox("COM口设置")
        settings_layout = QVBoxLayout()

        self.com_combo = QComboBox()
        self.update_com_ports()

        self.baudrate_input = self.create_baudrate_input()
        self.databits_combo = self.create_combo_box(["5", "6", "7", "8"])
        self.parity_combo = self.create_combo_box(["无", "奇", "偶"])
        self.stopbits_combo = self.create_combo_box(["1", "1.5", "2"])

        self.toggle_serial_button = QPushButton("打开串口")
        self.toggle_serial_button.clicked.connect(self.toggle_serial)

        for label, widget in zip(["COM口", "波特率", "数据位", "校验位", "停止位"],
                                 [self.com_combo, self.baudrate_input, self.databits_combo,
                                  self.parity_combo, self.stopbits_combo]):
            settings_layout.addWidget(QLabel(label))
            settings_layout.addWidget(widget)

        settings_layout.addWidget(self.toggle_serial_button)
        settings_group.setLayout(settings_layout)
        return settings_group

    def create_baudrate_input(self):
        baudrate_input = QLineEdit()
        baudrate_input.setPlaceholderText("请输入波特率（如：9600）")
        baudrate_input.setText("9600")
        return baudrate_input

    def create_display_group(self):
        display_group = QGroupBox("数据接收")
        display_layout = QVBoxLayout()
        self.display_box = QTextEdit()
        self.display_box.setReadOnly(True)
        display_layout.addWidget(self.display_box)

        clear_button = QPushButton("清空接收框")
        clear_button.clicked.connect(self.clear_display)
        display_layout.addWidget(clear_button)
        display_group.setLayout(display_layout)
        return display_group

    def create_send_grid(self):
        send_group = QGroupBox("发送区")
        grid_layout = QGridLayout()

        self.send_input = QTextEdit()
        self.send_input.setMinimumWidth(300)

        send_button = QPushButton("发送")
        send_button.clicked.connect(self.send_data)

        grid_layout.addWidget(self.send_input, 0, 0)
        grid_layout.addWidget(send_button, 0, 1)

        grid_layout.addWidget(send_group, 0, 0, 1, 2)  # 发送区占一行
        return grid_layout

    def create_combo_box(self, items):
        combo = QComboBox()
        combo.addItems(items)
        return combo

    def update_com_ports(self):
        self.com_combo.clear()
        ports = serial.tools.list_ports.comports()
        self.com_combo.addItems([port.device for port in ports])

    def toggle_serial(self):
        if not self.is_serial_open:
            self.open_serial()
        else:
            self.close_serial()

    def open_serial(self):
        try:
            com_port = self.com_combo.currentText()
            baudrate = int(self.baudrate_input.text())
            databits = int(self.databits_combo.currentText())
            parity = self.get_parity_value()
            stopbits = self.get_stopbits_value()

            self.serial = serial.Serial(port=com_port, baudrate=baudrate,
                                        bytesize=databits, parity=parity,
                                        stopbits=stopbits)
            self.is_serial_open = True
            self.toggle_serial_button.setText("关闭串口")
            self.toggle_serial_button.setStyleSheet("background-color: red;")
            QMessageBox.information(self, "成功", f"成功打开 {com_port}")
        except (serial.SerialException, ValueError) as e:
            QMessageBox.critical(self, "错误", f"无法打开串口: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"未知错误: {str(e)}")

    def get_parity_value(self):
        parity_map = {
            "无": serial.PARITY_NONE,
            "奇": serial.PARITY_ODD,
            "偶": serial.PARITY_EVEN
        }
        return parity_map.get(self.parity_combo.currentText(), serial.PARITY_NONE)

    def get_stopbits_value(self):
        stopbits_map = {
            1: serial.STOPBITS_ONE,
            1.5: serial.STOPBITS_ONE_POINT_FIVE,
            2: serial.STOPBITS_TWO
        }
        return stopbits_map.get(float(self.stopbits_combo.currentText()), serial.STOPBITS_ONE)

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
            data = self.send_input.toPlainText()
            if data:
                self.serial.write(data.encode('utf-8'))
                self.display_box.append(f"发送: {data}")
            else:
                QMessageBox.warning(self, "警告", "发送内容不能为空")
        else:
            QMessageBox.warning(self, "警告", "请先打开串口")

    def clear_display(self):
        self.display_box.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = SerialPortApp()
    window.show()
    sys.exit(app.exec_())
