"""
Copyright 2017 Timothy Laskoski

tree.py handles all code related to the parse tree
"""

def tree_append(parent, sub):
    "tree_append appends a sub tree to the parent tree"
    parent["Sub"].append(sub)
    # print("TREE APPEND", parent)

def add_subtree(parent, token):
    "add_subtree adds a subtree with a token to the parent"
    new_sub = create_tree_with_token(token, parent)
    tree_append(parent, new_sub)

    return parent, new_sub

def create_tree(parent):
    "create_tree creates a tree with the parent being the parent"
    return {"Tok": None, "Sub": [], "Par": parent}

def create_tree_with_token(token, parent):
    "create_tree_with_token creates a tree with a parent and a value"
    return {"Tok": token, "Sub": [], "Par": parent}