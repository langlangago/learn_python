#! encoding:utf-8


# 扑克牌游戏，item系列的应用
# from collections import namedtuple
# import json
# Card = namedtuple('Card', ['rank', 'suit'])
# card = Card('A', '红心')
# print(card.suit, card.rank)
# class FranchDeck:
#     ranks = [ str(i) for i in range(2, 11) ] + list('JQKA')
#     suits = ['黑桃', '红桃', '梅花', '方块']
#
#     def __init__(self):
#         self.__cards = [ Card(rank, suit) for rank in FranchDeck.ranks for suit in FranchDeck.suits]
#     def __getitem__(self, item):
#         return self.__cards[item]
#     def __len__(self):
#         return len(self.__cards)
#     def __str__(self):
#         return  json.dumps(self.__cards, ensure_ascii=False)
# deck = FranchDeck()
# print(deck)
# print(deck[10])
# from random import choice
# print(choice(deck))

# __hash__ 实例
# 100个对象，从人的类实例化而来，名字，性别一样，年龄不一样
# 按照名字和性别去重 set; 他们组成一个元组或者列表传给set
# 让set去自动去重，只剩下一个。
# set()依赖 hash 和 eq,所以自己要实现类的内置方法__hash__,__eq__
class A:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
    def __eq__(self, other):
        if self.name == other.name and self.sex == other.sex:
            return True
        return False
    def __hash__(self):
        return hash(self.name + self.sex)

a = A('alex', 'male', 18)
b = A('alex', 'male', 20)
print(set((a,b)))
