def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")
    if len(set(preorder)) != len(preorder) or len(set(inorder)) != len(inorder):
        raise ValueError("traversals must contain unique items")
    if not preorder:
        return {}
    root = {"v": preorder[0], "l": {}, "r": {}}
    for value in preorder[1:]:
        local_root = root
        while True:
            if inorder.index(value) - inorder.index(local_root["v"]) < 0:
                if local_root["l"]:
                    local_root = local_root["l"]
                else:
                    local_root["l"] = {"v": value, "l": {}, "r": {}}
                    break
            elif local_root["r"]:
                local_root = local_root["r"]
            else:
                local_root["r"] = {"v": value, "l": {}, "r": {}}
                break
    return root
