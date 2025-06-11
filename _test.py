# test_app.py

import pytest

# --- Function to be tested (from your Streamlit app logic) ---
def power_calculations(n):
    return n**2, n**3, n**5

# --- Unit Test Cases ---
def test_positive_number():
    assert power_calculations(2) == (4, 8, 32)

def test_zero():
    assert power_calculations(0) == (0, 0, 0)

def test_negative_number():
    assert power_calculations(-3) == (9, -27, -243)

def test_large_number():
    result = power_calculations(10)
    assert result == (100, 1000, 100000)

def test_float_number():
    result = power_calculations(2.5)
    assert round(result[0], 2) == 6.25
    assert round(result[1], 2) == 15.62
    assert round(result[2], 2) == 97.66

# --- Code Quality Test using flake8 ---
def test_code_quality():
    """Run flake8 on the current file to ensure code style compliance."""
    import subprocess
    result = subprocess.run(
        ["flake8", __file__],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    assert result.returncode == 0, f"Flake8 issues found:\n{result.stdout}"
