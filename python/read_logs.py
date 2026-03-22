from db import read_logs

logs = read_logs()

for log in logs:
    print(log)