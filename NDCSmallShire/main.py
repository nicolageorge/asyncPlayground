from scheduler import Scheduler, Task
from funx import (
    lucas,
    async_search,
    async_print_matches,
    is_prime,
    async_repetitive_message,
)


def run_lucas():
    scheduler = Scheduler()
    scheduler.add(async_search(lucas(), lambda x: len(str(x)) >= 6))
    scheduler.add(async_search(lucas(), lambda x: len(str(x)) >= 10))
    scheduler.run_to_completion()
    import pdb
    pdb.set_trace()


def run_isprime():
    scheduler = Scheduler()
    scheduler.add(async_print_matches(lucas(), is_prime))
    scheduler.run_to_completion()


def run_repetitive_messages():
    scheduler = Scheduler()
    scheduler.add(async_repetitive_message("You are wonderfull", 2))
    scheduler.add(async_print_matches(lucas(), is_prime))
    scheduler.run_to_completion()