import asyncio


# Asynchronous Programming: a type of programming that the code isn't executed in order,
# that means that we can run more than one function in one time, like background process

# Coroutines: asynchronous functions
# Await: execute coroutines inside coroutines
# asyncio.run(): executes coroutines OUTSIDE other coroutine
# asyncio.create_task(): a function that will be executed when nothing is executing

async def hello(text):
    print(text)


async def save():
    print('saving...')

asyncio.run(hello('Léo'))


async def double_hello(text):
    print(f'Hi {text}')
    await asyncio.sleep(1)
    await hello('Léo')
    task = asyncio.create_task(save())
    await asyncio.sleep(10)


asyncio.run(double_hello('Léo'))





