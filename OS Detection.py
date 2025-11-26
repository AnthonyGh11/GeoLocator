import platform
import subprocess
import re

def ping_host(host):
    system = platform.system()
    if system == "Windows":
        cmd = ["ping", "-n", "1", host]
    else:  # Linux / macOS
        cmd = ["ping", "-c", "1", host]

    try:
        output = subprocess.check_output(cmd, universal_newlines=True)
        return output
    except subprocess.CalledProcessError:
        return None

def extract_ttl(ping_output):
    # Match TTL in ping output (TTL=128 or ttl=128)
    match = re.search(r"ttl=(\d+)", ping_output, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None

def detect_os(ttl):
    if ttl >= 255:
        return "Linux/Unix"
    elif ttl >= 128:
        return "Windows"
    elif ttl >= 64:
        return "macOS or Linux"
    else:
        return "Unknown OS"

# --- Main ---
host = input("Enter IP or hostname to ping: ")
ping_result = ping_host(host)

if ping_result:
    ttl = extract_ttl(ping_result)
    if ttl:
        os_guess = detect_os(ttl)
        print(f"Ping to {host} succeeded. TTL = {ttl} → Likely OS: {os_guess}")
    else:
        print("Ping succeeded, but TTL could not be extracted.")
else:
    print(f"Ping to {host} failed.")
