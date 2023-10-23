import asyncio
import aiohttp


# class WriteToFile:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def __enter__(self):
#         self.file_object = open(self.filename, 'w')
#         return self.file_object
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.file_object:
#             self.file_object.close()


class AsyncSession:
    def __init__(self, url):
        self._url = url

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        response = await self.session.get(self._url)
        return response

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()


async def check(url):
    async with AsyncSession(url) as resp:
        html = await resp.text()
        return (f'{url}: {html[:20]}')


class ServerError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


async def server_returns_error():
    await asyncio.sleep(2)
    raise ServerError('Failed to get data')


async def main():
    async with asyncio.TaskGroup() as tg:
        print(type(tg))
        print(dir(tg))

        res = tg.create_task(check('https://www.youtube.com/'))
        res1 = tg.create_task(check('https://www.google.com/'))
        res2 = tg.create_task(check('https://www.dns.com/'))

    print(res.result())
    print(res1.result())
    print(res2.result())


asyncio.run(main())
