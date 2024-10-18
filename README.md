# IP-Blacklist-Checker

This script checks a list of IP addresses for malicious activity using asynchronous HTTP requests. It is designed to be fast and efficient by processing all non-private IPs concurrently.

## Features

- **Asynchronous Processing**: Utilizes `aiohttp` for faster API requests.
- **Color-Coded Output**: Uses ANSI escape sequences for color-coded output.
- **Result Sorting**: Sorts results based on malicious and suspicious counts.
- **Execution Time Measurement**: Measures and prints the total execution time.
- **Private IP Filtering**: Filters out private IP addresses.
- **Error Handling**: Handles invalid IPs and API request issues gracefully.

## Installation

To get started, install the required libraries:

```bash
pip install aiohttp termcolor
```

## Configuration

Create a `config.py` file in the same directory with your VirusTotal API key:

```python
VIRUSTOTAL_API_KEY = "your_virustotal_api_key_here"
```

## Usage

1. Save the script as `async-ip-checker.py` in your working directory.
2. Ensure `ip_list.txt` is in the same directory, with one IP address per line.
3. Run the script:

```bash
python async-ip-checker.py
```

## How It Works

- **IP List**: The script reads IP addresses from `ip_list.txt`.
- **Asynchronous Checks**: Each IP is checked for malicious activity asynchronously.
- **Output**: The results are displayed with color-coded output indicating the malicious and suspicious counts, and the total execution time is printed at the end.

## Example

Here's a simple example of how to run the script:

```bash
python async-ip-checker.py
```

The script will process the IPs asynchronously, display progress, and then show a sorted list of results with color-coding based on the malicious/suspicious counts.

## Sample Output

(Add your sample output here)

---

Feel free to customize this README further to suit your needs! If you have any other questions or need additional modifications, just let me know.
