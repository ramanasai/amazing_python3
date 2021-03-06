# An async coroutine
import asyncio
import time

async def myf():
    print('Enter')
    time.sleep(2)
    print('Exit')

async def main():
    print('before')
    task = asyncio.create_task(myf())
    await(task) # runs immediately
    time.sleep(2) 
    print('after')

asyncio.run(main()) # with ()