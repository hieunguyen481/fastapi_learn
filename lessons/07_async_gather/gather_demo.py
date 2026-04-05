import asyncio


async def fetch_data_1():
    await asyncio.sleep(2)
    return "Data 1"


async def fetch_data_2():
    await asyncio.sleep(3)
    return "Data 2"


async def main():
    results = await asyncio.gather(fetch_data_1(), fetch_data_2())
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
