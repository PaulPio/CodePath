"""You run a local bakery and are given the roots of two binary trees order1 and order2 where each node in the binary tree represents the number of a certain cookie type the customer has ordered. 
To maximize efficiency, you want to bake enough of each type of cookie for both orders together.

Given order1 and order2, merge the order together into one tree and return the root of the merged tree. To merge the orders, imagine that when place one tree on top of the other, some nodes of the two trees are overlapped while others are not. If two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the not None node will be used as the node of the new tree.

Start the merging process from the root of both orders.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

UMPIRE template 

# Understand 
inputs: 2 binary trees
outputs: 1 merged binary tree
constraints: -
edge cases - empty trees 

  # Match (any problems this reminds you of, any helpful patters to solve this e.g. two pointer technique, any data structures this reminds you of )
    bst merge two binary trees, dfs, bfs, recursion, queue
  # Plan (pseudocode) 
    like in the example that we saw in class, we will return root.val from tree1 plus root.val from tree 2, then call the functions recursive on left tree, then in the right tree
  # Implement (python code)
    root1 = order1.root
    root2 = order2.root
    if root1.val or root2.val == None:
        return None
    return [root1.val + root2.val] + merge_orders(root1.left, root1.left) + merge_orders(root1.right, root1.right)
  # Review (dry run of your code)

  # Evaluate (time and space complexity)
    return 

"""

from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root
def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root


def merge_orders(order1, order2):
    # If one node is missing, return the other (covers both being None as well)
    if not order1:
        return order2
    if not order2:
        return order1

    # If both exist, sum the values
    merged_node = TreeNode(order1.val + order2.val)

    # Recursively merge the left and right subtrees
    merged_node.left = merge_orders(order1.left, order2.left)
    merged_node.right = merge_orders(order1.right, order2.right)

    return merged_node
    

    

"""
     1             2         
    /  \         /   \       
   3    2       1     3   
 /               \      \   
5                 4      7   
"""
# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
print_tree(merge_orders(order1, order2))


#Problem 2: Croquembouche
class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    #base case, if root empty
    if not design:
        return []
    queue = deque([design]) # create a queue
    #create a list with visisted vlaues
    visited = []
    while queue: #while there are items on the queue
        current = queue.popleft() #remove the first item in the queue and send it to the current
        visited.append(current.val) #add current to the visited array
        if current.left: # if there is an item on current left, add to the queu
            queue.append(current.left)  
        if current.right: # if there is an item on current right, add to the queu
            queue.append(current.right)
    return visited # return visited array
"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print(print_design(croquembouche))



#Problem 3: Maximum Tiers in Cake
def max_tiers(cake):
    pass

