from cProfile import run
import threading
from threading import Thread
import os
import PyCrypto

# GLOBAL VARIABLE
running = False
transationIncoming = []
transationVerified = []

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

    def __init__(self, publicKeyPath, privateKeyPath):
        print(1)
    
    def getPrivateKey(self, privateKey):
        return self.privateKey

    def getPublicKey(self, publicKey):
        return self.publicKey
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

#################################
class Crypto:

    def doWalletKeys(mainPath):
        print('YES')

if __name__ == "__main__":
    directory = Directory("C:\\Arus")
    print(1)
 

