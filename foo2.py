import random

def generate_random_numbers(count, start, end):
    """
    Generate a list of random integers.

    Args:
        count (int): Number of random integers to generate.
        start (int): The lower bound of the range (inclusive).
        end (int): The upper bound of the range (inclusive).

    Returns:
        list: A list of random integers.
    """
    random_numbers = [random.randint(start, end) for _ in range(count)]
    return random_numbers

if __name__ == "__main__":
    # Example usage
    count = 5
    start = 1
    end = 10
    random_numbers = generate_random_numbers(count, start, end)
    print(f"Generated {count} random numbers between {start} and {end}: {random_numbers}")