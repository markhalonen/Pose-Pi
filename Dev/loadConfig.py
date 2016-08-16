import configparser
config = configparser.ConfigParser()
configPath = 'Specific/config.cfg'
config.read(configPath)
print(config['params']['id'])
