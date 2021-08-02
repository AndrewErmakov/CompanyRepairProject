def get_date_separator(date):
    separators = './-'
    for symbol in date:
        if symbol in separators:
            return symbol
