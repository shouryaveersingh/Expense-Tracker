from project import load, save
import os

FILE = "expenses.json"


def setup_function():
    if os.path.exists(FILE):
        os.remove(FILE)


def test_load_empty():
    assert load() == []


def test_save_and_load():
    data = [{"name": "Coffee", "amount": 3.5, "category": "Food"}]
    save(data)
    assert load() == data


def test_multiple_entries():
    data = [
        {"name": "Coffee", "amount": 3.5, "category": "Food"},
        {"name": "Bus", "amount": 2.0, "category": "Transport"}
    ]
    save(data)
    result = load()

    assert len(result) == 2
    assert result[1]["category"] == "Transport"
