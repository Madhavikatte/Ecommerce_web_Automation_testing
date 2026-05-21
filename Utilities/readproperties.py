import configparser
# import os
config=configparser.ConfigParser()
# config_path = os.path.join(os.path.dirname("C:/Users/train\PycharmProjects/NopCommerceApp/Configurations/Config.ini"), 'Config.ini')
config.read("Configurations/Config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationurl():
        url=config['Default']['baseurl']
        return url
    @staticmethod
    def getusername():
        username=config['Default']['Username']
        return username
    @staticmethod
    def getpassword():
        password=config['Default']['Password']
        return password

