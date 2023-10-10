#!/usr/bin/env python3
"""Task 0"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """random number for a seconds"""

    time_wait = random.random() * max_delay
    await asyncio.sleep(time_wait)
    return time_wait
