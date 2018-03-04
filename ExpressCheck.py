'''
Created on 2018年2月26日

@author: lidawei
'''

import json,requests
def searchPackage():
    #输入快递单号
    packageNumber = input('请输入快递单号：\n')
    url1 = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=' + packageNumber
    #用url1查询快递单号对应的快递公司，如中通则返回zhongtong
    companyName = json.loads(requests.get(url1).text)['auto'][0]['comCode']
    #在用url2查询快递单号、快递公司和快递详情，结果是一个json文件，用dict保存在resultdict中
    url2 = 'http://www.kuaidi100.com/query?type=' + companyName + '&postid=' + packageNumber 
    for item in json.loads(requests.get(url2).text)['data']:
        print(item['time'],item['context'])
searchPackage()
