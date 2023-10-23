import asyncio
from util.delay_functions import delay


async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    res = await sleep_for_three
    print(res)


asyncio.run(main())
