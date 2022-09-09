from implementation import *
from binary_node import *

# find_pi_day()
# store_fruits_and_vegggies()
# store_user_info()
# print_family_members()

my_tree = BinaryTree()

my_tree.insert_node(27)
my_tree.insert_node(14)
my_tree.insert_node(35)
my_tree.insert_node(10)
my_tree.insert_node(19)
my_tree.insert_node(31)
my_tree.insert_node(42)

my_tree.search_for_node(10)
my_tree.search_for_node(42)
my_tree.search_for_node(31)
my_tree.search_for_node(14)
my_tree.search_for_node(5)
my_tree.search_for_node(100)