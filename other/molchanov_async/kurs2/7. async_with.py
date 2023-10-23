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
        print(f'{url}: {html[:20]}')


class ServerError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


async def server_returns_error():
    await asyncio.sleep(2)
    raise ServerError('Failed to get data')


async def main():
    coros = [
        check('https://www.youtube.com/'),
        check('https://www.google.com/'),
        check('https://www.dns.com/'),
    ]

    for coro in asyncio.as_completed(coros):
        print(type(coro))
        print('запуск coro1')
        res = await coro
        print('coro выполнена')
        print(res)



    # results = await asyncio.gather(*coros, return_exceptions=True)
    #
    # for res in results:
    #     print(res)


asyncio.run(main())
