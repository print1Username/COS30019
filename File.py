import os

class File:
    def __init__(self,readfile,writefile):
        self.readfile = readfile
        self.writefile = writefile

    def DetectFile(self):
        if os.path.exists(self.readfile) and self.readfile.lower().endswith('.txt'):
            return True
        else:
            return False

    def ReadFile(self):
        filelist = []
        with open(self.readfile, 'r', encoding='utf-8') as file:
            for num, line in enumerate(file, 1):
                filelist.append(line.strip())
        return filelist

    def WriteFile(self, content):
        with open(self.writefile, 'w', encoding='utf-8') as file:
            file.write(content)

    def AddFile(self, content):
        with open(self.writefile, 'a', encoding='utf-8') as file:
            file.write('\n\n')
            file.write(content)