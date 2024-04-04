
def convert_hour_to_human_redable(hour: float) -> str:
    response : str = ''
    if hour > 24:
        response += f'{int(hour / 24)} day'
        if int(hour / 24) > 1:
            response += 's'
        if hour % 24 != 0:
            response += ' and '
    if hour % 24 != 0:
        response += f'{int(hour % 24)} hour'
        if int(hour % 24) > 1:
            response += 's'
    else:
        raise NotImplementedError()
    return response
