import platform
import subprocess
import time
import datetime

# Target address (Google DNS usually reliable)
target = "8.8.8.8"

# Ping interval in seconds
interval = 10

# Log file name
log_file = "internet_log.txt"

# Detect the operating system
current_os = platform.system().lower()

# Set ping command parameters based on the operating system
if current_os.startswith("win"):
    ping_command = ["ping", "-n", "1", target]
else:
    ping_command = ["ping", "-c", "1", target]

def check_internet():
    result = subprocess.run(ping_command, stdout=subprocess.PIPE)
    return result.returncode == 0

def log_status(message):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {message}\n")

if __name__ == "__main__":
    # Record the start time
    start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Log that the test has started, including the start time
    log_status(f"Test started - Start Time: {start_time}")
    
    while True:
        internet_up = check_internet()
        if not internet_up:
            log_status("Internet connection lost!")
        time.sleep(interval)
