import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time
import os
from Fletcher import Fletcher64

time.clock = time.time

class Wallet:
    publicKey = None
    privateKey = None
    publicKeyEncoded = None
    privateKeyEncoded = None

    def __init__(self, walletPath):
        self.publicKey = RSA.importKey(open(walletPath + os.sep + "publicKey.pem").read())
        self.privateKey = RSA.importKey(open(walletPath + os.sep + "privateKey.pem").read())
        self.publicKeyEncoded = self.publicKey.exportKey()
        self.privateKeyEncoded = self.privateKey.exportKey()
        fletcher = Fletcher64()
        fletcher.update(self.publicKeyEncoded.decode('ascii'))
        self.publicKeyEncoded = str(fletcher.hexdigest())
        fletcher.update(self.privateKeyEncoded.decode('ascii'))
        self.privateKeyEncoded = str(fletcher.hexdigest())
        print(self.privateKeyEncoded)
        fletcher2 = Fletcher64()
        fletcher2.update(self.publicKey.exportKey().decode('ascii'))
        print(fletcher2.hexdigest())
    
    def sign(self, msg):
        msgEncoded = str.encode(msg)
        encrypt = PKCS1_OAEP.new(self.publicKey).encrypt(msgEncoded)
        s = binascii.hexlify(encrypt)
        fletcher = Fletcher64()
        fletcher.update(s)
        return fletcher.hexdigest()


d = Wallet("C:\\Users\\MiccPC\Desktop")
print(d.sign('prova'))