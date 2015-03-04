import os
import configparser
config = configparser.ConfigParser( strict=False )
dirtree = {}
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
