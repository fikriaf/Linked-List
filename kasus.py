class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            print("Antrian kosong")
            return None
        else:
            removed = self.front.data
            self.front = self.front.next
            if not self.front:
                self.rear = None
            return removed

    def is_empty(self):
        return self.front is None


# Inisialisasi antrian
cpu_queue = Queue()

# JOB 1 masuk (Perkalian)
job1_result = 2 * 5
cpu_queue.enqueue(job1_result)

# JOB 2 masuk (Pertambahan)
cpu_queue.enqueue(4 + 7)

# JOB 3 masuk (Pertambahan hasil JOB 1 dengan 3)
job3_operand = cpu_queue.dequeue() + 3
cpu_queue.enqueue(job3_operand)

# Proses eksekusi JOB
while not cpu_queue.is_empty():
    hasil = cpu_queue.dequeue()
    print("Hasil eksekusi:", hasil)
