import random
import logging

logger = logging.getLogger(__name__)


def log_random_number():
    """
    Logs a random number between 1 and 10.
    This function is called every 5 minutes by django-q scheduler.
    """
    random_number = random.randint(1, 10)
    logger.info(f"Random number generated: {random_number}")
    print(f"Random number generated: {random_number}")
    return random_number

