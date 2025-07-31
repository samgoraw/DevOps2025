import logging

#With Logger Name
logger = logging.getLogger("Sam_Gourav")

logging.basicConfig(level=logging.DEBUG)


logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message") 


#debug < info < warning < error < critical 