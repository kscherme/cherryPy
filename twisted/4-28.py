from twisted.internet.defer import DeferredQueue
import time


def foo(data):
	print "foo: ", data

def bar(data):
	print "bar: ", data

donald = "duck"
mickey = "mouse"

queue = DeferredQueue()

queue.put(donald)


#queue.get() gets deferred object
# don't actually pull off that deferred object
queue.get().addCallback(foo)

queue.get().addCallback(bar)  #still will only print once

# Dequeue happens when you put something on there
queue.put(mickey)
# prints:
# foo:  duck
# bar:  mouse

# when you have the connections call queue.get().addCallback(forwardData)