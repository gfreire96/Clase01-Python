import logging

class LoggerBase:
    @staticmethod
    def configurar():
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        return logging.getLogger()

log = LoggerBase.configurar()
