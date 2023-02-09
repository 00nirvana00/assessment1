'''


@author: ashay
config with path information
change the top_dir to reflect the location of project
'''

import os


def makeDirIfNotExist(dirName):
    if not os.path.isdir(dirName):
        os.makedirs(dirName)


class DataDirPath:
    
    def __init__(self):
        # links to various data files
        # top_dir is the project directory
        
        top_dir = 'Y:\\Interviews\\zGithub\\backtest\\'
        self.top_dir = top_dir
        self.data_dir = os.path.join(top_dir,'data')
        self.result_dir = os.path.join(top_dir,'result')


        makeDirIfNotExist(self.data_dir)
        makeDirIfNotExist(self.result_dir)
