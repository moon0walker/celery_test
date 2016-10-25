import logging
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)
logger.setLevel(logging.DEBUG)
fileFormatter = logging.Formatter( '[%(asctime)s] [pid:%(process)s] [%(funcName)s] [%(levelname)s]: %(message)s' )
fileHandler = logging.FileHandler('Tasks.log')
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(fileFormatter)
fileHandler.setFormatter(fileFormatter)
logger.addHandler(streamHandler)
logger.addHandler(fileHandler)
