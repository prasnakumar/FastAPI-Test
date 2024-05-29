import asyncio
import aiohttp
import time

async def fetch(session, url):
    start_time = time.perf_counter()
    try:
        async with session.get(url) as response:
            response.raise_for_status()  # Raise an exception for HTTP errors
            result = await response.json()
            end_time = time.perf_counter()
            duration = end_time - start_time
            return result, duration
    except aiohttp.ClientError as e:
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Request to {url} failed: {e}")
        return None, duration

async def main():
    start_total_time = time.perf_counter()
    
    async with aiohttp.ClientSession() as session:
        # First API call
        api1_url = 'https://jsonplaceholder.typicode.com/posts/1'
        print(f"Fetching API 1: {api1_url}")
        api1_response, api1_duration = await fetch(session, api1_url)
        print(f"API 1 execution time: {api1_duration:.4f} seconds")
        if api1_response is None:
            print("Failed to fetch API 1. Exiting.")
            return

        print(f"API 1 response: {api1_response}")

                                                                                                                                                          
        userId = api1_response['userId']
        api2_url = f"https://jsonplaceholder.typicode.com/posts?userId={userId}"
        print(f"Fetching API 2: {api2_url}")
        api2_response, api2_duration = await fetch(session, api2_url)
        print(f"API 2 execution time: {api2_duration:.4f} seconds")
        if api2_response is None:
            print("Failed to fetch API 2. Exiting.")
            return

        print(f"API 2 response: {api2_response[:2]}...")  # Print only the first 2 results to keep it concise

        # Third API call can run concurrently with the second API call
        api3_url = 'https://jsonplaceholder.typicode.com/users'
        print(f"Fetching API 3: {api3_url}")
        api3_task = asyncio.create_task(fetch(session, api3_url))

        # Await the completion of the third API call
        api3_response, api3_duration = await api3_task
        print(f"API 3 execution time: {api3_duration:.4f} seconds")
        if api3_response is None:
            print("Failed to fetch API 3. Exiting.")
            return

        print(f"API 3 response: {api3_response[:2]}...")  # Print only the first 2 results to keep it concise

    end_total_time = time.perf_counter()
    total_duration = end_total_time - start_total_time
    print(f"Total execution time: {total_duration:.4f} seconds")

# Run the main function
asyncio.run(main())
