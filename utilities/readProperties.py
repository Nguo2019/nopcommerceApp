import configparser


config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class readConfig:
    @staticmethod  # this class can be accessed without creating any object
    def getAppURL():
        url=config.get('common info', 'baseurl')
        return url

    @staticmethod
    def getUserName():
        username=config.get('common info', 'username')
        return username

    @staticmethod
    def getPassWord():
        password=config.get('common info', 'password')
        return password


