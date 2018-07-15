# @Time     :2018/7/15 下午5:06
# @Author   :Jennings
# @Email    :zjn@wiwi.ink

# queue队列
# queue is especially useful in threaded programming when information must be exchanged safely between multiple threads.
#
# class queue.Queue(maxsize=0) #先入先出
# class queue.LifoQueue(maxsize=0) #last in fisrt out
# class queue.PriorityQueue(maxsize=0) #存储数据时可设置优先级的队列
# Constructor for a priority queue. maxsize is an integer that sets the upperbound limit on the number of items that can be placed in the queue. Insertion will block once this size has been reached, until queue items are consumed. If maxsize is less than or equal to zero, the queue size is infinite.
#
# The lowest valued entries are retrieved first (the lowest valued entry is the one returned by sorted(list(entries))[0]). A typical pattern for entries is a tuple in the form: (priority_number, data).
#
# exception queue.Empty
# Exception raised when non-blocking get() (or get_nowait()) is called on a Queue object which is empty.
#
# exception queue.Full
# Exception raised when non-blocking put() (or put_nowait()) is called on a Queue object which is full.
#
# Queue.qsize()
# Queue.empty() #return True if empty
# Queue.full() # return True if full
# Queue.put(item, block=True, timeout=None)
# Put item into the queue. If optional args block is true and timeout is None (the default), block if necessary until a free slot is available. If timeout is a positive number, it blocks at most timeout seconds and raises the Full exception if no free slot was available within that time. Otherwise (block is false), put an item on the queue if a free slot is immediately available, else raise the Full exception (timeout is ignored in that case).
#
# Queue.put_nowait(item)
# Equivalent to put(item, False).
#
# Queue.get(block=True, timeout=None)
# Remove and return an item from the queue. If optional args block is true and timeout is None (the default), block if necessary until an item is available. If timeout is a positive number, it blocks at most timeout seconds and raises the Empty exception if no item was available within that time. Otherwise (block is false), return an item if one is immediately available, else raise the Empty exception (timeout is ignored in that case).
#
# Queue.get_nowait()
# Equivalent to get(False).
#
# Two methods are offered to support tracking whether enqueued tasks have been fully processed by daemon consumer threads.
#
# Queue.task_done()
# Indicate that a formerly enqueued task is complete. Used by queue consumer threads. For each get() used to fetch a task, a subsequent call to task_done() tells the queue that the processing on the task is complete.
#
# If a join() is currently blocking, it will resume when all items have been processed (meaning that a task_done() call was received for every item that had been put() into the queue).
#
# Raises a ValueError if called more times than there were items placed in the queue.
#
# Queue.join() block直到queue被消费完毕
