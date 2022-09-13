import datetime


def get_timestamp_filename( filename: str = 'file', ext: str = 'log', pos: str = 'L'  ) -> str:

    if pos != 'L' and pos != 'R':
        raise TypeError('Position must be "L" (left) or "R" (rigth).')

    timestamp = str( datetime.datetime.now() )
    date_str = timestamp[0:10]

    if pos == 'R':
        return f"{filename}-{date_str}.{ext}"
    else:
        return f"{date_str}-{filename}.{ext}"