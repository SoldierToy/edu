import asyncio


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


async def coro_norm():
    return "Hello World"


async def coro_value_error():
    raise ValueError


async def coro_type_error():
    raise TypeError


async def main():
    try:
        res = await asyncio.gather(
            coro_norm(),
            coro_value_error(),
            coro_type_error(),
            return_exceptions=True
        )
    except ValueError as e:
        print(f"{e=}")
    except TypeError as e:
        print(f"{e=}")
    else:
        print(f'{res=}')

        # async with asyncio.TaskGroup() as tg:
        #     print(type(tg))
        #     print(dir(tg))
        #
        #     res = tg.create_task(check('https://www.youtube.com/'))
        #     res1 = tg.create_task(check('https://www.google.com/'))
        #     res2 = tg.create_task(check('https://www.dns.com/'))

        # print(res.result())
        # print(res1.result())
        # print(res2.result())


asyncio.run(main())
