# -*- coding:utf8 -*-

'''
Unicode是内存编码的规范，
UTF-8是如何保存于传输Unicode的手段
所有字符串都是unicode字符串
Python3中默认源码是UTF-8编码
'''
#001 字符转换为Unicode
print(ord("中"))
print(oct(ord('中')))
print(hex(ord('中')))
print(bin(ord('中')))

#002 Unicode转化为'中'
print(chr(20013))
#print(chr(0o47055))
#print(chr(0x4e2d))
#print(chr(0b100111000101101))

#003 Unicode转为字符
print('\u4e2d\u6587')
#结果\u+16进制: 中文，


'''
str类型在内存Unicode表示，一个字符对应若干字节
若是网络传输或保存在磁盘，就需要str变成bytes保存
以下显示内容虽然相同，但是bytes中每个字符都只占用一个字节
'''
row_str1 = 'aAbBcDxXyYzZ'
# 以Unicode表示str
# 通过encode()方法可以编码指定的bytes类型
print(row_str1.encode('utf-8'))
#结果: b'aAbBcDxXyYzZ'

# 中文-->utf8编码
china_str1 = '中文'
print(bytes(china_str1,encoding='utf8'))
print(china_str1.encode('utf-8'))
#结果: b'\xe4\xb8\xad\xe6\x96\x87'

# 从网络或磁盘读取字节流
# bytes-->str，用decode()
byte_str1 = row_str1.encode('utf-8')
china_utf8 = china_str1.encode('utf-8')
print(byte_str1.decode('ascii'))
print(byte_str1.decode('utf-8'))
print(china_utf8.decode('utf-8'))

# 计算字符个数
print(len('abc'))
print(len('中文'),len('中文'.encode('utf-8')))
#结果: 3 2 6

