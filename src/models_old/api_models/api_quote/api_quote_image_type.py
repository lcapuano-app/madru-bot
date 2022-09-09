from typing import Any, TypedDict

from validators import ValidateProps


class ApiQuoteImageType ( TypedDict ):
    sm : str
    qt : str


class ApiQuoteImageTypeValidator( ValidateProps ):

    def crash_invalid( data: Any, where: str = '' ) -> None:
        self = ApiQuoteImageTypeValidator

        self.exit_on_error( prop = 'sm', obj = data, expected_type = str, where=where )
        self.exit_on_error( prop = 'qt', obj = data, expected_type = str, where=where )
