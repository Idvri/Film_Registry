import asyncio

from aiohttp import ClientSession

from src import start_parsing


async def main():
    """Основной скрипт парсера."""

    async with ClientSession() as session:
        await start_parsing(session)


if __name__ == '__main__':
    asyncio.run(main())
