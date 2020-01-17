# -*- coding:utf8 -*-

#001 字符转换为unicode
print(ord("中"))
print(oct(ord('中')))
print(hex(ord('中')))
print(bin(ord('中')))
#结果20013
#结果0o47055
#结果0x4e2d
#结果0b100111000101101

#002 Unicode转为字符
print('\u4e2d\u6587')
#\u+16进制，打印结果: 中文

# 字符'中',unicode=20013
print(chr(20013))
print(chr(0x4e2d))
# 字符'文',unicode=25991
print(chr(0o62607))
print(chr(0b110010110000111))



'''
str类型在内存Unicode表示，一个字符对应若干字节
若是网络传输或保存在磁盘，就需要str变成bytes保存
以下显示内容虽然相同，但是bytes中每个字符都只占用一个字节
'''
bx = b'abc'
x = 'abc'
# 以Unicode表示str，通过encode()方法可以编码指定的bytes类型
print(x.encode('utf-8'))
a = '中文'
print(bytes(a,encoding='utf8'))
print(a.encode('utf-8'))
# 从网络或磁盘读取字节流，bytes-->str，用decode()
print(b'abc'.decode('ascii'))
print(b'abc'.decode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 计算字符个数
print(len('abc'))
print(len('中文'))
print(len('中文'.encode('utf-8')))


'''
格式化方式和C语言一致
%d整数；%f浮点数；%s字符串；%x十六进制整数
'''
print('hello, %s' %('world'))
