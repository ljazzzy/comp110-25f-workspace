__author__ = "730760217"  

from exercises.ex04.dictionary import invert

# --- Tests for invert ---
def test_invert_use_case_1() -> None:
    """Tests that invert correctly swaps keys and values in a normal dictionary."""
    test_dict = {"a": "1", "b": "2", "c": "3"}
    assert invert(test_dict) == {"1": "a", "2": "b", "3": "c"}


def test_invert_use_case_2() -> None:
    """Tests that invert works when there is only one key-value pair."""
    test_dict = {"x": "z"}
    assert invert(test_dict) == {"z": "x"}


def test_invert_edge_case_duplicate_values() -> None:
    """Tests that invert raises an error when duplicate values exist (values can't be keys)."""
    test_dict = {"a": "1", "b": "1"}
    try:
        invert(test_dict)
        assert False  # should not reach this point
    except KeyError:
        assert True


# --- Tests for favorite_color ---
def test_favorite_color_use_case_1() -> None:
    """Tests that favorite_color returns the color that appears most often."""
    colors = {"Alice": "blue", "Bob": "green", "Carmen": "blue"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_use_case_2() -> None:
    """Tests tie-breaking rule — returns first color in tie order."""
    colors = {"Alice": "red", "Bob": "red", "Carmen": "blue", "Dan": "blue"}
    assert favorite_color(colors) == "red"


def test_favorite_color_edge_case_empty_dict() -> None:
    """Tests that favorite_color returns an empty string when given an empty dictionary."""
    colors = {}
    assert favorite_color(colors) == ""


# --- Tests for count ---
def test_count_use_case_1() -> None:
    """Tests count on a normal list with repeated items."""
    items = ["a", "b", "a", "c"]
    assert count(items) == {"a": 2, "b": 1, "c": 1}


def test_count_use_case_2() -> None:
    """Tests count on a list with all unique elements."""
    items = ["x", "y", "z"]
    assert count(items) == {"x": 1, "y": 1, "z": 1}


def test_count_edge_case_empty_list() -> None:
    """Tests count on an empty list."""
    items = []
    assert count(items) == {}


# --- Tests for alphabetizer ---
def test_alphabetizer_use_case_1() -> None:
    """Tests that alphabetizer groups words by first letter correctly."""
    words = ["apple", "banana", "avocado"]
    assert alphabetizer(words) == {"a": ["apple", "avocado"], "b": ["banana"]}


def test_alphabetizer_use_case_2() -> None:
    """Tests that alphabetizer handles mixed case letters by lowercasing them."""
    words = ["Apple", "banana", "Avocado"]
    assert alphabetizer(words) == {"a": ["Apple", "Avocado"], "b": ["banana"]}


def test_alphabetizer_edge_case_empty_list() -> None:
    """Tests that alphabetizer returns an empty dict when given an empty list."""
    assert alphabetizer([]) == {}


# --- Tests for update_attendance ---
def test_update_attendance_use_case_1() -> None:
    """Tests that update_attendance adds a student correctly."""
    attendance = {"Monday": ["Alice"]}
    update_attendance(attendance, "Monday", "Bob")
    assert attendance == {"Monday": ["Alice", "Bob"]}


def test_update_attendance_use_case_2() -> None:
    """Tests that update_attendance creates a new key if day doesn’t exist."""
    attendance = {"Monday": ["Alice"]}
    update_attendance(attendance, "Tuesday", "Bob")
    assert attendance == {"Monday": ["Alice"], "Tuesday": ["Bob"]}


def test_update_attendance_edge_case_duplicate_student() -> None:
    """Tests that update_attendance doesn’t add duplicates if student already present."""
    attendance = {"Monday": ["Alice"]}
    update_attendance(attendance, "Monday", "Alice")
    assert attendance == {"Monday": ["Alice"]}

    with pytest.raises(KeyError):
        my_dictionary = {'alyssa': 'byrnes', 'adam': 'byrnes'}
        invert(my_dictionary)