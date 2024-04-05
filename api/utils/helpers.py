import math


def convert_hour_to_human_redable(hours: float) -> str:
    if hours <= 0:
        return '0 seconds'

    aux_response = ''
    hours_aux = math.trunc(hours)

    minutes = (hours - hours_aux) * 60
    minutes_aux = math.trunc(minutes)

    seconds = (minutes - minutes_aux) * 60
    seconds_aux = math.trunc(seconds)

    if hours_aux:
        aux_response += f"{hours_aux} hour"
        if hours_aux > 1:
            aux_response += 's'
        aux_response += ' '

    if minutes_aux:
        aux_response += f"{minutes_aux} minute"
        if minutes_aux > 1:
            aux_response += 's'
        aux_response += ' '

    if seconds_aux:
        aux_response += f"{seconds_aux} second"
        if seconds_aux > 1:
            aux_response += 's'

    if aux_response[-1] == ' ':
        aux_response = aux_response[:-1]

    return aux_response
