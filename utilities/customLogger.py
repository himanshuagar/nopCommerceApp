import logging
import os

class LogGen():
    @staticmethod
    def loggen():
        print ("i am in Loggen function")
        log_dir="./Logs"
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        log_fie=os.path.join(log_dir,"automation.log")
        logging.basicConfig(filename=log_fie,
                            level=logging.INFO)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
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