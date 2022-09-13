from contextlib import contextmanager
from typing import IO, Generator


@contextmanager
def open_with_error(
    filename: str,
    mode: str = "r",
    encoding: str = 'utf8'
) -> Generator[tuple[IO, None] | tuple[None, IOError], None, None]:

    try:
        f = open( filename, mode, encoding=encoding )
    except IOError as err:
        yield None, err
    else:
        try:
            yield f, None
        finally:
            f.close()
