import time
import signal
import os

print("Self destruction in:")
time.sleep(1)

for i in range(3, 0, -1):
	print(i)
	time.sleep(1)

print("Goodbye, world")

os.kill(os.getppid(), signal.SIGHUP)
