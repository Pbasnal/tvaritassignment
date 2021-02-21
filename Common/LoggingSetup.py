import logging

def SetupLogger():
    logging.basicConfig(filename="api.log",
                                format='%(asctime)s %(message)s',
                                filemode='w')

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    return logger

