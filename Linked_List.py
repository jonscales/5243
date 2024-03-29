"""
Linked List Code
Code copied from bfaure/Python3_Data_Structures GitHub
https://github.com/bfaure/Python3_Data_Structures/blob/master/Linked_List/main.py
"""

class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class linked_list:
	def __init__(self):
		"""constructor method"""
		self.head=node()
	
	def insertFront(self, data):
		"""Adds new node containing 'data' to the beginning of the linked list """
		new_node=node(data) # creates new node instance
		new_node.next=self.head #sets new node's next to point to head 
		self.head=new_node # makes the new node into the head node

	def insertRear(self,data):
		"""Adds new node containing 'data' to the end of the linked list."""
		new_node=node(data) # creates new node instance
		cur=self.head # creates a traversing pointer intially pointed at head node
		while cur.next!=None: # loop to move point down list to end
			cur=cur.next
		cur.next=new_node # points last node to new node (new node already points to null)
	
	def insertInOrder(self,data):
		"""Adds node with data in order for sorted list"""
		new_node=node(data)  # creates new node instance
		if self.length==0:
			self.head=new_node	
		else: 
			cur=self.head # creates a traversing pointer intially pointed at head node
			if (cur.data<self.head.data): # if new data < head node data, do a front sert
				self.insertFront(data)
			else:
				while (cur.next.data<data): #traverse list until data of next node is > than data yet current node data is < data
					cur=cur.next 
					if(cur.next==None): # if all nodes are checked and none are > than data, insert data at last position
						cur.next=new_node
					else: # create connenctions to insert new node between cur and cur.next nodes
						new_node.next=cur.next
						cur=new_node
		
	def length(self):
		"""Returns the length (integer) of the linked list."""
		cur=self.head
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total 

	def display(self):
		"""Prints out the linked list in traditional Python list format."""
		elems=[]
		cur_node=self.head
		while cur_node.next!=None:
			cur_node=cur_node.next
			elems.append(cur_node.data)
		print(elems)

	def get(self,index):
		"""Returns the value of the node at 'index'."""
		if index>=self.length() or index<0: # added 'index<0' post-video
			print("ERROR: 'Get' Index out of range!")
			return None
		cur_idx=0
		cur_node=self.head
		while True:
			cur_node=cur_node.next
			if cur_idx==index: return cur_node.data
			cur_idx+=1

	def erase(self,index):
		"""Deletes the node at index 'index'."""
		if index>=self.length() or index<0: # added 'index<0' post-video
			print("ERROR: 'Erase' Index out of range!")
			return 
		cur_idx=0
		cur_node=self.head
		while True:
			last_node=cur_node
			cur_node=cur_node.next
			if cur_idx==index:
				last_node.next=cur_node.next
				return
			cur_idx+=1

	def __getitem__(self,index):
		"""Allows for bracket operator syntax (i.e. a[0] to return first item)."""
		return self.get(index)

	def insertAt(self,index,data):
		"""Inserts a new node at index 'index' containing data 'data'.
		   Indices begin at 0. If the provided index is greater than or 
		   equal to the length of the linked list the 'data' will be appended."""

		if index>=self.length() or index<0:
			return self.append(data)
		cur_node=self.head
		prior_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index: 
				new_node=node(data)
				prior_node.next=new_node
				new_node.next=cur_node
				return
			prior_node=cur_node
			cur_idx+=1

	
	def insertEmptyNode(self,index,node):
		"""Inserts the node 'node' at index 'index'. Indices begin at 0.
		   If the 'index' is greater than or equal to the length of the linked 
		   list the 'node' will be appended."""
		if index<0:
			print("ERROR: 'Erase' Index cannot be negative!")
			return
		if index>=self.length(): # append the node
			cur_node=self.head
			while cur_node.next!=None:
				cur_node=cur_node.next
			cur_node.next=node
			return
		cur_node=self.head
		prior_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index: 
				prior_node.next=node
				return
			prior_node=cur_node
			cur_idx+=1

	
	def set(self,index,data):
		"""Sets the data at index 'index' equal to 'data'.
		   Indices begin at 0. If the 'index' is greater than or equal 
		   to the length of the linked list a warning will be printed 
		   to the user."""
		if index>=self.length() or index<0:
			print("ERROR: 'Set' Index out of range!")
			return
		cur_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index: 
				cur_node.data=data
				return
			cur_idx+=1