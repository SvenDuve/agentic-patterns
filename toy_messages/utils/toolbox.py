def add_numbers(a:int, b:int) -> int:
    """
    Adds two numbers together.

    Args:
        a: The first int.
        b: The second int.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b

def decide_to_play_lottery(p:float) -> bool:
    """
    Given a certain probability, decide to play the lottery or not.

    Args:
        p: The probability of winning.
    """
    if p > 0.7:
        return True
    else:
        return False
