import string
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum


class SgfTree:
    def __init__(self, properties=None, children=None, parent=None):
        self.properties = properties or defaultdict(list)
        self.children = children or []
        self.parent = parent

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other):
        return not self == other


class ValueType(Enum):
    UNDETERMINED: int = 0
    PROPERTY_KEY: int = 1
    PROPERTY_VALUE: int = 2


@dataclass
class SgfProperty:
    value_type: ValueType = ValueType.UNDETERMINED
    value: str = ""
    key: str = None
    backslashed: bool = False


def parse(input_string):
    if not input_string or input_string[0] != "(":
        raise ValueError("tree missing")
    if input_string[1] != ";":
        raise ValueError("tree with no nodes")
    root = local_root = node = SgfTree()
    sgf_property = SgfProperty()
    for i, char in enumerate(input_string[2:], 2):
        match char:
            case "(":
                if sgf_property.value_type == ValueType.PROPERTY_VALUE:
                    sgf_property.value += char
            case ";":
                if sgf_property.value_type == ValueType.PROPERTY_VALUE:
                    sgf_property.value += char
                    continue
                node = SgfTree()
                if local_root:
                    local_root.children.append(node)
                    node.parent = local_root
                if input_string[i - 1] == "(":
                    local_root = node
            case "[":
                if sgf_property.value_type == ValueType.PROPERTY_VALUE:
                    sgf_property.value += char
                    continue
                if sgf_property.value_type == ValueType.PROPERTY_KEY:
                    sgf_property.key = sgf_property.value
                sgf_property = SgfProperty(
                    value_type=ValueType.PROPERTY_VALUE, key=sgf_property.key
                )
            case "]":
                if sgf_property.backslashed:
                    sgf_property.value += char
                    sgf_property.backslashed = False
                    continue
                node.properties[sgf_property.key].append(sgf_property.value)
                sgf_property = SgfProperty(key=sgf_property.key)
            case ")":
                if sgf_property.value_type == ValueType.PROPERTY_VALUE:
                    sgf_property.value += char
                    continue
                if sgf_property.value_type == ValueType.PROPERTY_KEY:
                    raise ValueError("properties without delimiter")
                sgf_property = SgfProperty()
                if local_root:
                    local_root = local_root.parent
            case _:
                if sgf_property.value_type == ValueType.UNDETERMINED:
                    sgf_property.value_type = ValueType.PROPERTY_KEY
                if (
                    sgf_property.value_type == ValueType.PROPERTY_KEY
                    and char not in string.ascii_uppercase
                ):
                    raise ValueError("property must be in uppercase")
                if char == "\\":
                    if sgf_property.backslashed:
                        sgf_property.value += "\\"
                        sgf_property.backslashed = False
                    else:
                        sgf_property.backslashed = True
                elif char in {" ", "\t"}:
                    sgf_property.value += " "
                    sgf_property.backslashed = False
                elif char == "\n":
                    if sgf_property.backslashed:
                        sgf_property.backslashed = False
                    else:
                        sgf_property.value += char
                else:
                    sgf_property.value += char
    return root
