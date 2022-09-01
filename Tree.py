class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов

class SimpleTree:

    def __init__(self, root):
        self.Root = root # корень, может быть None

    def AddChild(self, ParentNode, NewChild): # ваш код добавления нового дочернего узла существующему ParentNode
        if self.Root is None:
            self.Root = NewChild
        else:
            ParentNode.Children.append(NewChild)
            NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):# ваш код удаления существующего узла NodeToDelete
        node_up = NodeToDelete.Parent
        if node_up == None:
            self.Root = None
            return
        node_up.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def GetAllNodes(self):# ваш код выдачи всех узлов дерева в определённом порядке
        vizit = []  # надо предусмотреть если корень none или только один корень
        stack = []
        node = self.Root
        if node == None:
            return vizit
        vizit.append(node)
        while True:
            for i in range(len(node.Children)):
                stack.insert(0, node.Children[i])
            if len(stack) == 0:
                break
            node = stack[0]
            vizit.insert(0, stack[0])
            stack.pop(0)
        return vizit

    def FindNodesByValue(self, val):# ваш код поиска узлов по значению
        vizit = []
        stack = []
        result = []
        node = self.Root
        if node == None:  # если первый узел none
            return vizit
        if node.NodeValue == val:  # если один узел корневой
            result.append(node)
        while True:
            for i in range(len(node.Children)):
                stack.insert(0, node.Children[i])
            if len(stack) == 0:
                break
            node = stack[0]
            if node.NodeValue == val:
                result.append(node)
            vizit.insert(0, stack[0])
            stack.pop(0)
        return result

    def MoveNode(self, OriginalNode, NewParent):# ваш код перемещения узла вместе с его поддеревом -- # в качестве дочернего для узла NewParent
        if self.Root == None:  # если первый узел none
            return
        if OriginalNode == None:
            return
        if NewParent == None:
            return
        if OriginalNode.Parent == NewParent:# если переставляемые нepks уже так и стоят
            return
        else:
            node_up = OriginalNode.Parent
            index = 0
            for i in range(len(node_up.Children)):
                if node_up.Children[i] == OriginalNode:
                    index = i
            node_up.Children.remove(node_up.Children[index])
            self.AddChild(NewParent, OriginalNode)

    def Count(self):# количество всех узлов в дереве
        if self.Root == None:  # если первая нода нан
            return 0
        count = len(self.GetAllNodes())  # количество всех узлов в дереве
        return count
    def LeafCount(self):# количество листьев в дереве
       if self.Root == None:# если первый узел none
           return 0
       count = 0
       for i in self.GetAllNodes():
           if len(i.Children) == 0 or i.Children == None:
               count += 1# количество листьев в дереве
       return count
