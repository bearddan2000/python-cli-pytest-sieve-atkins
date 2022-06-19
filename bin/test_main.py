import pytest
import main

def test_SieveOfAtkin(capsys):
    main.SieveOfAtkin(5)
    captured = capsys.readouterr()
    assert captured.out == "2 3 "
