import asyncio

async def fetch_data():
    print('Start fetching data')
    await asyncio.sleep(2)
    print('Done fetching data')
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)
        
async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())
    
    await task2
    value_of_task1 = await task1
    print(value_of_task1)

asyncio.run(main())