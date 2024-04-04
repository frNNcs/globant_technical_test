from api.utils.helpers import convert_hour_to_human_redable


def test_convert_hour_to_human_redable():
    assert convert_hour_to_human_redable(1) == '1 hour'
    assert convert_hour_to_human_redable(2) == '2 hours'
    """
    assert convert_hour_to_human_redable(24) == '1 day'
    assert convert_hour_to_human_redable(48) == '2 days'
    assert convert_hour_to_human_redable(25) == '1 day and 1 hour'
    assert convert_hour_to_human_redable(26) == '1 day and 2 hours'
    assert convert_hour_to_human_redable(49) == '2 days and 1 hour'
    assert convert_hour_to_human_redable(50) == '2 days and 2 hours'
    assert convert_hour_to_human_redable(2.5) == '2 hours and 30 minutes'
    assert convert_hour_to_human_redable(24.5) == '1 day and 30 minutes'
    """
