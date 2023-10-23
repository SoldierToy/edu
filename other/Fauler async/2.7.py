import asyncio

from util.delay_functions import delay


async def add_one(number: int) -> int:
    return number + 1


async def hello_world_message():
    await delay(10)
    return 'Hello World!'


async def main():
    message = await hello_world_message()
    one_plus_one = await add_one(1)
    print(message)
    print(one_plus_one)


asyncio.run(main())
