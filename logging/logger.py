# Logging is important when writing program output data 
# It's best practice to not use the root logger, and create your own logger as a module
import logging 
import sys
import FilterExample as InfoFilter
logging.basicConfig() # Sets the basic configuration for the logging messages. Takes 3 arguments by default: level= logging level, format= message format, datefmt= 
# formatted logging message date
import logger_helper as log_helper

# Sending logging messages to standard output using HTTP or some other method
logger = logging.getLogger(__name__)

# Create the logging handlers
stream_handler = logging.StreamHandler()

file_handler = logging.FileHandler('file.log')

# Set the handler level and format
stream_handler.setLevel(logging.WARNING) # Any logging level at warning and above is logged into the standard output stream  
file_handler.setLevel(logging.ERROR) # Any logging level at error and above is logged into the file

formatter = logging.Formatter(fmt='%(name)s ::  %(levelname)s :: %(message)s') 

# stream_handler.addFilter(InfoFilter()) Ensures only LOG level messages are written to stream and file

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning('This is a warning') # Logged to stream only
logger.error('Unique error message') # Logged to both stream and file

