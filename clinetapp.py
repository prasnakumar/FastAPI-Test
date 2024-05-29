import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        api1_url = 'https://jsonplaceholder.typicode.com/posts/1'
        api1_data = await fetch(session, api1_url)
        print(f"API 1 Response: {api1_data}")

        userId = api1_data['userId']
        api2_url = f'https://jsonplaceholder.typicode.com/posts?userId={userId}'

        api2_data = await fetch(session, api2_url)
        print(f"API 2 Response: {api2_data[:2]}")

        api3_url = 'https://jsonplaceholder.typicode.com/users'
        api3_task = asyncio.create_task(fetch(session, api3_url))
        
        api3_data = await api3_task
        print(f"API 3 Response: {api3_data[:2]}")

asyncio.run(main())
