from pydantic import BaseModel

from phases.domain.domain_exception import DomainException


class Response(BaseModel):
    error_code: str
    message: str


class NotFoundResponse(Response):
    error_code: str
    message: str

    @staticmethod
    def status_code() -> int:
        return 404

    @staticmethod
    def get_content(exception: DomainException) -> dict[str, str]:
        return {"error_code": exception.error_code, "message": exception.message}
