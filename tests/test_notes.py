import pytest

import sightreading.randnotes as s

def test_diatonic():
    assert s.is_sharp(("A#2", 5))
    assert s.is_flat(("Bb3", 3))

def test_frets():
    assert s.fretnote(6, 0) == ["E2"]
    assert set(s.fretnote(1, 2)) == set(["F#4", "Gb4"])

def test_padding():
    notes = ["C2"] * 7
    s.pad_line(notes, start=True, end=True)

    assert notes == ["treble-clef", "time-signature", "C2", "C2", "C2", "C2", "bar", "C2", "C2", "C2", "rest", "double-bar"]

def test_staff_dim():
    lines = s.rand_staff([1], range(13), 1, 2, False)
    
    assert len(lines) == 2
    assert lines[0][-1] == "end-bar"
    assert lines[1][6] == "bar"
    assert lines[1][8] == "rest"
