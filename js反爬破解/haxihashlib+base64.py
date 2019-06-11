# #-*-coding:utf-8-*-
# import hashlib,random,hmac
# #各种摘要算法，位数越多数据越安全，不过加密的时候就越慢
# #加salt..如果遇到相同口令的，可以把用户名也加进去加密
# salt= ''.join([chr(random.randint(48, 122)) for i in range(20)])
#
# #MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
# md5 = hashlib.md5()
# md5.update(('阿牛喔'+salt).encode('utf-8'))
# print(md5.hexdigest())
#
# #SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
# sha1 = hashlib.sha1()
# sha1.update(('阿牛喔'+salt).encode('utf-8'))
# print(sha1.hexdigest())
#
# #SHA256的结果是256 bit字节，通常用一个64位的16进制字符串表示。
# sha256 = hashlib.sha256()
# sha256.update(('阿牛喔'+salt).encode('utf-8'))
# print(sha256.hexdigest())
#
# #hmac算法
# print(hmac.new(salt.encode('utf-8'), '阿牛喔'.encode('utf-8'), 'MD5').hexdigest())
#

# -*- coding: utf-8 -*-
import hashlib, random,hmac,base64

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    #验证相同password+salt，在hashlib和hmac会不会得到相同哈希，答案是不能，两者内部原理不一样
    print(get_md5(password+user.salt))
    h=hmac.new(user.salt.encode('utf-8'), password.encode('utf-8'), 'MD5').hexdigest()
    print(h)
    #变成base64编码，128bit（md5)就是16个8bit字节或者32个4bit字节，变成base64成为192bit就是24个8bit字节
    #实际中可能将password+salt用base64加密，再用哈希加密
    f = base64.b64encode(hmac.new(user.salt.encode('utf-8'), password.encode('utf-8'), 'MD5').digest())
    print(f)
    #base64解码
    F=base64.b64decode(f)
    print(F)
    return user.password == get_md5(password+user.salt)

print(login('michael', '123456'))
