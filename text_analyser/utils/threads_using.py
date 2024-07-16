import asyncio
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=10)


async def run_in_thread(func, *args, **kwargs):
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(executor, func, *args, **kwargs)
    return result
