import asyncio

async def main():
    print('tim')
    #foo('text')
    await foo('text')
    print('finished')

async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())