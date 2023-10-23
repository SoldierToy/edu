import asyncio
from util.delay_functions import delay


async def main():
    s1 = asyncio.create_task(delay(3))
    s2 = asyncio.create_task(delay(3))
    s3 = asyncio.create_task(delay(3))


    await s1
    print('---')
    await s2
    print('---')
    await s3
    print('---')


asyncio.run(main())
