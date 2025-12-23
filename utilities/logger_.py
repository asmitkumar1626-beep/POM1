import logging
def get_log(name=__name__):
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter=logging.Formatter('%(asctime)s-%(name)s-%(message)s')
    ch=logging.StreamHandler()
    fh=logging.FileHandler("logs.log")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger