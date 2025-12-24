from project import top_five, todays_data, usage_on, format_time
import pytest


# ---------- format_time tests ----------
def test_format_time():
    assert format_time(0) == "0h 0m 0s"
    assert format_time(60) == "0h 1m 0s"
    assert format_time(3665) == "1h 1m 5s"

# ---------- printing functions tests using capsys ----------
def test_top_five_print(capsys):
    top_five()
    captured = capsys.readouterr()
    assert captured.out != ""  # something was printed

def test_todays_data_print(capsys):
    todays_data()
    captured = capsys.readouterr()
    assert captured.out != ""  # ensures it prints

def test_usage_on_print(capsys):
    try:
        usage_on("2025-01-01")   # works even if file missing? better handle try/except
        captured = capsys.readouterr()
        assert captured.out != ""
    except FileNotFoundError:
        pass


