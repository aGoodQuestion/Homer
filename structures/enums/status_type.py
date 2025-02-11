from enum import Enum

class StatusType(Enum):
    MESSAGE = "message"
    ERROR = "error"
    CONCLUDE_SUCCESS = "conclusion_success"
    CONCLUDE_FAILURE = "conclusion_failure"
