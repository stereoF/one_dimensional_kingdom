from functools import reduce


class OneDimentionalKingdom(object):
    bomb_cnt = 1

    def __init__(self, kingdoms):
        self.kingdoms = kingdoms

    def __sort_kingdoms(self):
        self.kingdoms.sort(key=lambda kingdom: kingdom[0])

    def __reduce_two_kingdoms(self, kingdom1, kingdom2):
        if kingdom1[1] <= kingdom2[0]:
            self.bomb_cnt += 1
            return kingdom2
        else:
            return [kingdom2[0], min(kingdom1[1], kingdom2[1])]

    def place_bombs(self):
        self.__sort_kingdoms()
        reduce(lambda kingdom1, kingdom2: self.__reduce_two_kingdoms(kingdom1, kingdom2), self.kingdoms)


# kingdoms = [[1, 3], [2, 5], [6, 9]]
# kingdoms = [[1, 14], [5, 11], [3, 27], [31, 32], [2, 8], [15, 19]]
# one_dimentional_kingdom = OneDimentionalKingdom(kingdoms)
# one_dimentional_kingdom.place_bombs()
# print(one_dimentional_kingdom.bomb_cnt)