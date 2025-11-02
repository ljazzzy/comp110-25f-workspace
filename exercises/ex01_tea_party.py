"""Program to plan the tea party by calculating supplies and cost."""

__author__: str = "730760217"


def main_planner(guests: int) -> None:
    """Entrypoint of the program: plan tea party supplies and cost."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Return the number of tea bags needed for the given number of guests."""
    return people * 2


def treats(people: int) -> int:
    """Return the number of treats needed for the given number of guests."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Return the total cost of the tea bags and treats combined."""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
