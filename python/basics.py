import asyncio 
import time 

# Co-routine that is awaitable. async keyword creates a co-routine
async def say_hello(runtype):
    print('Hello Started...') 
    if runtype == 'asyncio':    # Test if requesting asyncio style.
        await asyncio.sleep(1) 
    else:
        time.sleep(1)       # Blocking code. No advantage of async here. 
    print('...Hello Ended.') 

async def say_world(runtype):
    print('World started...') 
    if runtype == 'asyncio':
        await asyncio.sleep(2) 
    else: 
        time.sleep(2)       # Blocking functions are not aware of Event Loop.
    print('...World ended.')

async def main(flag='asyncio'):
    # Create the tasks 
    t1 = asyncio.create_task(say_hello(flag))
    t2 = asyncio.create_task(say_world(flag))

    # Await them
    await t1 
    await t2

if __name__ == '__main__':
    x = input("Use time.sleep? Reply 'y' if you want to run time.sleep: ") 
    start = time.time()
    if x == 'y':
        asyncio.run(main(x)) 
    else:
        asyncio.run(main())
    end = time.time()
    print(f'[+] Time taken = {end - start:.2f}')