from chapters.ch2.seasons import season


def test_seasons_input():
    season_output = season("winter")
    assert season_output == "snow"

def test_other_input():
    season_output = season("x")
    assert season_output == "I don't know that season"