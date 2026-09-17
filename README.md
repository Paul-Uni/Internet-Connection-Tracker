# Internet Connection Tracker

A small Python script that pings a host once per second and writes a log entry whenever
the connection drops. Built to answer one question: is my internet actually dropping out,
or does it just feel that way?

If you ever argued with your ISP about outages you could not prove, this is the minimum
amount of code that gives you something to point at.

## How it works

- Pings the target host (default `google.com`) every second using the system `ping` command
- Counts consecutive failures, and only logs once a configurable threshold is reached, so
  a single dropped packet does not fill the log
- Writes timestamped entries to `ping_log.txt` and inserts a blank line when the connection
  comes back, which makes outages easy to spot as blocks in the file

## Configuration

Everything is set at the top of the script:

| Setting | Default | Meaning |
|---------|---------|---------|
| `host` | `google.com` | Host to ping |
| `log_file` | `ping_log.txt` | Log output file |
| `check_Intervall` | `1` | Seconds between checks |
| `failure_threshold` | `2` | Consecutive failures before logging |

## Requirements

- Python 3
- Windows, because the ping command uses the `-n` flag. On Linux or macOS change it to `-c`.

## Run

```bash
python BambusConnect.py
```

Runs until you stop it with Ctrl+C.

## Example log

```
2026-03-14 21:04:11: Ping to google.com failed for 2 consecutive times
2026-03-14 21:04:12: Ping to google.com failed for 3 consecutive times

2026-03-14 22:47:05: Ping to google.com failed for 2 consecutive times
```

## Possible improvements

Kept deliberately simple. Things that would make it more useful:

- Log the moment the connection recovers and the total outage duration
- Cross platform ping flag detection
- CSV output for plotting downtime over a week
- Run as a background service instead of a foreground script
