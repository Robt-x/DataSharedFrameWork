from ECC import *
import py_ecc as ecc
import binascii
import base64
import secrets
from tinyec import registry
curve = registry.get_curve('secp256r1')
k = secrets.randbelow(curve.field.n)
K = k * curve.g
r = secrets.randbelow(curve.field.n)
rK = r * K  # = r * k * G
rG = r * curve.g
# print(r)
# print(rK)
# print(rG)
text = "i ord() 返回 单字符 对应的 ascii码 。 chr() 返回 ascii码 对应的 单字符 "
text.strip()
cipher = []
for char in text:
    intchar = ord(char)
    print(char, end=': ')
    print(intchar)
    C1 = intchar + rK.x + rK.y
    cipher.append([C1, rG])
for i in cipher:
    print(i)
s = ''
for (c_text, C2) in cipher:
    kC2 = C2 * k
    intch = c_text - kC2.y - rK.x
    s += chr(intch)
print(s)
# secp = ecc.secp256k1
#
#
# def HexToDec(value):
#     try:
#         return int(value.replace(' ', ''), 16)
#     except ValueError:
#         return "Invalid Hexadecimal Value"
#
# p = secp.P
# a = HexToDec("0000000000000000000000000000000000000000000000000000000000000000")
# b = HexToDec("0000000000000000000000000000000000000000000000000000000000000007")
# G = secp.G
# G_x, G_y = G[0], G[1]
# # 获取椭圆曲线的阶
# n = secp.N
# # key = '792eca682b890b31356247f2b04662bff448b6bb19ea1c8ab48da222c894efab'
# key = '000000000000000000000000000000000000000000000000000000000000000c'
# KEY = secp.privtopub(binascii.unhexlify(key))
# KEY_x, kEY_y = KEY[0], KEY[1]
# print("a: {:}\nb: {:}\np: {:}\nG: {:}\nn: {:}\nkey: {:}\nKEY: {:}".format(a, b, p, G, n, key, KEY))

