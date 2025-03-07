from run_timing import run_timing


def test_run_timing(monkeypatch, capsys):
    inputs = iter(["30", "40", ""])  # predefined answers
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))

    run_timing()

    captured = capsys.readouterr().out
    assert "Average running time: 35.0" in captured
    assert "Total runs: 2" in captured


def test_run_timing2(monkeypatch, capsys):
    inputs = iter(["10", "15", "5", ""])  # predefined answers
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))

    run_timing()

    captured = capsys.readouterr().out
    assert "Average running time: 10.0" in captured
    assert "Total runs: 3" in captured
