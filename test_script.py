import os

# 1. Dummy sanity test to make sure CI always runs at least one test
def test_basic_math():
    assert 2 + 2 == 4

# 2. Test a function in a.py if it exists
try:
    from a import greet

    def test_greet_function():
        assert greet() == "Hello from Adithya Python inside Docker + Kubernetes!"

except ImportError:
    pass  # Skip this if greet() doesn't exist in a.py

# 3. Check that required datasets are present
def test_heart_csv_exists():
    assert os.path.isfile("heart.csv"), "heart.csv file is missing!"

def test_lungcancer_csv_exists():
    assert os.path.isfile("lungcancer.csv"), "lungcancer.csv file is missing!"
