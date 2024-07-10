# queue.py

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """ Menambahkan item ke dalam antrian (queue) """
        self.queue.append(item)

    def dequeue(self):
        """ Menghapus item dari awal antrian (queue) dan mengembalikannya """
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None  # atau raise Exception, tergantung kebutuhan

    def remove_at(self, index):
        """ Menghapus item dari antrian (queue) berdasarkan index """
        if 0 <= index < len(self.queue):
            return self.queue.pop(index)
        else:
            return None  # atau raise Exception, tergantung kebutuhan

    def head(self):
        """ Mengembalikan elemen yang berada di depan antrian (queue) """
        if not self.is_empty():
            return self.queue[0]
        else:
            return None  # atau raise Exception, tergantung kebutuhan

    def display(self):
        """ Menampilkan semua elemen dalam antrian (queue) """
        print("Queue:", self.queue)

    def is_empty(self):
        """ Memeriksa apakah antrian (queue) kosong """
        return len(self.queue) == 0
