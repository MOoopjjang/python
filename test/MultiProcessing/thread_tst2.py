#!python3
# -*- coding:utf-8 -*-


def tst1():
    from queue import Queue
    from threading import Thread, Condition

    class Producer(Thread):
        def __init__(self, _cv, _queue):
            self._cv = _cv
            self._queue = _queue
            self._running = True
            Thread.__init__(self)

        def push(self, _data):
            self._queue.put(_data)
            return self

        def stop(self):
            self._running = False

        def run(self):
            while self._running:
                with self._cv:
                    if self._queue:
                        self._cv.notify_all()

    class Consumer(Thread):
        def __init__(self, _cv, _queue):
            self._cv = _cv
            self._queue = _queue
            self._running = True
            Thread.__init__(self)

        def run(self):
            while self._running:
                with self._cv:
                    print('WATTING~~~~~~~~~~~')
                    self._cv.wait()
                    while self._queue:
                        v = self._queue.get()
                        print('v : {}'.format(v))

    condition = Condition()
    que = Queue()
    producer = Producer(condition, que)
    consumer = Consumer(condition, que)

    producer.start()
    consumer.start()

    while True:
        input_str = input('input:')
        producer.push(input_str)


if __name__ == '__main__':
    tst1()
