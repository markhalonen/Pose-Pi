import configparser

config = configparser.ConfigParser()

config['params'] = {}
myParams = config['params']
myParams['id'] = '9917'
myParams['tag'] = '37a0e35e-c1f9-4af3-878b-932f4cae3844'
myParams['hw_type'] = 'pi'

with open('Specific/config.cfg', 'w') as configfile:
    config.write(configfile)
