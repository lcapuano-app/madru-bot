def get_int_decimal_size( val: int ) -> int:

    try: 
        # We will add zeros to form tens, hundreds, etc...
        acc: list[str] = ['1']

        # Int str representation
        val_str: str = str( val )

        # Adds zeros to acc
        for _ in val_str: 
            acc.append('0')

        acc.pop()

        # Joins acc to string, then casts to an int
        size = int( ''.join( acc) )

        return size
    
    except Exception:
        return 1