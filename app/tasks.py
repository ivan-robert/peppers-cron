import random
import logging

logger = logging.getLogger(__name__)




def print_result_hook(result):
    """
    Prints the result of the task.
    """
    print(f"Result: {result}")
    return result