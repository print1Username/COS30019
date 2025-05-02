import argparse


class Parser:
    def __init__(self):
        parser = argparse.ArgumentParser(
            prog='Tree Based Search',
            description='This is the python program about the tree based search.',
            epilog='Smile :)'
        )

        parser.add_argument('--strategy', type=str, default='dfs',choices=['dfs', 'bfs', 'gbfs', 'as', 'cus1', 'cus2'],help='Choose the Search Strategy for the program')
        parser.add_argument('--generate', action=argparse.BooleanOptionalAction, help='Choose to generate the solution in a file')
        parser.add_argument('--readfile', type=str, default='file.txt', help='Choose the read txt file.')
        parser.add_argument('--writefile', type=str, default='file_sol.txt',help='Custom the file name for the output solution')
        parser.add_argument('--window', action=argparse.BooleanOptionalAction, default=True,help='Choose to run the window or don`t start the windows')
        self.args = parser.parse_args()

    def ParserSearchStrategy(self):
        return self.args.strategy.lower()

    def ParserReadfile(self):
        return self.args.readfile

    def ParserWriteFile(self):
        return self.args.writefile

    def ParserCreateWindow(self):
        return self.args.window

