"""EX02 - Wordle"""

__author__ = "730760217"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def input_guess(expected_length: int) -> str:
    """Prompt the user for a guess of the correct length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def contains_char(word_search: str, single_character: str) -> bool:
    """Return True if single_character is found in word_search."""
    assert len(single_character) == 1, f"len('{single_character}') is not 1"
    i: int = 0
    while i < len(word_search):
        if word_search[i] == single_character:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Return emoji string showing which letters are correct or misplaced."""
    assert len(guess) == len(secret), "Guess and secret must be the same length."
    result: str = ""
    i: int = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i += 1
    return result    


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    won: bool = False
    while turn <= 6 and not won:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            won = True
        else:
            turn += 1
    if not won:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
