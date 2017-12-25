import youtube_dl.YoutubeDL

class Node:

    def __init__(self, link):
        self.song = link
        self.next = None
        self.title = None
        self.time = None

    def get_next(self) -> object:
        if self.next is None:
            print('Nothing else in queue')
        else:
            return self.next

    def next(self, n: object, link: object) -> object:
        if n.next is None:
            n.next = Node(link)
        elif n.next is not None:
            node = n.get_next()
            n.next(node, link)
        else:
            return

    def has_next(self):
        if self.next is None:
            return True
        else: 
            return False

class Queue:

    def __init__(self):
        self.current = None
        self.playlist = []

    def add(self, link):
        if self.current is None:
            self.current = Node(link)
        else:
            self.current.next(self.current, link)
        self.update()
    
    def build(self, node: Node):
        if node.has_next() is True:
            self.playlist.append('{} Duration: {}/{}\n'.format(node.title, str(node.duration /60).split('.')[0], str(node.duration % 60)))
            n = node.get_next()
            self.build(n)
        else:
            self.playlist.append('{} Duration: {}/{}\n'.format(node.title, str(node.duration /60).split('.')[0], str(node.duration % 60)))
    
    def update(self):
        self.playlist = []
        if self.current is not None:
            self.build(self.current)

