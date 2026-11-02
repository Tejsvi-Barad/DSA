class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top=None
        
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node
        
    def pop(self):
        if self.top is None:
            print("stack is empty")
            return None
        popped_data=self.top.data
        self.top=self.top.next
        print(f"Popped data:{popped_data}")
        return popped_data
    
    def peek(self):
        if self.top is None:
            print("stack is empty")
            return None
        print(f"top element :{self.top.data}")
        return self.top.data
    
    def display(self):
        if self.top is None:
            print("stack is empty")
            return
        temp =self.top
        while temp is not None:
            print(f"{temp.data}",end="->")
            temp =temp.next
        print("None")

st = stack()
print("stack ope using linkdlist")
st.push(10)
st.push(20)
st.push(30)
st.display()
st.peek()

st.pop()
st.display()
       
    