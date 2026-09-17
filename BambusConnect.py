import subprocess
import datetime
import time


def ping(host):
    command = ['ping', '-n', '1', host]
    return subprocess.run(command, stdout=subprocess.DEVNULL).returncode == 0


host = "google.com"
log_file = "ping_log.txt"
check_Intervall = 1
failure_count = 0
failure_threshold = 2

while True:
    with open(log_file, 'a') as f:
        result = ping(host)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')   
        if not result:
            failure_count += 1
            if failure_count >= failure_threshold:
                f.write(f"{timestamp}: Ping to {host} failed for {failure_count} consecutive times\n")
        else:
            if failure_count > 0:
                f.write(f"\n")
            failure_count = 0
    time.sleep(check_Intervall)