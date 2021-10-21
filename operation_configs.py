#coding:utf-8
import configparser,os
import json

BASEDIR = os.path.dirname(os.path.abspath(__file__))

class OperationConfigs(object):
    def __init__(self):
        self.file_name = "sas.ini"
        self.config = configparser.ConfigParser()
        self.config.read(self.getConfigsPath(self.file_name),encoding='UTF-8')

    #获得文件路径
    def getConfigsPath(self,file):
        return os.path.join(BASEDIR,file).replace('\\','/')

    #读取items
    def readItems(self,section):
        return self.config.items(section)
    #写入section
    def writeSection(self,section,option,value):
        if section not in self.config.sections():
            self.config.add_section(section)
        self.config.set(section, option, value)
        with open(self.getConfigsPath(self.file_name),"w+") as f:
            self.config.write(f)
        return 200

    # 获取port.json信息
    def getJsonInfo(self):
        with open(self.getConfigsPath('pcle.json'), encoding='utf-8') as f:
            return json.load(f)

    def writJsonInfo(self, port_info):
        with open(self.getConfigsPath('pcle.json'), 'w', encoding='utf-8') as w:
            json.dump(port_info, w)

