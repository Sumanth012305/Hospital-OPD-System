class Patient:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

class OPDPriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, patient):
        self.queue.append(patient)
        self.queue.sort()  # Sort based on priority

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)  # Return the patient with highest priority

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]  # Return the patient at the front

    def size(self):
        return len(self.queue)

# Example usage
if __name__ == '__main__':
    opd_queue = OPDPriorityQueue()
    opd_queue.enqueue(Patient('Alice', 2))
    opd_queue.enqueue(Patient('Bob', 1))
    opd_queue.enqueue(Patient('Charlie', 3))

    print('Next patient:', opd_queue.peek().name)
    while not opd_queue.is_empty():
        patient = opd_queue.dequeue()
        print('Attending patient:', patient.name)