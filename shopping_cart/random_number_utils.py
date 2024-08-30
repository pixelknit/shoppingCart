import random
import string

class RandomUtils:
    """
    Class for generation of random numbers, it can create containers
    or single values.
    """
    @staticmethod
    def generate_random_id() -> str:
        """
        Generates a random ID number of length 6 as a string.
        """
        return "".join(random.choices(string.ascii_uppercase, k=6))

    def generate_random_int_in_range(self, x: int) -> int:
        """
        Generates a random number in a given range.

        Args:
            x: the range will start from 0 up until x
        Returns:
            A random integer value
        """
        return random.choice([0,x])

