# test_example.py
import pytest

@pytest.fixture
def sample_data():
    return {"a": 1, "b": 2}

def test_sum(sample_data):
    assert sample_data["a"] + sample_data["b"] == 3