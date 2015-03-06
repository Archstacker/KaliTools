import os
import configparser

nodes=[]
links=[]
dirnums={}
def dfs( currnode,parentnum ):
    nodes.append( {'name':currnode['name'],'icon':currnode['icon'],'power':currnode['power'],'description':''} )
    currnum = len(nodes)-1
    dirnums[currnode['dirname']] = currnum
    if parentnum is not None:
        links.append( {'source':parentnum,'target':currnum} )
    for num in currnode:
        if num != 'name' and num != 'dirname' and num != 'icon' and num != 'power' and num != 'description' :
            dfs( currnode[num],currnum )


config = configparser.ConfigParser( strict=False )
dirtree = { 'name':'Kali','dirname':'Kali','icon':'kali-menu.png','power':10,'description':'' }
destdir = 'Kali/desktop-directories'
for filename in os.listdir(destdir):
    tdic = dirtree
    power = 8
    for num in filename.split('-',3):
        if num[0].isdigit() and num[1].isdigit():
            power = power - 2
            try:
                tdic = tdic[num]
            except:
                tdic[num] = {}
                tdic = tdic[num]
    if tdic != dirtree:
        config.read( os.path.join(destdir,filename) )
        tdic['name'] = config['Desktop Entry']['Name[zh_CN]']
        tdic['dirname'] = filename.split('.')[0]
        tdic['icon'] = config['Desktop Entry']['Icon']
        tdic['power'] = power
        tdic['description'] = ''

dfs( dirtree,None )
destdir = 'Kali/applications'
for filename in os.listdir(destdir):
    config.read( os.path.join(destdir,filename) )
    nodes.append( {'name':config['Desktop Entry']['name'],'icon':'kali-menu.png','power':1,'description':''} )
    currnum = len(nodes)-1
    for category in config['Desktop Entry']['Categories'].split(';'):
        try:
            if category != 'top10' and category != '' :
                links.append( {'source':dirnums[category],'target':currnum} )
        except:
            pass
print(nodes)
print(links)
