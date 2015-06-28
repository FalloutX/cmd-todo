import random
from clint.textui import puts, indent, colored

class Counter(object):
    def __init__(self, name, base):
        self._todobase = base
        self._name = name
        self._count = self._todobase.get('/counter', self._name)
        if self._count is None:
            self._count = random.randint(1,1000)
            self._todobase.put('/counter', self._name, self._count)

    def get(self):
        self._count += 1
        self._todobase.put('/counter', self._name, self._count)
        return self._count


def foreach(collection, callback):
    for key in collection.keys():
        item = collection[key]
        callback(item, key)

def print_todo_item(item, key=None):
    """
    prints an todo item.
    """
    if item is not None:
        donestring = colored.green((u'\u2713').encode('utf-8'))
        puts( str(key) + " : "+colored.blue(str(item['bounty'])) + " : " + item['task']
             + " " + (donestring if item['done'] else ''))
    else:
        puts( colored.red('404: Nothing Found'))
