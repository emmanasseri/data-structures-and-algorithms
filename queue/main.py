from Queue import Queue

def main():
    queueExample = Queue()
    queueExample.enqueue(40)
    print(queueExample.peekFront()._data)

    

main()