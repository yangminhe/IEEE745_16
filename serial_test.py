import serial
import time

# 打开串口的函数
def open_serial_port(port, baudrate, bytesize, parity, stopbits):
    try:
        ser = serial.Serial(port, baudrate, bytesize=bytesize, parity=parity, stopbits=stopbits, timeout=1)
        print(f"串口 {port} 已打开")
        return ser
    except serial.SerialException as e:
        print(f"打开串口失败: {e}")
        return None

# 发送查询数据的函数
def send_query(ser, query_info):
    query_bytes = bytes.fromhex(query_info)  # 将十六进制字符串转换为字节
    ser.write(query_bytes)  # 发送
    print(f"已发送查询数据: {query_info}")

# 读取返回数据的函数
def read_response(ser):
    time.sleep(1)  # 等待数据返回
    if ser.in_waiting > 0:
        data = ser.readline()  # 读取一行数据
        hex_data = data.hex().upper()  # 将字节数据转换为16进制字符串并转换为大写

        # 以每4个字节分开显示
        formatted_hex_data = ' '.join(hex_data[i:i + 8] for i in range(0, len(hex_data), 8))
        print(f"接收到的16进制数据: {formatted_hex_data}")





# 关闭串口的函数
def close_serial_port(ser):
    if ser is not None and ser.is_open:
        ser.close()
        print("串口已关闭")

if __name__ == "__main__":
    # 串口配置
    serial_port_name = 'COM9'  # 串口号
    serial_baudrate = 9600      # 波特率
    serial_bytesize = serial.EIGHTBITS  # 数据位
    serial_parity = serial.PARITY_ODD    # 校验位
    serial_stopbits = serial.STOPBITS_ONE  # 停止位

    serial_port = open_serial_port(serial_port_name, serial_baudrate, serial_bytesize, serial_parity, serial_stopbits)
    
    if serial_port:
        try:
            # 查询信息
            query_info = "5B29010300003A885D"
            send_query(serial_port, query_info)  # 发送查询
            read_response(serial_port)  # 读取响应
        finally:
            close_serial_port(serial_port)  # 确保关闭串口
