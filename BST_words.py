"""
Binary Search Tree Code
Code copied from bfaure/Python3_Data_Structures GitHub
https://github.com/bfaure/Python3_Data_Structures/blob/master/Binary_Search_Tree/main.py
"""
class node:
	def __init__(self,word=None):
		self.word=word
		self.left_child=None
		self.right_child=None
		self.parent=None # pointer to parent node in tree
		self.height=1

class binary_search_tree:
	def __init__(self):
		self.root=None
		
	def insert(self,word):
		if self.root==None:
			self.root=node(word)
		else:
			self._insert(word,self.root)

	def _insert(self,word,cur_node):
		if word<cur_node.word:
			if cur_node.left_child==None:
				cur_node.left_child=node(word)
				cur_node.left_child.parent=cur_node # set parent
			else:
				self._insert(word,cur_node.left_child)
		elif word>cur_node.word:
			if cur_node.right_child==None:
				cur_node.right_child=node(word)
				cur_node.right_child.parent=cur_node # set parent
			else:
				self._insert(word,cur_node.right_child)
		else:
			print("word already in tree!")

	def in_order_print(self):
		if self.root!=None:
			self._in_order_print(self.root)
	def pre_order_print(self):
		if self.root!=None:
			self._pre_order_print(self.root)		
	def post_order_print(self):
		if self.root!=None:
			self._post_order_print(self.root)

	def _in_order_print(self,cur_node):
		if cur_node!=None:
			self._in_order_print(cur_node.left_child)
			print (str(cur_node.word))
			self._in_order_print(cur_node.right_child)
	
	def _pre_order_print(self,cur_node):
		if cur_node!=None:
			print (str(cur_node.word))
			self._pre_order_print(cur_node.left_child)
			self._pre_order_print(cur_node.right_child)

	def _post_order_print(self,cur_node):
		if cur_node!=None:
			self._post_order_print(cur_node.left_child)
			self._post_order_print(cur_node.right_child)		
			print (str(cur_node.word))
	def inorder_print(self):
		if self.root!=None:
			self._inorder_print(self.root)

	def preorder_print(self):
		if self.root!=None:
			self._preorder_print(self.root)

	def postorder_print(self):
		if self.root!=None:
			self._postorder_print(self.root)				

	def _inorder_print(self,cur_node):
		if cur_node!=None:
			self._inorder_print(cur_node.left_child)
			print (str(cur_node.word))
			self._inorder_print(cur_node.right_child)

	def _preorder_print(self,cur_node):
		if cur_node!=None:
			print (str(cur_node.word))
			self._preorder_print(cur_node.left_child)
			self._preorder_print(cur_node.right_child)

	def _postorder_print(self,cur_node):
		if cur_node!=None:
			self._postorder_print(cur_node.left_child)
			self._postorder_print(cur_node.right_child)	
			print (str(cur_node.word))			

	def height(self):
		if self.root!=None:
			return self._height(self.root,0)
		else:
			return 0

	def _height(self,cur_node,cur_height):
		if cur_node==None: return cur_height
		left_height=self._height(cur_node.left_child,cur_height+1)
		right_height=self._height(cur_node.right_child,cur_height+1)
		return max(left_height,right_height)

	def find(self,word):
		if self.root!=None:
			return self._find(word,self.root)
		else:
			return None

	def _find(self,word,cur_node):
		if word==cur_node.word:
			return cur_node
		elif word<cur_node.word and cur_node.left_child!=None:
			return self._find(word,cur_node.left_child)
		elif word>cur_node.word and cur_node.right_child!=None:
			return self._find(word,cur_node.right_child)

	def delete_word(self,word):
		return self.delete_node(self.find(word))

	def delete_node(self,node):

		## -----
		# Improvements since prior lesson

		# Protect against deleting a node not found in the tree
		if node==None or self.find(node.word)==None:
			print("Node to be deleted not found in the tree!")
			return None 
		## -----

		# returns the node with min word in tree rooted at input node
		def min_word_node(n):
			current=n
			while current.left_child!=None:
				current=current.left_child
			return current

		# returns the number of children for the specified node
		def num_children(n):
			num_children=0
			if n.left_child!=None: num_children+=1
			if n.right_child!=None: num_children+=1
			return num_children

		# get the parent of the node to be deleted
		node_parent=node.parent

		# get the number of children of the node to be deleted
		node_children=num_children(node)

		# break operation into different cases based on the
		# structure of the tree & node to be deleted

		# CASE 1 (node has no children)
		if node_children==0:

			# Added this if statement post-video, previously if you 
			# deleted the root node it would delete entire tree.
			if node_parent!=None:
				# remove reference to the node from the parent
				if node_parent.left_child==node:
					node_parent.left_child=None
				else:
					node_parent.right_child=None
			else:
				self.root=None

		# CASE 2 (node has a single child)
		if node_children==1:

			# get the single child node
			if node.left_child!=None:
				child=node.left_child
			else:
				child=node.right_child

			# Added this if statement post-video, previously if you 
			# deleted the root node it would delete entire tree.
			if node_parent!=None:
				# replace the node to be deleted with its child
				if node_parent.left_child==node:
					node_parent.left_child=child
				else:
					node_parent.right_child=child
			else:
				self.root=child

			# correct the parent pointer in node
			child.parent=node_parent

		# CASE 3 (node has two children)
		if node_children==2:

			# get the inorder successor of the deleted node
			successor=min_word_node(node.right_child)

			# copy the inorder successor's word to the node formerly
			# holding the word we wished to delete
			node.word=successor.word

			# delete the inorder successor now that it's word was
			# copied into the other node
			self.delete_node(successor)

	def search(self,word):
		if self.root!=None:
			return self._search(word,self.root)
		else:
			return False

	def _search(self,word,cur_node):
		if word==cur_node.word:
			return True
		elif word<cur_node.word and cur_node.left_child!=None:
			return self._search(word,cur_node.left_child)
		elif word>cur_node.word and cur_node.right_child!=None:
			return self._search(word,cur_node.right_child)
		return False 
	
	# def __repr__(self):
	# 	"""function to display the tree sort of """
	# 	if self.root==None: return ''
	# 	content='\n' # to hold final string
	# 	cur_nodes=[self.root] # all nodes at current level
	# 	cur_height=self.root.height # height of nodes at current level
	# 	sep=' '*(2**(cur_height-1)) # variable sized separator between elements
	# 	while True:
	# 		cur_height+=-1 # decrement current height
	# 		if len(cur_nodes)==0: break
	# 		cur_row=' '
	# 		next_row=''
	# 		next_nodes=[]

	# 		if all(n is None for n in cur_nodes):
	# 			break

	# 		for n in cur_nodes:

	# 			if n==None:
	# 				cur_row+='   '+sep
	# 				next_row+='   '+sep
	# 				next_nodes.extend([None,None])
	# 				continue

	# 			if n.word!=None:       
	# 				buf=' '*int((5-len(str(n.word)))/2)
	# 				cur_row+='%s%s%s'%(buf,str(n.word),buf)+sep
	# 			else:
	# 				cur_row+=' '*5+sep

	# 			if n.left_child!=None:  
	# 				next_nodes.append(n.left_child)
	# 				next_row+=' /'+sep
	# 			else:
	# 				next_row+='  '+sep
	# 				next_nodes.append(None)

	# 			if n.right_child!=None: 
	# 				next_nodes.append(n.right_child)
	# 				next_row+='\ '+sep
	# 			else:
	# 				next_row+='  '+sep
	# 				next_nodes.append(None)

	# 		content+=(cur_height*'   '+cur_row+'\n'+cur_height*'   '+next_row+'\n')
	# 		cur_nodes=next_nodes
	# 		sep=' '*int(len(sep)/2) # cut separator size in half
	# 	return content

wordlist=binary_search_tree()
with open('words_50.txt','r') as file:
	for word in file:
		wordlist.insert(word.strip())

#print(wordlist)
#input("press enter to continue")
print("inorder print")
wordlist.in_order_print()
input("Press enter to continue")
print("preorder print")
wordlist.pre_order_print()
input("Press enter to continue")
print("postorder print")
wordlist.post_order_print()
