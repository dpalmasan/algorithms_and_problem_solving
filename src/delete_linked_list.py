class SinglyLinkedListNode:
    def __init__(self,
                 data: int,
                 next: "SinglyLinkedListNode"=None):
        self.data = data
        self.next = next
        self.last = self

    def append(self, node: "SinglyLinkedListNode"):
        self.last.next = node
        self.last = node

def deleteNode(llist, position):
    # Write your code here
    rec = llist
    pos = 0
    while rec:
        if position == 0:
            return rec.next
        elif rec.next.next is None and pos + 2 == position:
            rec.next = None
            return llist
        elif position == pos + 1:
            rec.next = rec.next.next
            break
        pos += 1
        rec = rec.next
    return llist



inp = [
    20,
    6,
    2,
    19,
    7,
    4,
    15,
    9
]

llist = None
for i, data in enumerate(inp):
    node = SinglyLinkedListNode(data)
    if i == 0:
        llist = node
    else:
        llist.append(node)

rec = llist
while rec:
    print(rec.data)
    rec = rec.next

llist = deleteNode(llist, 7)

print("="*79)
rec = llist
while rec:
    print(rec.data)
    rec = rec.next