import re


class List:
    def __init__(self, mylist):
        self.mylist = mylist

    def DetectList(self):
        if isinstance(self.mylist, list):
            return True
        else:
            return False

    def GetSizeList(self):
        pattern = r'\[(\d+),(\d+)\]'
        size_list = []
        matches = re.findall(pattern, self.mylist[0])
        for match in matches:
            for m in match:
                size_list.append(int(m))
        return size_list

    def GetStartList(self):
        pattern = r'\((\d+),(\d+)\)'
        start_list = []
        matches = re.findall(pattern, self.mylist[1])
        for match in matches:
            for m in match:
                start_list.append(int(m))
        return tuple(start_list)

    def GetEndList(self):
        pattern = r'\((\d+),(\d+)\)'
        end_list = []
        matches = re.findall(pattern, self.mylist[2])
        for match in matches:
            x, y = match
            end_list.append((int(x),int(y)))
        return end_list

    def GetWallList(self):
        pattern = r'\((\d+),(\d+),(\d+),(\d+)\)'
        wall_list = []
        for item in self.mylist[3:]:
            if isinstance(item, str):
                matches = re.findall(pattern, item)
                for match in matches:
                    wall = tuple(int(num) for num in match)
                    wall_list.append(wall)
        return wall_list

    def ConvertWallList(self):
        wall_list = self.GetWallList()
        new_wall_list = []
        for wall in wall_list:
            for i in range(self.GetSizeList()[0]):
                for j in range(self.GetSizeList()[1]):
                    if (i >= wall[0]) and (i < wall[0] + wall[2]) and (j >= wall[1]) and (j < wall[1] + wall[3]):
                        new_wall_list.append((i,j))
        return new_wall_list