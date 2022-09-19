import datetime


def get_timestamp_filename( filename: str = 'file', ext: str = 'log', pos: str = 'L'  ) -> str:
    """ 
    Adds a timestamp (ignores millis) to a `filename`.

    It can be on start `pos = 'L'` or end `pos = 'R'`

    ::param::filename: file name `default` file
    ::param::ext: file extension `default` log
    ::param::pos: timestamp position `default` L

    ::returns:: str
    """

    timestamp = str( datetime.datetime.now() )
    date_str = timestamp[0:10]

    if pos == 'R':
        return f"{filename}-{date_str}.{ext}"
    else:
        return f"{date_str}-{filename}.{ext}"