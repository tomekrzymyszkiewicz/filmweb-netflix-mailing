import configparser

def load_config(file_name):
    config = configparser.ConfigParser()
    config.read(file_name)
    sender = {"mail": config['sender']['mail'], "password": config['sender']['password']}
    receivers = []
    for receiver in config['receivers'].values():
        receivers.append(receiver)
    return sender, receivers
