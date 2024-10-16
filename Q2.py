import threading
import time
import random

class WriterReaderProblem:
    def __init__(self):
        self.resource = 0
        self.readers_count = 0
        self.readers_lock = threading.Lock()
        self.writers_lock = threading.Lock()
        self.write_waiting = threading.Condition(self.writers_lock)

    def read(self, reader_id):
        with self.readers_lock:
            self.readers_count += 1
            if self.readers_count == 1:
                self.writers_lock.acquire()

        print(f"Reader {reader_id} is reading. Resource value: {self.resource}")
        time.sleep(random.uniform(0, 1))

        with self.readers_lock:
            self.readers_count -= 1
            if self.readers_count == 0:
                self.writers_lock.release()

    def write(self, writer_id):
        with self.write_waiting:
            print(f"Writer {writer_id} is waiting.")
            self.write_waiting.wait()

        with self.writers_lock:
            print(f"Writer {writer_id} is writing. Resource value before: {self.resource}")
            self.resource += 1
            print(f"Writer {writer_id} is writing. Resource value after: {self.resource}")
            time.sleep(random.uniform(0, 1))

        with self.write_waiting:
            self.write_waiting.notify()

def reader_function(reader_id, wr_problem):
    while True:
        wr_problem.read(reader_id)
        time.sleep(random.uniform(0, 1))

def writer_function(writer_id, wr_problem):
    while True:
        wr_problem.write(writer_id)
        time.sleep(random.uniform(0, 1))

if __name__ == "__main__":
    wr_problem = WriterReaderProblem()

    # Create reader threads
    for i in range(3):
        reader_thread = threading.Thread(target=reader_function, args=(i + 1, wr_problem))
        reader_thread.start()

    # Create writer threads
    for i in range(2):
        writer_thread = threading.Thread(target=writer_function, args=(i + 1, wr_problem))
        writer_thread.start()
