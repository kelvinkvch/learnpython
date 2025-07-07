import asyncio
import threading


async def hello(name):
    print(f"Hello {name},{threading.current_thread}")
    await asyncio.sleep(1)
    print(f"Hallow {name},{threading.current_thread}")
    return name


async def main():
    l = await asyncio.gather(hello("Bob"), hello("alice"))
    # print()
    print(l)


asyncio.run(main())
