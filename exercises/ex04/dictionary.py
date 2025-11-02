"""Dictionary utility functions."""

__author__ = "730760217"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Return a dictionary with keys and values inverted."""
    result: dict[str, str] = {}
    for key, value in input_dict.items():
        if value in result:
            raise KeyError("Duplicate key when inverting!")
        result[value] = key
    return result


def favorite_color(favorites: dict[str, str]) -> str:
    """Return the color that appears most frequently."""
    color_counts: dict[str, int] = {}
    for color in favorites.values():
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    most_popular = ""
    highest_count = 0
    for name in favorites:
        color = favorites[name]
        if color_counts[color] > highest_count:
            most_popular = color
            highest_count = color_counts[color]
    return most_popular


def count(items: list[str]) -> dict[str, int]:
    """Return a dictionary counting how many times each string appears."""
    counts: dict[str, int] = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Categorize words by their starting letter."""
    result: dict[str, list[str]] = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter in result:
            result[first_letter].append(word)
        else:
            result[first_letter] = [word]
    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Add a student's attendance for a given day, avoiding duplicates."""
    if day not in attendance:
        attendance[day] = []
    if student not in attendance[day]:
        attendance[day].append(student)


