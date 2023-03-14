import hashlib

def hashConfig():
    hashMd5 = hashlib.md5()
    hashMd5.update(f'{timeStamp}{privateKey}{publicKey}'.encode('utf-8'))
    hashConfig = hashMd5.hexdigest()

    return hashConfig
