#  Returns: true if s was converted successfully; otherwise, false.
def string_to_float(string: any) -> tuple:
    is_parser = False
    value = None

    # Check if is None:
    if string is not None:
        # Try to convert
        try:
            value = float(string)
            is_parser = True
        except:
            pass

    return is_parser, value
