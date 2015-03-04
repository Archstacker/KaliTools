import os
import configparser

nodes=[]
links=[]
def dfs( currnode,parentnum ):
    nodes.append( {'name':currnode['name']} )
    currnum = len(nodes)-1
    if parentnum is not None:
        links.append( {"source":parentnum,"target":currnum} )
    for num in currnode:
        if num != 'name':
            dfs( currnode[num],currnum )


config = configparser.ConfigParser( strict=False )
dirtree = { 'name':'Kali' }
destdir = 'Kali/desktop-directories'
for filename in os.listdir(destdir):
    tdic = dirtree
    for num in filename.split('-',3):
        if num[0].isdigit() and num[1].isdigit():
            try:
                tdic = tdic[num]
            except:
                tdic[num] = {}
                tdic = tdic[num]
    if tdic != dirtree:
        config.read( os.path.join(destdir,filename) )
        tdic['name'] = config['Desktop Entry']['Name[zh_CN]']

dfs( dirtree,None )
print(nodes)
print(links)
