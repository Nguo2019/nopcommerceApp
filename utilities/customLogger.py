import logging


class logGen:
    @staticmethod
    def loggen():
        #1 youtube viewer`s  method works

        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename=".\\Logs\\automation.log", mode='a')
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger

        """
        # 2  Teacher`s method doesnot work
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            filemode='a'
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
        """
