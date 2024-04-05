from api.utils.helpers import convert_hour_to_human_redable


def test_convert_hour_to_human_redable():
    assert convert_hour_to_human_redable(0) == '0 seconds'
    assert convert_hour_to_human_redable(1) == '1 hour'
    assert convert_hour_to_human_redable(2) == '2 hours'
    assert convert_hour_to_human_redable(1.5) == '1 hour 30 minutes'
    assert convert_hour_to_human_redable(1.1) == '1 hour 6 minutes'
    assert convert_hour_to_human_redable(1.01) == '1 hour 36 seconds'
    assert convert_hour_to_human_redable(5.57) == '5 hours 34 minutes 12 seconds'
    assert convert_hour_to_human_redable(0.5) == '30 minutes'
    assert convert_hour_to_human_redable(0.1) == '6 minutes'
    assert convert_hour_to_human_redable(0.01) == '36 seconds'
