import logging

logging.basicConfig(level=logging.DEBUG)
# By default the level is Warning

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")


#debug < info < warning < error < critical