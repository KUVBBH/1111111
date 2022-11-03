'''
*需要安装 Qpython 3H

*需要再手机根目录(/storage/emulated/0/)
下创建tv(小写)文件夹

*将直播源文件放在tv文件夹下
后缀为.m3u或者.m3u8

*本文件放在qpython文件夹下

*可以检测频道是否可用，去除重复频道，去除无用频道

*会在tv文件夹下从新生成一个.m3u8文件

*urllib.request.urlopen(a,timeout=3)
timeout时间为秒，out值越大，结果会更准确 

*修改台标等其他操作可以在74,76行完成

*直播源在B站搜，有很多

*写的比较乱，勿喷
 
'''
import urllib.request
import random
import os

www=[]
zzz=[]
ppp=[]
sss='#EXTM3U\n'

def qwertyui(a):
    try:
        urllib.request.urlopen(a,timeout=3)
    except :
        print('不能用')
        return 0
    else :
        print('能用')  
        return 1
        
qqq=os.listdir('../tv')
for i in qqq:
    if ''.join(i.split('.')[-1:]) == 'm3u8' or ''.join(i.split('.')[-1:]) == 'm3u' :
        www.append(i)
if len(www) == 1 :
    with open ('../tv/'+www[0],'r') as f :
        vvv=f.readlines()[1:]
else:
    print('*'*10,'\n请选择文件:\n','*'*10)
    for i in range (1,len(www)+1):
        print(i,'---',www[i-1])
    nnn=input('选择文件:')
    print(www[int(nnn)-1])
    with open ('../tv/'+www[int(nnn)-1],'r') as f :
        vvv=f.readlines()[1:]
for i in range (0,len(vvv)-1,2) :
    print(vvv[i])
    ggg=qwertyui(vvv[i+1])
    print('共',len(vvv)/2,'个,已完成',i/2+1,'个','\n'*5)
    if ggg == 1 :
        fff=(''.join(vvv[i].split(',')[-1:]),vvv[i+1])
        zzz.append(fff)
print(zzz)
for i in zzz :
    #print(i[0],i[1])
    if i[0] not in ppp :
        ppp.append(i[0])
        #print(i[0][0:4])
        if i[0][0:4] == 'cctv' or i[0][0:4] == 'CCTV' :
            sss=sss+'#EXTINF:-1 group-title="央视频道",'+i[0]+i[1]
        else :
            sss=sss+'#EXTINF:-1 group-title="其他频道",'+i[0]+i[1]
print(sss)
name=str(random.randint(100000,1000000))
with open('../tv/'+name+'.m3u8','w') as f :
    f.write(sss)
    
print('\n'*10+'文件保存在"tv"目录下，名为'+name+'.m3u8'+'\n'*10)
