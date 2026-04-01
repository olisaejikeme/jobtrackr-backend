from typing import TypeVar, Optional
from http import HTTPStatus

from app.schemas.response_schema import ResponseSchema

T = TypeVar('T')


class ResponseUtils:
    """Utility functions for building standardized API responses."""

    @staticmethod
    def ok(message: str, data: T | None = None) -> ResponseSchema[T]:
        return ResponseSchema(
            message=message,
            status=True,
            status_code=HTTPStatus.OK.value,
            data=data
        )

    @staticmethod
    def created(message: str, data: T | None = None) -> ResponseSchema[T]:
        return ResponseSchema(
            message=message,
            status=True,
            status_code=HTTPStatus.CREATED.value,
            data=data
        )

    @staticmethod
    def no_content(message: str) -> ResponseSchema[None]:
        return ResponseSchema(
            message=message,
            status=True,
            status_code=HTTPStatus.NO_CONTENT.value,
            data=None
        )

    @staticmethod
    def bad_request(message: str, data: T | None = None) -> ResponseSchema[T]:
        return ResponseSchema(
            message=message,
            status=False,
            status_code=HTTPStatus.BAD_REQUEST.value,
            data=data
        )

    @staticmethod
    def unauthorized(message: str, data: T | None = None) -> ResponseSchema[T]:
        return ResponseSchema(
            message=message,
            status=False,
            status_code=HTTPStatus.UNAUTHORIZED.value,
            data=data
        )

    @staticmethod
    def forbidden(message: str, data: T | None = None) -> ResponseSchema[T]:
        return ResponseSchema(
            message=message,
            status=False,
            status_code=HTTPStatus.FORBIDDEN.value,
            data=data
        )

    @staticmethod
    def conflict(message: str, data: T | None = None) -> ResponseSchema[T]:
        return ResponseSchema(
            message=message,
            status=False,
            status_code=HTTPStatus.CONFLICT.value,
            data=data
        )

    @staticmethod
    def not_found(message: str, data: T | None = None) -> ResponseSchema[T]:
        return ResponseSchema(
            message=message,
            status=False,
            status_code=HTTPStatus.NOT_FOUND.value,
            data=data
        )

    @staticmethod
    def error(message: str, status: HTTPStatus, data: T | None = None) -> ResponseSchema[T]:
        return ResponseSchema(
            message=message,
            status=False,
            status_code=status.value,
            data=data
        )