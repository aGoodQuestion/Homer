from util.singleton_meta import SingletonMeta
from loguru import logger
from structures.enums import StatusType


class Status(metaclass=SingletonMeta):
    def __init__(self):
        self.status_box = None

    def initialize(self, status_box):
        self.status_box = status_box

    def update(self, type: StatusType, message: str = None):
        if type == StatusType.MESSAGE:
            if self.status_box:
                self.status_box.write(message)
            else:
                logger.info(message)
        elif type == StatusType.CONCLUDE_SUCCESS:
            if self.status_box:
                self.status_box.update(label=message, state="complete", expanded=False)
            else:
                logger.success(message)
        elif type == StatusType.CONCLUDE_FAILURE:
            if self.status_box:
                self.status_box.update(label=message, state="error", expanded=False)
            else:
                logger.error(message)
        elif type == StatusType.ERROR:
            if self.status_box:
                self.status_box.error(message)
            else:
                logger.error(message)
