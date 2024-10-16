# Readers-Writers Problem

This project implements a solution for the classic Readers-Writers Problem, simulating multiple readers and writers accessing a shared resource (in this case, a variable) using Python's threading and synchronization mechanisms.

## Problem Description

In database management systems (DBMS), multiple users can either read from or write to a shared resource (such as a database). The goal of the Readers-Writers Problem is to allow multiple readers to read from the shared resource concurrently while ensuring that only one writer can modify the resource at any given time.

### Synchronization overview:
In this solution, synchronization mechanisms (locks and conditions) are used to solve the problem of concurrent access to a shared resource:

- **Multiple Readers**: Can access the resource simultaneously without blocking each other.
- **Writers**: Require exclusive access to the resource, meaning they must wait until there are no active readers or writers.
- **Reader-Writer Coordination**: The combination of locks and conditions ensures that when a writer wants to write, it waits for readers to finish, and once a writer has access, readers are blocked until the writer finishes.

This synchronization strategy prevents **race conditions** (multiple threads modifying or accessing the resource at the same time) and ensures data consistency.

### Key Requirements:
- Multiple readers can access the resource simultaneously without conflicts.
- Writers require exclusive access to the resource, meaning only one writer can modify the resource at a time.
- Synchronization mechanisms (locks and conditions) are used to ensure the proper coordination between readers and writers.

## Solution Overview

This Python implementation uses:
- **Locks** to ensure exclusive access to the shared resource for writers and manage reader access.
- **Condition variables** to manage waiting writers, ensuring writers get access only when no readers are using the resource.

### Synchronization Mechanisms Used:

**1. Locks:**
   - **Readers Lock (`readers_lock`)**: This lock is used to ensure that readers can safely increment and decrement the count of active readers. When the first reader accesses the resource, the readers lock ensures that the writer cannot access the resource at the same time. If more readers arrive while a reader is already reading, they can proceed without interruption.
   
   - **Writers Lock (`writers_lock`)**: This lock ensures that only one writer can access the shared resource at a time. When a writer acquires this lock, no other readers or writers can access the resource until the writer has finished.

**2. Condition Variables:**
   - **Write Waiting (`write_waiting`)**: This condition variable is used to put writers in a waiting state if the resource is currently being accessed by readers. It prevents writers from "jumping in" while there are active readers. Once the resource becomes available (i.e., no readers), a writer can proceed and modify the resource.


## Code Breakdown

- **`WriterReaderProblem` class**: This is the core class that manages the shared resource, reader and writer threads, and synchronization.
  - **`read` method**: Used by reader threads to read from the resource. It uses locks to allow multiple readers to read concurrently.
  - **`write` method**: Used by writer threads to write to the resource, ensuring exclusive access during writing operations.

- **`reader_function`**: This function simulates a reader's behavior, continuously attempting to read from the resource and pausing between reads.
- **`writer_function`**: This function simulates a writer's behavior, continuously attempting to write to the resource and pausing between writes.

