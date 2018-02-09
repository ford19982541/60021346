# -*- coding: utf-8 -*-
#ptva = PhayaoTambolViaAmphur
import json
ptva ={
     "mueng"  :[["maeka",30000],
                ["maetum",10000]],
     "maejai" : [["maejai",30000]],
     "pong" : [["pong",35000]]
}

s = json.dumps(ptva)
outjson =open('json.txt','w')
json.dump(ptva,outjson)
outjson.close()

injson =open('json.txt','r')
x = json.load(injson)
injson.close()