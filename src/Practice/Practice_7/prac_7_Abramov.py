from dataclasses import dataclass
from typing import Optional, Generic, TypeVar


V = TypeVar("V")

@dataclass
class Tree(Generic[V]):
    root: Optional["TreeNode"]
    size: int = 0


@dataclass
class TreeNode(Generic[V]):
    key: Optional[any]
    value: Optional[V]
    left: Optional["TreeNode[V]"]
    right: Optional["TreeNode[V]"]


def create_tree_map():
    return Tree(None)


def put(tree: Tree,key: int, value):
    if tree.size != 0:
        put_node(tree.root, key, value)
    else:
        put_root(tree, key, value)
    tree.size += 1


def put_node(tree_root: TreeNode, key: int, value: V):
    if tree_root is None:
        return TreeNode(key,value,None,None)
    if key > tree_root.key:
        tree_root.right = put_node(tree_root.right,key,value)
    if key < tree_root.key:
        tree_root.left = put_node(tree_root.left, key, value)
    return tree_root


def put_root(tree: Tree, key: int,value: V):
    tree.root = TreeNode(key,value,None,None)


def remove_node(tree_root, key):
    if tree_root is None:
        raise AttributeError("No key in tree")


    def remove_recursion(tree_root, key):
        if tree_root.key < key:
            n_right_child, value = remove_recursion(tree_root.right, key)
            tree_root.right = n_right_child
        elif tree_root.key > key:
            n_right_child, value = remove_recursion(tree_root.left, key)
            tree_root.left = n_right_child
        if tree_root.left is None and tree_root.right is None:
            return None, tree_root.value
        elif tree_root.left is not None or tree_root.right is not None:
            n_node = tree_root.left if tree_root.left is not None else tree_root.right
            return n_node, tree_root.value
        else:
            pass
            # tree_root, value = remove_recursion(tree_root.left, key)
        return TreeNode[V], key


def remove(tree, key):
    if tree.root is None:
        raise AttributeError("No such key")
    return remove_node(tree.root, key)