import serial

ser=serial.Serial()
ser.port='COM9'
ser.baudrate=9600
ser.bytesize=serial.EIGHTBITS
ser.parity=serial.PARITY_ODD
ser.stopbits=serial.STOPBITS_ONE
ser.timeout=1

ser.open()
data = ser.readline()
print(data)
