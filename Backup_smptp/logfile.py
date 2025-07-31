import logging

logging.basicConfig(
      filename = 'app.log',
      filemode = 'a', #a stands for append
      level = logging.DEBUG,
      format = '%(asctime)s - %(levelname)s - %(message)s'

)


logging.debug("Debug info")
logging.info("Processing started")
logging.warning("Something is wrong")
logging.error("Data process failed")
logging.critical("System Crash!")

