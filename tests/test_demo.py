import pytest

from dvla_regdb.demo import demo


def test_demo(capsys: pytest.CaptureFixture[str]) -> None:
    demo()
    out = capsys.readouterr().out
    assert "There are 3 registrations" in out
    assert "Registration AB01 CDE  Year 2001 Id 12345" in out
    assert "Registration AB01 CDE has Id 12345" in out
    assert "Registration FG02 HJK has Id 67890" in out
    assert "Registration L33T H4X0R has Id Unassigned" in out
