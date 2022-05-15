from node import Node


def parse(token_chain):
    trees = [token_chain]
    complete_trees = []
    while len(trees) > 0:
        tree = trees.pop(0)
        if len(tree) == 1 and isinstance(tree[0], Node) and tree[0].is_root():
            complete_trees.append(tree)
            continue
        for node in Node.__subclasses__():
            for rule in node.rules():
                for i in range(len(tree) - len(rule)+1):
                    if all(isinstance(tok, clause) for tok, clause in zip(tree[i:], rule)):
                        new_tree = tree[:i] + [node(tree[i:i+len(rule)])] + tree[i+len(rule):]
                        trees.append(new_tree)
    if len(complete_trees) == 0:
        raise ValueError("Could not build syntax tree")
    if len(complete_trees) > 1:
        raise ValueError("Multiple syntax trees")
    return complete_trees[0][0]

