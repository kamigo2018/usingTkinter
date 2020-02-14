import datetime
import random


class StrUtil():
    def __init__(self):
        pass
    
    @staticmethod
    def getDateStr():
        return str(datetime.datetime.now().date())
    
    @staticmethod
    def getTimeStr():
        return str(datetime.datetime.now())


class RandUtil():
    def __init__(self):
        pass
    @staticmethod
    def getRandWords():
        result = []
        len = random.randint(10,21)
        for i in range(len):
            c = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567890')
            result.append(c)
        return ''.join(result)
        