import asyncio

async def say_hello():
    print("Start")
    await asyncio.sleep(2)
    print("End")
    return "Hello"

async def main():
    result = await say_hello()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())