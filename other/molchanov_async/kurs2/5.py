import asyncio


async def greet(time_out):
    await asyncio.sleep(time_out)
    return "Hello world"


async def main():
    long_task = asyncio.create_task(greet(5))

    try:
        res = await asyncio.wait_for(asyncio.shield(long_task), 5)
    except asyncio.TimeoutError:
        print('Задача была отменена')
        res = await long_task
        print(res)

asyncio.run(main())
