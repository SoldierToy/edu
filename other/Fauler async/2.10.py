import asyncio
from util.delay_functions import delay


async def hello_every_second():
    for i in range(5):
        await asyncio.sleep(1)
        print('пока я жду, исполняется другой код')


async def main():
    first_delay = asyncio.create_task(delay(3))
    two_delay = asyncio.create_task(delay(3))
    hello = asyncio.create_task(hello_every_second())
    await hello
    await first_delay
    await two_delay

asyncio.run(main())