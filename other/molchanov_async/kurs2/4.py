import asyncio


async def greet(time_out):
    await asyncio.sleep(time_out)
    return "Hello world"


async def main():
    long_task = asyncio.create_task(greet(6452))

    sec = 0
    while not long_task.done():
        await asyncio.sleep(1)
        sec += 1

        if sec == 5:
            long_task.cancel()

        print('Time passed', sec)

    try:
        await long_task

    except asyncio.CancelledError:
        print('Задача была отменана')

asyncio.run(main())
