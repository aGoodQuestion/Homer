from util.singleton_meta import SingletonMeta
from loguru import logger
from structures.enums import StatusType


class Status(metaclass=SingletonMeta):
    def __init__(self):
        self.status_box = None

    def initialize(self, status_box):
        self.status_box = status_box

    def update(self, type: StatusType, message: str, tabs=0):
        message_padded = self._generate_tabs(tabs) + message
        if type == StatusType.MESSAGE:
            if self.status_box:
                self.status_box.write(message_padded)
            else:
                logger.info(message_padded)
        elif type == StatusType.CONCLUDE_SUCCESS:
            if self.status_box:
                self.status_box.update(label=message_padded, state="complete", expanded=False)
            else:
                logger.success(message_padded)
        elif type == StatusType.CONCLUDE_FAILURE:
            if self.status_box:
                self.status_box.update(label=message_padded, state="error", expanded=False)
            else:
                logger.error(message_padded)
        elif type == StatusType.ERROR:
            if self.status_box:
                self.status_box.error(message_padded)
            else:
                logger.error(message_padded)

    def _generate_tabs(self, tabs: int) -> str:
        if self.status_box:
            return f"{'&nbsp;' * 5 * tabs}"
        else:
            return f"{'\t' * tabs}"