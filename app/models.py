#-*- coding:utf-8 -*-
import datetime
from werkzeug.security import generate_password_hash,check_password_hash


# 乐器
# author:hyb


class Instrument:

    def __init__(self, name, price, weight, description, transportation, imagePath):
        self.__Name = name
        self.__Price = price
        self.__Weight = weight
        self.__Description = description
        self.__Transportation = transportation
        self.__ImagePath = imagePath

    def getName(self):
        return self.__Name

    def getPrice(self):
        return self.__Price

    def getWeight(self):
        return self.__Weight

    def getDescription(self):
        return self.__Description

    def getTransportation(self):
        return self.__Transportation

    def getImagePath(self):
        return self.__ImagePath

    def saveToDb(self):
        pass

    def modify(self, **kwargs):
        pass


# 购物车
# author:hyb
class ShoppingCraft:

    def __init__(self,*args):
        self.__Instruments = list(args)
        self.__TotalPrice = sum([instrument.getPrice()
                                 for instrument in self.__Instruments])

    def getAllInstruments(self):
        return self.__Instruments

    def getTotalPrice(self):
        return self.__TotalPrice

    def pay(self,username,*args):
        pass

    def payAll(self,username):
        pass

    def remove(self,*args):
        pass

    def removeAll(self):
        pass


# 订单
# author:hyb
class Order:

    def __init__(self,*args):
        self.__Instruments = list(args)
        self.__DateTime = datetime.datetime.now()
        self.__TotalPrice = sum([instrument.getPrice()
                                 for instrument in self.__Instruments])

    def getAllInstruments(self):
        return self.__Instruments

    def getDateTime(self):
        return self.__DateTime

    def getTotalPrice(self):
        return self.__TotalPrice


# 用户
# author:hyb
class User:

    def __init__(self,username,password):
        self.__username = username
        self.__password_hash = generate_password_hash(password)
        self.__shoppingCraft = ShoppingCraft()

    def getUsername(self):
        return self.__username

    def payShoppingCraft(self,*args):
        self.__shoppingCraft.pay(self.__username,*args)

    def payAllShoppingCraft(self):
        self.__shoppingCraft.pay(self.__username)

    def removeShoppingCraft(self,*args):
        self.__shoppingCraft.remove(*args)

    def removeAllShoppingCraft(self):
        self.__shoppingCraft.removeAll()

    def saveToDb(self):
        from .dbConnect import get_cursor
        cur = get_cursor()
        try:
            if cur.execute('INSERT INTO user(username,password_hash) VALUES("%s","%s")'
                    ,(self.__username,self.__password_hash)):
                cur.connection.commit()
                return True
            else:
                return False
        except BaseException as e:
            return False

    