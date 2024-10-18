import asyncio
import aiohttp
import ipaddress
from termcolor import colored
from config import VIRUSTOTAL_API_KEY
import os
import time

async def check_ip(ip, session):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {
        "accept": "application/json",
        "x-apikey": VIRUSTOTAL_API_KEY
    }
    try:
        async with session.get(url, headers=headers, ssl=False) as response:
            if response.status == 200:
                data = await response.json()
                malicious_count = data['data']['attributes']['last_analysis_stats']['malicious']
                return ip, malicious_count
            else:
                print(f"Error checking IP {ip}: HTTP {response.status}")
                return ip, None
    except Exception as e:
        print(f"Error checking IP {ip}: {str(e)}")
        return ip, None

async def process_ip_list(file_path):
    results = []
    
    print(f"Attempting to open file: {file_path}")
    try:
        with open(file_path, 'r') as file:
            ips = [line.strip() for line in file if line.strip()]
        print(f"Successfully opened file. Found {len(ips)} IP addresses.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return results
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return results
    
    ips = [ip for ip in ips if not ipaddress.ip_address(ip).is_private]
    
    async with aiohttp.ClientSession() as session:
        tasks = [check_ip(ip, session) for ip in ips]
        results = await asyncio.gather(*tasks)
    
    return results

def format_results(results):
    formatted_results = []
    for ip, malicious_count in results:
        if malicious_count is not None:
            if malicious_count >= 5:
                color = 'red'
            elif 1 <= malicious_count < 5:
                color = 'yellow'
            else:
                color = 'green'
            formatted_results.append(colored(f"IP: {ip}, Malicious Vendors: {malicious_count}", color))
        else:
            formatted_results.append(f"IP: {ip}, Error occurred during check")
    return formatted_results

async def main():
    start_time = time.time()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "ip_list.txt")
    
    print(f"Script directory: {script_dir}")
    print(f"Full file path: {file_path}")
    
    results = await process_ip_list(file_path)
    formatted_results = format_results(results)
    
    if formatted_results:
        for result in formatted_results:
            print(result)
    else:
        print("No results to display. Make sure 'ip_list.txt' exists in the same directory as this script and is not empty.")
    
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
