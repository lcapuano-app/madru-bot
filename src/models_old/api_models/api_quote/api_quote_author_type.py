from typing import Any, TypedDict

from validators import ValidateProps


class ApiQuoteAuthorType ( TypedDict ):
    displayName : str
    idName      : str
    quoteName   : str


class ApiQuoteAuthorTypeValidator( ValidateProps ):

    def crash_invalid( data: Any, where: str = '' ) -> None:
        self = ApiQuoteAuthorTypeValidator

        self.exit_on_error( prop = 'displayName', obj = data, expected_type = str, where=where )
        self.exit_on_error( prop = 'idName',      obj = data, expected_type = str, where=where )
        self.exit_on_error( prop = 'quoteName',   obj = data, expected_type = str, where=where )


