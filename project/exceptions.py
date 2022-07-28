class BaseServiceError(Exception):
    code = 500


class ItemNotFound(BaseServiceError):
    code = 404


class InvalidToken(BaseServiceError):
    code = 403


class IncorrectPassword(BaseServiceError):
    code = 403
