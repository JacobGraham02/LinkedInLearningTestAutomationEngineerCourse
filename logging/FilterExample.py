import logging

class InfoFilter(logging.Filter):
    
    # Only logs records which the function evaluates to true. That is, only the records that have an info logging level. 
    def filter(self, record):
        return record.levelno == logging.INFO # Constant evaluates to integer   