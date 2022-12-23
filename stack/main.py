from Stack import Stack

def main():
    stack = Stack()
    stack.push('a')
    top = stack.peek()
    print(top._data)
    stack.push('b')
    stack.pop()
    

main()