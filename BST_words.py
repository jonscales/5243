"""
Binary Search Tree Code
Code copied from bfaure/Python3_Data_Structures GitHub
https://github.com/bfaure/Python3_Data_Structures/blob/master/Binary_Search_Tree/main.py
"""
import os
import math

"""This allows specification of a path for the '.dot' output for graphviz"""
script_dir=os.path.dirname(os.path.abspath(__file__))
outpath=os.path.join(script_dir, 'mybst.dot')

class node:
	node_counter = 0
	def __init__(self,word = None):
		self.word = word
		self.left_child = None
		self.right_child = None
		self.parent = None # pointer to parent node in tree
		self.height = 1
		self.balance_factor = 0
		self.node_id = node.node_counter
		node.node_counter += 1

class binary_search_tree:
	def __init__(self):
		self.root = None
		self.node_id = 0
		self.num_nodes = 0
		self.sum_of_heights = 0

	def complexity(self):
		"""Returns the complexity of O(logn) for the size of the tree (n)"""
		return "{:.2f}".format(math.log(self.num_nodes, 2))
	
	def height(self):
		if self.root!=None:
			return self._height(self.root,0)
		else:
			return 0

	def _height(self,cur_node,cur_height):
		if cur_node==None: 
			return cur_height
		left_height=self._height(cur_node.left_child,cur_height+1)
		right_height=self._height(cur_node.right_child,cur_height+1)
		return max(left_height,right_height)
	
	def avg_height(self):
		"""Returns the average height of the nodes"""
		return self.sum_of_heights/self.num_nodes
		
	def height_sum(self):
		""" will calculate a sum of the heights of all nodes in a tree. Is passed the tree itself
			then recursively calls each child until reaching leaf nodes. The sum of heights is stored
			as an attribute of the tree. The function also returns the value"""
		if self.root==None:
			self.sum_of_heights = 0
		else:
			self._height_sum(self.root)
		return self.sum_of_heights
			
	def _height_sum(self, cur_node):
		""" recursive height summation method called from the height_sum(root) method"""
		if cur_node != None:
			self.sum_of_heights += cur_node.height
			self._height_sum(cur_node.left_child)
			self._height_sum(cur_node.right_child)
	
	def _calculate_height(self, cur_node):
		if cur_node == None:
			return 0
		return 1 + max(self._calculate_height(cur_node.left_child),self._calculate_height(cur_node.right_child))
	
	def update_heights(self, cur_node=None):
		"""Updates the node's height attribute after any insertion, deletion, 
			or rebalancing """
		if cur_node == None:	
			cur_node=self.root
		if cur_node == None:
			return
		cur_node.height = self._calculate_height(cur_node)
		self.update_heights(cur_node.left_child)
		self.update_heights(cur_node.right_child)
		
	def update_balfactor(self,cur_node):
		"""Updates the balance factor attribute of a node after any insertion,
			deletion, or rebalancing event"""
		if cur_node == None:
			return 0
		else:
			left_height = cur_node.left_child.height if cur_node.left_child else 0
			right_height = cur_node.right_child.height if cur_node.right_child else 0 
			cur_node.balance_factor = left_height - right_height
		
		return cur_node.balance_factor	
		
	def insert(self,word):
		inTree=False
		if self.root == None:
			self.root=node(word)
			self.num_nodes += 1
			self.update_heights()
			self.update_balfactor(self.root)
			
		else:
			self._insert(word,self.root)
			if inTree == False:
				self.num_nodes += 1
				self.update_heights()
				self.update_balfactor(self.root)

	def _insert(self,word,cur_node):
		inTree=False
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
			inTree = True # used to keep the node count from being incremented 
	
		return inTree
	
	#public methods for prints
	def in_order_print(self):
		if self.root!=None:
			self._in_order_print(self.root)
	def pre_order_print(self):
		if self.root!=None:
			self._pre_order_print(self.root)		
	def post_order_print(self):
		if self.root!=None:
			self._post_order_print(self.root)

	#private recursive print methods called by public methods above
	def _in_order_print(self,cur_node):
		if cur_node!=None:
			self._in_order_print(cur_node.left_child)
			print ('%d- %s, h=%d, bf=%d'%(cur_node.node_id, str(cur_node.word),cur_node.height, cur_node.balance_factor))
			self._in_order_print(cur_node.right_child)
	
	def _pre_order_print(self,cur_node):
		if cur_node!=None:
			print ('%d- %s, h=%d, bf=%d'%(cur_node.node_id, str(cur_node.word),cur_node.height, cur_node.balance_factor))
			self._pre_order_print(cur_node.left_child)
			self._pre_order_print(cur_node.right_child)

	def _post_order_print(self,cur_node):
		if cur_node!=None:
			self._post_order_print(cur_node.left_child)
			self._post_order_print(cur_node.right_child)		
			print ('%d- %s, h=%d, bf=%d'%(cur_node.node_id, str(cur_node.word),cur_node.height, cur_node.balance_factor))



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

		# Protect against deleting a node not found in the tree
		if node==None or self.find(node.word)==None:
			print("Node to be deleted not found in the tree!")
			return None 
		
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

		#call update methods to update height and balance factor	
		self.update_height(node.parent)
		self.update_balfactor(node.parent)

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
	
	#GraphViz output generation for visualization of node structures
	def graphviz_get_ids(self, node, viz_out):
		if node:
			self.graphviz_get_ids(node.left_child, viz_out)
			viz_out.write(" node{} [label=\"{}-{}, H={}, BF={}\"];\n".format(node.node_id, node.node_id, node.word, node.height, node.balance_factor))
			self.graphviz_get_ids(node.right_child, viz_out)
	
	def graphviz_make_connections(self, node, viz_out):
		if node:
			if node.left_child:
				viz_out.write("  node{} -> node{};\n".format(node.node_id, node.left_child.node_id))
				self.graphviz_make_connections(node.left_child, viz_out)
			if node.right_child:
				viz_out.write("  node{} -> node{};\n".format(node.node_id, node.right_child.node_id))
				self.graphviz_make_connections(node.right_child, viz_out)
				
	def graphviz_out(self,filename):
		with open(filename, 'w') as viz_out:
			viz_out.write("digraph g { \n")
			self.graphviz_get_ids(self.root, viz_out)
			self.graphviz_make_connections(self.root, viz_out)
			viz_out.write("} \n")
			
#Main Program	

wordBST=binary_search_tree()
with open('words_25.txt','r') as file:
	for word in file:
		wordBST.insert(word.strip().upper())

wordBST.graphviz_out(outpath)

print("inorder print")
wordBST.in_order_print()
# Perform analysis of the tree
print('The number of nodes in this AVL tree is : ', wordBST.num_nodes)
print('Tree height is : ', wordBST.height())
print('O(log n) complexity value for this tree is : ', wordBST.complexity())
print('The total sum of all node heights is : ', wordBST.height_sum())
print('The average node height is : ', wordBST.avg_height())
# input("Press enter to continue")
# print("preorder print")
# wordlist.pre_order_print()
# input("Press enter to continue")
# print("postorder print")
# wordlist.post_order_print()
