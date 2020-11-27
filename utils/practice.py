import asyncio
import time


async def test():
    start_time = time.time()
    print('hello')
    await asyncio.sleep(1)
    print('world')
    end_time = time.time()
    print('spend: %ss' % (end_time - start_time))


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    start_time = time.time()
    task1 = asyncio.create_task(
        say_after(1, 'hello1'))

    task2 = asyncio.create_task(
        say_after(2, 'world1'))

    await task1
    await task2
    end_time = time.time()
    print('spend: %ss' % (end_time - start_time))

if __name__ == '__main__':
    asyncio.run(test())
    asyncio.run(main())
