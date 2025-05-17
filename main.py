# Constants
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    bake_time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return bake_time_remaining

def preparation_time_in_minutes(layers):
    """Calculate the preparation time in minutes.

    :param layers: int - number of layers in the lasagna.
    :return: int - preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers and returns how many minutes
    the lasagna needs to be prepared based on the `PREPARATION_TIME`.
    """

    preparation_time = layers * PREPARATION_TIME
    return preparation_time


def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """Calculate the total elapsed time in minutes.

    :param layers: int - number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes).

    Function that takes the number of layers and the actual minutes the lasagna
    has been in the oven as arguments and returns how many minutes the lasagna
    has been cooking.
    """
    
    total_elapsed_time = preparation_time_in_minutes(layers) + elapsed_bake_time
    return total_elapsed_time

def main():
    """Main function to run the lasagna preparation and baking time calculations."""
    print("Welcome to Guido's Gorgeous Lasagna!"'\n'
    "Let's calculate the time needed for your lasagna.")
    layers = int(input("Enter the number of layers: "))
    elapsed_bake_time = int(input("Enter the elapsed bake time: "))

    print(f"Preparation time: {preparation_time_in_minutes(layers)} minutes")
    print(f"Elapsed time: {elapsed_time_in_minutes(layers, elapsed_bake_time)} minutes")
    print(f"Bake time remaining: {bake_time_remaining(elapsed_bake_time)} minutes")


if __name__ == "__main__":
    main()

