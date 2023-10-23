import asyncio


async def busy_loop():
    for i in range(10):
        await nothing()


async def nothing():
    await asyncio.sleep(0)
    print('busy')


async def normal():
    for i in range(10):
        await asyncio.sleep(0)
        print('normal corutine')


async def main():
    # await asyncio.gather(busy_loop(), normal())

    f = asyncio.create_task(busy_loop())
    f1 = asyncio.create_task(normal())

    await f
    await f1


asyncio.run(main())
