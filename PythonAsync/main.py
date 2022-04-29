import asyncio 

# Asynchronous operations and events occur simulatenously with the main program flow and does not rely on the main program to complete before executing
# Asynchronous / Await are typically used to fetch remote resources like json or other form of data from a database or file, wait for network requests, etc. 

# Coroutines are subroutines that allows execution of a some operation to be suspended and resumed while the program is running.
# The keyword async wraps around the function and returns a coroutine object. You must use the keyword 'await' to await the execution of this coroutine object, regardless of 
# success or failure. 
# Event loops allow us to write asynchronous code. By definition, an event loop waits for and dispatches events or messages in a program. 
async def main():
    print('jacob')
    task = asyncio.create_task(foo('sample text')) # Start executing as an async operation, while allowing the other program code to execute
    # await task # The first comment tag on this line will suspend the program until the async task finishes executing
    print('Async function foo is finished execution')
    
async def foo(text):
    print(text)
    await asyncio.sleep(1)
    
asyncio.run(main())
