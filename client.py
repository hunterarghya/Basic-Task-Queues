import time

from worker import mail_task

time.sleep(2)


print ("submitting task...")
task = mail_task.delay("arghya07cse@gmail.com")

while not task.ready():
    print("Task state:", task.state)
    time.sleep(1)

print("RESULT =", task.get())