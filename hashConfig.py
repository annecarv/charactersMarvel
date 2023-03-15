import hashlib
import dotenv
import os
import datetime

dotenv.load_dotenv(dotenv.find_dotenv())

timeStamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')

privateKey = os.getenv('privateKey')
publicKey = os.getenv('publicKey')

def hashConfig():
    hashMd5 = hashlib.md5()
    hashMd5.update(f'{timeStamp}{privateKey}{publicKey}'.encode('utf-8'))
    hashConfig = hashMd5.hexdigest()

    return hashConfig

hashConfig()