from enum import Enum, unique


@unique
class ServiceSignal(Enum):
    KEY_ERROR = 'KEY_ERROR'
    NO_FOUND = 'NO_FOUND'
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'


@unique
class ResponseSignal(Enum):
    NO_FOUND = 404
    SUCCESS = 200
    FAILED = 500
    DATA_MISSING = 401
