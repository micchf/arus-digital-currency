from cProfile import run
import threading
from threading import Thread
import os
from Crypto.PublicKey import RSA
import time

time.clock = time.time

# GLOBAL VARIABLE
running = False
transationIncoming = []
transationVerified = []

#################################

def doWalletKeys(walletPath):
    privateKey = RSA.generate(1024)
    publicKey = privateKey.publickey()
    f = open(walletPath + os.sep + "privateKey.pem",'wb')
    f.write(privateKey.export_key('PEM'))
    f.close()
    f = open(walletPath + os.sep + "publicKey.pem",'wb')
    f.write(publicKey.export_key('PEM'))
    f.close()
    return privateKey, publicKey


def getWalletKeys():
        print('YES')
    
#################################

#################################
class Console(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global running
        while running:
            inputData = input()
            if inputData == "1":
                running = False

#################################

#################################
class Wallet:
    publicKey = None
    privateKey = None
    publicKeyEncoded = None
    privateKeyEncoded = None

    def __init__(self, privateKey, publicKey):
        self.privateKey = privateKey
        self.publicKey = publicKey
    
    def getPrivateKey(self):
        return self.privateKey

    def getPublicKey(self):
        return self.publicKey
    
    def getPrivateKeyEncoded(self):
        return self.privateKeyEncoded

    def getPublicKeyEncoded(self):
        return self.publicKeyEncoded
#################################

#################################
class Client:
    version = None

    def __init__(self, version):
        self.version = version
    
    def getVersion(self):
        return self.version
#################################

#################################
class Directory:
    mainPath = None
    blockchainPath = None
    walletPath = None
    infoFilePath = None

    def __init__(self, mainPath):
        if os.path.isdir(mainPath):
            self.mainPath = mainPath
        else:
            os.mkdir(mainPath)
        if os.path.isdir(mainPath + os.sep + "blocks"):
            self.blockchainPath = mainPath + os.sep + "blocks"
        else:
            os.mkdir(mainPath + os.sep + "blocks")
        if os.path.isdir(mainPath + os.sep + "wallet"):
            self.walletPath = mainPath + os.sep + "wallet"
        else:
            os.mkdir(mainPath + os.sep + "wallet")
        if os.path.isfile(mainPath + os.sep + "info.json"):
            self.walletPath = mainPath + os.sep + "info.json"
        else:
            print('Make info File')
    
    def getMainPath(self):
        return self.mainPath
    def getBlockChainPath(self):
        return self.blockchainPath
    def getWalletPath(self):
        return self.walletPath
    def getInfoFilePath(self):
        return self.infoFilePath
#################################

if __name__ == "__main__":
    directory = Directory("C:\\Arus")
    WalletUser = None
    if os.path.isfile(directory.getWalletPath() + os.sep + "privateKey.pem"):
        getWalletKeys()
    else:
        privateKey, publicKey = doWalletKeys(directory.getWalletPath())
        WalletUser = Wallet(privateKey, publicKey)
        print(type(WalletUser.getPrivateKey()))

 

