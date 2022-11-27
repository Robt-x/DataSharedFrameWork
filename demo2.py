import base64 as b64

from tinyec import registry, ec

sub_group = ec.SubGroup(
    p=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F,
    g=(0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
       0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8),
    n=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141,
    h=0x1
)
curve = ec.Curve(a=0, b=7, field=sub_group, name='secp256k1')
# curve = registry.get_curve('secp256r1')
K = 30
p = curve.field.p


# encode int m to a point on E
def curveEncode(m):
    m *= K
    while True:
        # step 1
        f = pow(m, 3, p) + 7  # secp256k1, change it to your curve
        f = f % p
        # step 2
        y = pow(f, (p + 1) // 4, p)  # p+1 because p mod 4 = 3, to be changed
        # step 3: check
        if f == pow(y, 2, p):
            return ec.Point(curve, m, y)  # return the point
        m += 1


def curveDecode(Pm):
    m = int(Pm.x) // K  # convert Pm[0] into int type
    return m


text = "i ord() 返回 单字符 对应的 ascii码 。 chr() 返回 ascii码 对应的 单字符 "
b_text = text.encode()
print(b_text)
bs_text = b64.b64encode(b_text)
print(bs_text)
s = ''.join(bin(i).replace('0b', '') for i in bs_text[:2])
x = int(s, 2)
print(s)
print(x)
Pm1 = curveEncode(x)
print(Pm1)
print(curveDecode(Pm1))
# for k in range(0, 4096):
#     p = k * curve.g
#     print(f"{k} * G = ({p.x}, {p.y})")
# b_text = b64.b64decode(bs_text)
# print(b_text)
# text = b_text.decode('utf-8')
# print(text)
