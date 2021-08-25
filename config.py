import os
class Config:
    '''
    General configuration parent class
    '''
    
    SECRET_KEY = 'wadi'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://zawadi:wadi@localhost/blogs'

   

    # @staticmethod
    # def init_app(app):
    #     pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://zawadi:wadi@localhost/blogs'
    

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}