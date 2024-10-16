# Readers-Writers Problem

## Introduction
This project implements a solution for the classic Readers-Writers Problem, simulating multiple readers and writers accessing a shared resource (in this case, a variable) using Python's threading and synchronization mechanisms.

### Synchronization overview:
Synchronization mechanisms in an operating system are techniques used to control the access of multiple processes or threads to shared resources in order to prevent conflicts and ensure data consistency. These mechanisms are essential in multi-threaded and multi-process environments where processes or threads may need to access shared data or resources simultaneously. Here’s a detailed overview:
In this solution, synchronization mechanisms (locks and conditions) are used to solve the problem of concurrent access to a shared resource:

<img width="1020" alt="Screenshot 1403-07-25 at 10 55 46" src="https://github.com/user-attachments/assets/ec6e7a57-2c87-42f7-9b5e-7f7e5a3aba43">

### Types of Synchronization Mechanisms
1. Mutex (Mutual Exclusion):
   - A mutex is a locking mechanism that ensures that only one thread can access a resource at a time. When a thread locks a mutex, other threads trying to lock the same mutex will block until it is unlocked.
2. **Semaphores:**
   - A semaphore is a signaling mechanism that can be used to control access to a resource. It can be binary (0 or 1, similar to a mutex) or counting (allowing a certain number of threads to access the resource).
   - **Binary Semaphore:** Similar to a mutex, allowing one thread to enter the critical section.
   - **Counting Semaphore:** Allows multiple threads to access the critical section, up to a defined limit.
3. **Condition Variables:**
   - These are used to block a thread until a particular condition is met. Condition variables work in conjunction with mutexes to allow threads to wait for certain conditions to be true before proceeding.
4. **Read-Write Locks:**
   - These locks allow concurrent access for multiple readers but give exclusive access to a writer. This is useful when reads are more frequent than writes, improving performance.
5. **Barriers:**
   - A synchronization barrier is a mechanism that forces a set of threads to wait until all threads reach a certain point of execution before continuing. It is often used in parallel programming.
6. **Spinlocks:**
   - A type of lock that repeatedly checks if the lock is available, "spinning" in a loop until it can acquire the lock. Spinlocks can be efficient in scenarios where the wait time is expected to be short, but they can waste CPU cycles if the wait is long.


## Program Functionality

### Key Requirements:
- Multiple readers can access the resource simultaneously without conflicts.
- Writers require exclusive access to the resource, meaning only one writer can modify the resource at a time.
- Synchronization mechanisms (locks and conditions) are used to ensure the proper coordination between readers and writers.

## Problem Description

In database management systems (DBMS), multiple users can either read from or write to a shared resource (such as a database). The goal of the Readers-Writers Problem is to allow multiple readers to read from the shared resource concurrently while ensuring that only one writer can modify the resource at any given time.

## Solution Overview

This Python implementation uses:
- **Locks** to ensure exclusive access to the shared resource for writers and manage reader access.
- **Condition variables** to manage waiting writers, ensuring writers get access only when no readers are using the resource.

### Synchronization Mechanisms Used:
In this solution, synchronization mechanisms (locks and conditions) are used to solve the problem of concurrent access to a shared resource:

**1. Locks:**
   - **Readers Lock (`readers_lock`)**: This lock is used to ensure that readers can safely increment and decrement the count of active readers. When the first reader accesses the resource, the readers lock ensures that the writer cannot access the resource at the same time. If more readers arrive while a reader is already reading, they can proceed without interruption.
   
   - **Writers Lock (`writers_lock`)**: This lock ensures that only one writer can access the shared resource at a time. When a writer acquires this lock, no other readers or writers can access the resource until the writer has finished.

**2. Condition Variables:**
   - **Write Waiting (`write_waiting`)**: This condition variable is used to put writers in a waiting state if the resource is currently being accessed by readers. It prevents writers from "jumping in" while there are active readers. Once the resource becomes available (i.e., no readers), a writer can proceed and modify the resource.

- **Multiple Readers**: Can access the resource simultaneously without blocking each other.
- **Writers**: Require exclusive access to the resource, meaning they must wait until there are no active readers or writers.
- **Reader-Writer Coordination**: The combination of locks and conditions ensures that when a writer wants to write, it waits for readers to finish, and once a writer has access, readers are blocked until the writer finishes.
  
This synchronization strategy prevents **race conditions** (multiple threads modifying or accessing the resource at the same time) and ensures data consistency.


## Code Breakdown

- **`WriterReaderProblem` class**: This is the core class that manages the shared resource, reader and writer threads, and synchronization.
  - **`read` method**: Used by reader threads to read from the resource. It uses locks to allow multiple readers to read concurrently.
  - **`write` method**: Used by writer threads to write to the resource, ensuring exclusive access during writing operations.

- **`reader_function`**: This function simulates a reader's behavior, continuously attempting to read from the resource and pausing between reads.
- **`writer_function`**: This function simulates a writer's behavior, continuously attempting to write to the resource and pausing between writes.

