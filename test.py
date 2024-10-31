import sys
import struct
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

# 16进制浮点数转10进制的转换器类
class HexFloatToDecimalConverter(QWidget):
    # 初始化方法
    def __init__(self):
        super().__init__()
        self.initUI()
    
    # 界面初始化方法
    def initUI(self):
        self.setWindowTitle('16进制浮点数转10进制')
        self.setGeometry(100, 100, 400, 150)
        
        self.layout = QVBoxLayout()
        
        self.hex_label = QLabel('输入16进制浮点数:', self)
        self.layout.addWidget(self.hex_label)
        
        self.hex_input = QLineEdit(self)
        self.hex_input.setPlaceholderText('例如：40490FDB')
        self.layout.addWidget(self.hex_input)
        
        self.convert_button = QPushButton('转换', self)
        self.convert_button.clicked.connect(self.convert_hex_to_decimal)
        self.layout.addWidget(self.convert_button)
        
        self.result_label = QLabel('', self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.result_label)
        
        self.setLayout(self.layout)
    
    # 16进制转10进制的方法
    def convert_hex_to_decimal(self):
        hex_str = self.hex_input.text().strip()
        try:
            decimal_value = self.hex_float_to_decimal(hex_str)
            self.result_label.setText(f'转换结果: {decimal_value}')
        except ValueError as e:
            self.result_label.setText(f'错误: {str(e)}')
    
    # 将16进制字符串转换为10进制浮点数的方法
    def hex_float_to_decimal(self, hex_str):
        if len(hex_str) != 8:
            raise ValueError('16进制数必须是8个字符长')
        hex_bytes = bytes.fromhex(hex_str)
        float_value, = struct.unpack('!f', hex_bytes)
        return float_value
    
# 主程序入口
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HexFloatToDecimalConverter()
    ex.show()
    sys.exit(app.exec_())