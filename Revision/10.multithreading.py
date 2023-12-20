# Chapter 11: Concurrent and Parallel Programming

# Concurrent Programming with threading

import threading
import time


# Function to simulate a time-consuming task
def task(name, delay):
    print(f"{name} started")
    time.sleep(delay)
    print(f"{name} completed")


# Creating threads
thread1 = threading.Thread(target=task, args=("Task 1", 2))
thread2 = threading.Thread(target=task, args=("Task 2", 4))

# Starting threads
thread1.start()
thread2.start()

# Waiting for threads to finish
thread1.join()
thread2.join()

# Execution continues here after both threads finish
print("All tasks completed")

# Explanation:
# - The `task` function simulates a time-consuming task using `time.sleep`.
# - Two threads, `thread1` and `thread2`, are created to execute different tasks concurrently.
# - `start` method initiates the execution of threads.
# - `join` method ensures that the main program waits for threads to finish before proceeding.
