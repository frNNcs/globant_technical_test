
def convert_hour_to_human_redable(hour: float) -> str:
    if hour > 24:
        return f"{hour // 24} days and {hour % 24} hours"
    else:
        return f"{hour} hours"
