import os
from urllib.request import urlopen

class Solution:

    def __init__(self, size_list, value_list, backpack_size):
        self.size_list = size_list
        self.value_list = value_list
        self.backpack_size = backpack_size
        self.solution_matrix = [[-1 for x in range(backpack_size+1)] for j in range(len(size_list)+1)]
        # initialisation of empty matrix for future solution


    def dynamic_pack_it(self, n, backpack_size):
        # function find the most effective way to pack
        # the sum of values must be the biggest but the
        # sum of sizes can't be bigger then the size of backpack

        if n == 0 or backpack_size == 0:
            self.solution_matrix[n][backpack_size] = 0
            return 0

        elif self.solution_matrix[n][backpack_size] != -1:
            return self.solution_matrix[n][backpack_size]

        elif self.size_list[n-1] <= backpack_size:
            self.solution_matrix[n][backpack_size] = max(self.value_list[n-1] + self.dynamic_pack_it(n-1, backpack_size - self.size_list[n-1]), self.dynamic_pack_it(n-1, backpack_size))
            return self.solution_matrix[n][backpack_size]

        else:
            self.solution_matrix[n][backpack_size] = self.dynamic_pack_it(n - 1, backpack_size)
            return self.solution_matrix[n][backpack_size]

    def greedy_pack_it(self, n, backpack_size):
        # first step is too calculate value to size ratio

        solution_list = []
        size = 0
        solution = 0

        for x in range(n):
            temp = [self.value_list[x], self.size_list[x], (self.value_list[x] / self.size_list[x])]
            solution_list.append(temp)

        solution_list = sorted(solution_list, key = lambda x: x[2], reverse = True)

        for i in range(n):
            if size + solution_list[i][1] <= backpack_size:
                size += solution_list[i][1]
                solution += solution_list[i][0]

        return solution


if __name__ == '__main__':

    if not os.path.exists("test_data.txt"): #checkout if path allready exist
        u = urlopen('http://www.cs.put.poznan.pl/mmachowiak/instances/plecak.txt') #download necessary file
        localFile = open('test_data.txt', 'wb')
        localFile.write(u.read())
        localFile.close()

    text_file = open('test_data.txt', "r")
    text_file = text_file.readlines()

    #data preparation to acceptable format
    text_file[0] = int(text_file[0][0])
    text_file[1] = text_file[1][0:(text_file[0]*2) -1 ]
    text_file[2] = text_file[2][0:(text_file[0]*2) - 1]
    text_file[3] = int(text_file[3][0])
    print("input data: {}".format(text_file))

    n = text_file[0] # number of possible elements
    size_list = [] # element i have size[i] size and value_list[i] value
    value_list = []
    backpack_size = text_file[3]

    for index in range(0, len(text_file[1]), 2):
        size_list.append(int(text_file[1][index])) #rewrite values in list from char into int format
        value_list.append(int(text_file[2][index]))
    s = Solution(size_list, value_list,backpack_size)

    print("dynamic: {}".format(s.dynamic_pack_it(n, backpack_size)))
    print("greedy: {}".format(s.greedy_pack_it(n, backpack_size)))


