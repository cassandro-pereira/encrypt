#Encrypt Linked list
from cryptography.fernet import Fernet

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def print_hash(self):
        return print("The hash of this Linked List is : " + str(hash(self)))
    
    def print_encoding(self):
        encoding = str(self).encode(encoding="ascii")
        print ("The encoding of this Linked list is : " + str(encoding))
        return encoding
    
    def print_decoding(self, encoded_ll):
        decoding = str(encoded_ll).encode().decode(encoding="ascii")
        print ("The decoding of this Linked list is : " + str(decoding))
    
    def encode_all(self):
        temp = self.head
        while temp is not None:
            temp.value = str(temp.value).encode(encoding="ascii")
            temp = temp.next
    
    def decode_all(self):
        temp = self.head
        while temp is not None:
            temp.value = str(temp.value).encode().decode(encoding="ascii")
            temp = temp.next
      
#Creating a linked List for encrypting    
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(55)

my_linked_list.print_list()

##Now printing the hash values
my_linked_list.print_hash()

#Encoding Linked list (object)
encoding = my_linked_list.print_encoding()

#Decoding Linked List (object)
my_linked_list.print_decoding(encoding)

#Encoding all items from Linked List
my_linked_list.encode_all()
my_linked_list.print_list()

#Decoding all items from Linked List
my_linked_list.decode_all()
my_linked_list.print_list()