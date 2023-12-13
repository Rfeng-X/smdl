from random import randint
import time
print('游戏名《神秘地牢》')
print('IO字体建议使用Arial CE或Letter Gothic Std')
print('game start')
map1=['X X X X X X X X X X X X X X X X X X X X X',
      'X X X X X X X X X X X X X X X X X X X X X',
      'X X                                   X X',
      'X X                                   X X',
      'X X                                   X X',
      'X X                                   X X',
      'X X                                   X X',
      'X X                                   X X',
      'X X                                   X X',
      'X X                                   X X',
      'X X                                   X X',
      'X X                                   X X',
      'X X                                   X X',
      'X X                                   X X',
      'X X                                   X X',
      'X X                                   X X',
      'X X                                   X X',
      'X X                                   X X',
      'X X                                   X X',
      'X X X X X X X X X X X X X X X X X X X X X',
      'X X X X X X X X X X X X X X X X X X X X X']
map2=['X X X X X X X X X X X X X X X X X X X',
      'X X X X X X X X X X X X X X X X X X X',
      'X X X X X X X X X X X X X X X X X X X',
      'X X X               k           X X X',
      'X X X            /w\            X X X',
      'X X X               v           X X X',
      'X X X                           X X X',
      'X X X             P             X X X',
      'X X X                           X X X',
      'X X X                           X X X',
      'X X X                           X X X',
      'X X X                           X X X',      
      'X X X         /XI   IX\         X X X',
      'X X X        /XXX # XXX\     [!]X X X',
      'X X X X X X XXXXXXXXXXXXX X X X X X X',
      'X X X X X X XXXXXXXXXXXXX X X X X X X',
      'X X X X X X X X X X X X X X X X X X X']
sight=['         ',
       '         ',
       '         ',
       '         ',
       '         ']
Sight=['             ',
       '             ',
       '             ',
       '             ',
       '             ',
       '             ',
       '             ']       
TB=False
wzsy=False
dscj=False
ngqj=False
xmzs=False
fp={}
def zt():
    print('精力值:',life,'钥匙:',key,'个','金币:',money,'精华:',soul),print('工具栏:',tools)
print('骑士K;法师F;游侠S;医生H;工匠R;魔人Y;炮手D;猎人V')
player=input("请选择角色:")
if player=='K':
    life=[0]*6
    key=2
    money=6
    soul=2
    dj={}
    tools={'/':4,'[]':4,'=}':0,'T':5}
    wq={'1:长剑+--':4,'6:重盾{:}':4}    
elif player=='F':
    life=[0]*4
    key=2
    money=7
    soul=6
    dj={'护身符δ':1}
    tools={'/':2,'[]':3,'=}':0,'T':5}
    wq={'5:钩爪=~3':3,'3:奶盾[+]':2}
    dscj=True
elif player=='S':
    life=[0]*5
    key=3
    money=5
    soul=2
    dj={'神秘眼镜ee':1}
    tools={'/':3,'[]':2,'=}':4,'T':5}
    wq={'5:钩爪=~3':2,'2:弩炮=<}':3}
    TB=True
elif player=='H':
    life=[0,0,0,0]
    key=2
    money=8
    soul=4
    dj={}
    tools={'/':3,'[]':2,'=}':3,'T':6}
    wq={'3:奶盾[+]':5}
elif player=='R':
    life=[0]*5
    key=4
    money=8
    soul=0
    dj={}
    tools={'/':3,'[]':3,'=}':2,'T':8}
    wq={'4:砍刀->>':2,'2:弩炮=<}':2}
    ngqj=True
elif player=='Y':
    life=[0]*6
    key=0
    money=4
    soul=4
    dj={'神秘眼镜ee':1}
    tools={'/':3,'[]':4,'=}':0,'T':5}
    wq={'5:钩爪=~3':3,'4:砍刀->>':3}
    xmzs=True
elif player=='D':
    life=[0]*5
    key=2
    money=6
    soul=3
    dj={'1.炸弹Q':2}
    tools={'/':2,'[]':3,'=}':2,'T':5}
    wq={'2:弩炮=<}':3,'6:重盾{:}':3}
elif player=='V':
    life=[0]*5
    key=2
    money=6
    soul=2
    dj={}
    tools={'/':4,'[]':3,'=}':3,'T':5}
    wq={'1:长剑+--':2,'2:弩炮=<}':2,'4:砍刀->>':1,'5:钩爪=~3':1,'3:奶盾[+]':1}
    wzsy=True    
else:
    life=[0]*randint(4,8)
    dj={}
    wq={}
    key=randint(2,8)
    money=randint(6,12)
    soul=randint(2,6)
    tools={'/':randint(2,10),'[]':randint(2,10),'=}':randint(2,10),'T':randint(4,9)}
nd=input('请选择难度(1:简单;2:困难;3:地狱):')
if nd=='1':
    key+=3;money+=6;soul+=5
    tools['/']+=3;tools['[]']+=3;tools['=}']+=3;tools['T']+=3
if nd=='2':
    key+=1;money+=3;soul+=3
    tools['/']+=1;tools['[]']+=1;tools['=}']+=1;tools['T']+=1
zt()  
xsjc=input('是否需要新手教程(yes or no):')
if xsjc=='yes':
    print('------------')
    print('B为墙壁,#为出口,^为钥匙,$为宝箱,G是商店,X是地图边缘')
    print('*是精华,&是怪兽,@是魔法祭台,M是铁匠铺')
    print('wasd控制移动方向,按回车执行指令')
    print('方向中输入esc,可以退出游戏,方向中输入wq,可以查看武器栏,方向中输入dj,可以查看道具栏')
    print('成就结算每层分开')
    print('------------')
TJ=input('是否需要查看图鉴(yes or no):')
if TJ=='yes':
    print('------------')
    print('魔法祭台中的魔法:')
    print('‘无中生有’:闪避成功获得装备;‘隐身咒语’:100%逃跑;‘血魔之手’:拳头攻击吸血')
    print('‘点石成金’:挖墙概率获得金币;‘能工巧匠’:开宝箱概率不消耗钥匙;‘元素萃取’:翻垃圾堆不会收到伤害')
    print('铁匠铺中合成的武器:')
    print('长剑:100%命中,伤害1~2;弩炮:概率连击,伤害1~3;奶盾:加两滴血和一层护盾')
    print('砍刀:伤害2~3;重盾:加两层护盾,伤害1;勾爪:伤害1~2,吸血一滴')
    print('高级护盾格挡失败不消耗')
    print('------------')
def zspd(m,n,x,y,key,money,tools,js,life2,xmzs):
    if len(life2)<=0:
        print('\\你战胜了怪物//')
        gw=s[m][n]
        s[m]=s[m][0:n]+' '+s[m][n+1:]
        s[x]=s[x][0:y]+player+s[x][y+1:]
        x,y=m,n
        key,money,tools,xmzs=zlp(key,money,tools,gw,xmzs)
        js+=1
    return m,n,x,y,key,money,tools,js,life2,xmzs
def playerfight(hh,R1,R4,Tb,Q,soul,m,n,x,y,key,money,tools,js,dj,life2,gwhd,xmzs):
    sb=False
    if hh==0:
        print('----------')
        print('你的回合,请选择你的操作')
        print('1:普通攻击;2:武器攻击;3:闪避;4:逃跑')
        cz=input('序号:')
        sb=False
        if cz=='1':
            print('1:拳头;2:长矛/;3:弩箭=}')
            gj=input('请选择你的操作:')
            if gj=='2':
                if R1<=8:
                    if tools['/']>0:
                        if '[]' in gwhd:
                            print('>怪物有护盾<')
                            print('>使用长矛,攻击造成1点伤害')
                            print(player+' '+'/'+' '+'-1')
                            gwhd.pop()
                            life2.pop()
                            soul+=1
                            tools['/']-=1
                            m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                            if len(life2)<=0:
                                Q=False
                                return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                            zdxl(life2,tools,soul,gwhd)
                            hh=1
                        else:
                            print('>使用长矛，攻击造成2点伤害')
                            print(player+' '+'/'+' '+'-2')
                            life2.pop()
                            soul+=1
                            tools['/']-=1
                            m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                            if len(life2)<=0:
                                Q=False
                                return hh,Tb,sb,Q,soul,key,money,js,xmzs                        
                            life2.pop()
                            soul+=1
                            m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                            if len(life2)<=0:
                                Q=False
                                return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                            zdxl(life2,tools,soul,gwhd)
                            hh=1                        
                    else:
                        print('>>你没有长矛<<')
                else:
                    print('>怪物闪避了你的攻击<')
                    print('miss')
                    if tools['/']>0:
                        tools['/']-=1
                    print('工具栏:',tools)
                    hh=1                                        
            elif gj=='3':
                if R1<=8:
                    if tools['=}']>0:
                        if '[]' in gwhd:
                            print('>怪物有护盾<')
                            print('>>无法造成伤害<<')
                            print(player+' '+'=}'+' '+'-0')
                            gwhd.pop()
                            tools['=}']-=1             
                            zdxl(life2,tools,soul,gwhd)
                            hh=1
                        else:
                            print('>使用弩箭，攻击造成1点伤害')
                            print(player+' '+'=}'+' '+'-1')
                            life2.pop()
                            soul+=1
                            tools['=}']-=1
                            m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                            if len(life2)<=0:
                                Q=False
                                return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                            zdxl(life2,tools,soul,gwhd)
                            print('|触发连击|')
                            hh=0
                    else:
                        print('>>你没有弩箭<<')    
                else:
                    print('>怪物闪避了你的攻击<')
                    print('miss')
                    if tools['=}']>0:
                        tools['=}']-=1    
                    print('工具栏:',tools)
                    hh=1
            else:
                if R1<=10:
                    if '[]' in gwhd:
                            print('>怪物有护盾<')
                            print('>>无法造成伤害<<')
                            print(player+' '+';'+' '+'-0')
                            gwhd.pop()             
                            zdxl(life2,tools,soul,gwhd)
                            hh=1
                    else:
                        print('>使用拳头，攻击造成1点伤害')
                        print(player+' '+';'+' '+'-1')
                        life2.pop()
                        soul+=1
                        if xmzs:
                            print('|触发血魔之手|')
                            print(player+' '+';'+' '+'+1')
                            life.append(0)
                            print('你的精力值:',life)
                        m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                        if len(life2)<=0:
                            Q=False
                            return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                        print('怪物血量:',life2)
                        print('精华:',soul)
                        hh=1
                else:
                    print('>怪物闪避了你的攻击<')
                    print('miss')
                    hh=1                             
        elif cz=='3':
            sb=True
            hh=1
        elif cz=='4':
            if R4<=Tb:
                print('|逃跑成功|')
                Q=False
                return hh,Tb,sb,Q,soul,key,money,js,xmzs 
            else:
                print('>>逃跑失败<<')
                hh=1
        elif cz=='2':
            print('武器栏:',wq)
            wqxh=input('代号:')
            if wqxh=='1':
                if '1:长剑+--' not in wq:
                    print('>>你没有该装备<<')
                elif wq['1:长剑+--']>0:
                    if R1<=7:
                        if '[]' in gwhd:
                            print('>怪物有护盾<')
                            print('>使用长剑，攻击造成1点伤害')
                            print(player+' '+'+--'+' '+'-1')
                            gwhd.pop()
                            life2.pop()
                            soul+=1
                            wq['1:长剑+--']-=1
                            m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                            if len(life2)<=0:
                                Q=False
                                return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                            zdxl(life2,tools,soul,gwhd)
                            hh=1
                        else:
                            print('>使用长剑，攻击造成2点伤害')
                            print(player+' '+'+--'+' '+'-2')
                            life2.pop()
                            soul+=1
                            wq['1:长剑+--']-=1
                            m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                            if len(life2)<=0:
                                Q=False
                                return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                            life2.pop()
                            soul+=1
                            m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                            if len(life2)<=0:
                                Q=False
                                return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                            zdxl(life2,tools,soul,gwhd)
                            hh=1
                    elif 7<R1:
                        if '[]' in gwhd:
                            print('>怪物有护盾<')
                            print('>>无法造成伤害<<')
                            print(player+' '+'+--'+' '+'-0')
                            gwhd.pop()
                            wq['1:长剑+--']-=1
                            zdxl(life2,tools,soul,gwhd)
                            print('|触发连击|')
                            hh=0
                        else:
                            print('>使用长剑，攻击造成1点伤害')
                            print(player+' '+'+--'+' '+'-1')
                            life2.pop()
                            soul+=1
                            wq['1:长剑+--']-=1
                            m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                            if len(life2)<=0:
                                Q=False
                                return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                            zdxl(life2,tools,soul,gwhd)
                            print('|触发连击|')
                            hh=0
                else:
                    print('>>你没有该装备<<')
            elif wqxh=='2':
                if '2:弩炮=<}' not in wq:
                    print('>>你没有该装备<<')
                elif wq['2:弩炮=<}']>0:
                    if R1==1:
                        if '[]' in gwhd:
                                print('>怪物有护盾<')
                                print('>使用弩炮，攻击造成2点伤害')
                                print(player+' '+'=<}'+' '+'-2')
                                gwhd.pop()
                                life2.pop()
                                soul+=1
                                wq['2:弩炮=<}']-=1
                                m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                                if len(life2)<=0:
                                    Q=False
                                    return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                                life2.pop()
                                soul+=1
                                m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                                if len(life2)<=0:
                                    Q=False
                                    return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                                zdxl(life2,tools,soul,gwhd)
                                hh=1
                        else:
                            print('>使用弩炮，暴击!攻击造成3点伤害')
                            print(player+' '+'=<}'+' '+'-3')
                            life2.pop()
                            soul+=1
                            wq['2:弩炮=<}']-=1
                            m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                            if len(life2)<=0:
                                Q=False
                                return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                            life2.pop()
                            soul+=1
                            m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                            if len(life2)<=0:
                                Q=False
                                return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                            life2.pop()
                            soul+=1
                            m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                            if len(life2)<=0:
                                Q=False
                                return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                            zdxl(life2,tools,soul,gwhd)
                            hh=1
                    elif 1<R1<=5:
                        if '[]' in gwhd:
                            print('>怪物有护盾<')
                            print('>使用弩炮，攻击造成1点伤害')
                            print(player+' '+'=<}'+' '+'-1')
                            gwhd.pop()
                            life2.pop()
                            soul+=1
                            wq['2:弩炮=<}']-=1
                            m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                            if len(life2)<=0:
                                Q=False
                                return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                            zdxl(life2,tools,soul,gwhd)
                            print('|触发连击|')
                            hh=0
                        else:
                            print('>使用弩炮，攻击造成2点伤害')
                            print(player+' '+'=<}'+' '+'-2')
                            life2.pop()
                            soul+=1
                            wq['2:弩炮=<}']-=1
                            m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                            if len(life2)<=0:
                                Q=False
                                return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                            life2.pop()
                            soul+=1
                            m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                            if len(life2)<=0:
                                Q=False
                                return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                            zdxl(life2,tools,soul,gwhd)
                            print('|触发连击|')
                            hh=0
                    elif 5<R1<9:
                        if '[]' in gwhd:
                            print('>怪物有护盾<')
                            print('>>无法造成伤害<<')
                            print(player+' '+'=<}'+' '+'-0')
                            gwhd.pop()
                            wq['2:弩炮=<}']-=1
                            zdxl(life2,tools,soul,gwhd)
                            print('|触发连击|')
                            hh=0
                        else:
                            print('>使用弩炮，攻击造成1点伤害')
                            print(player+' '+'=<}'+' '+'-1')
                            life2.pop()
                            soul+=1
                            wq['2:弩炮=<}']-=1
                            m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                            if len(life2)<=0:
                                Q=False
                                return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                            zdxl(life2,tools,soul,gwhd)
                            print('|触发连击|')
                            hh=0
                    else:
                        print('>怪物闪避了你的攻击<')
                        print('miss')
                        hh=1
                        wq['2:弩炮=<}']-=1
                else:
                    print('>>你没有该装备<<')                                           
            elif wqxh=='3':
                if '3:奶盾[+]' not in wq:
                    print('>>你没有该装备<<') 
                elif wq['3:奶盾[+]']>0:
                    if R1<=10:
                        print('>使用奶盾')
                        print(player+' '+'[+]'+' '+'+2')
                        life.append(0)
                        life.append(0)
                        tools['[]']+=1
                        wq['3:奶盾[+]']-=1
                        print('工具栏:',tools)
                        hh=1
                    else:
                        print('>>格挡失败<<')
                        hh=1
                else:
                    print('>>你没有该装备<<')                               
            elif wqxh=='4':
                    if '4:砍刀->>' not in wq:
                        print('>>你没有该装备<<')
                    elif wq['4:砍刀->>']>0:
                        if R1<=5:
                            if '[]' in gwhd:
                                print('>怪物有护盾<')
                                print('>使用砍刀，攻击造成2点伤害')
                                print(player+' '+'->>'+' '+'-2')
                                gwhd.pop()
                                life2.pop()
                                soul+=1
                                wq['4:砍刀->>']-=1
                                m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                                if len(life2)<=0:
                                    Q=False
                                    return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                                life2.pop()
                                soul+=1
                                m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                                if len(life2)<=0:
                                    Q=False
                                    return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                                zdxl(life2,tools,soul,gwhd)
                                hh=1
                            else:
                                print('>使用砍刀，攻击造成3点伤害')
                                print(player+' '+'->>'+' '+'-3')
                                life2.pop()
                                soul+=1
                                wq['4:砍刀->>']-=1
                                m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                                if len(life2)<=0:
                                    Q=False
                                    return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                                life2.pop()
                                soul+=1
                                m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                                if len(life2)<=0:
                                    Q=False
                                    return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                                life2.pop()
                                soul+=1
                                m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                                if len(life2)<=0:
                                    Q=False
                                    return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                                zdxl(life2,tools,soul,gwhd)
                                hh=1
                        elif 6<=R1<=7:
                            if '[]' in gwhd:
                                print('>怪物有护盾<')
                                print('>使用砍刀，攻击造成1点伤害')
                                print(player+' '+'->>'+' '+'-1')
                                gwhd.pop()
                                life2.pop()
                                soul+=1
                                wq['4:砍刀->>']-=1
                                m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                                if len(life2)<=0:
                                    Q=False
                                    return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                                zdxl(life2,tools,soul,gwhd)
                                hh=1
                            else:
                                print('>使用砍刀，攻击造成2点伤害')
                                print(player+' '+'->>'+' '+'-2')
                                life2.pop()
                                soul+=1
                                wq['4:砍刀->>']-=1
                                m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                                if len(life2)<=0:
                                    Q=False
                                    return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                                life2.pop()
                                soul+=1
                                m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                                if len(life2)<=0:
                                    Q=False
                                    return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                                zdxl(life2,tools,soul,gwhd)
                                hh=1
                        else:
                            print('>怪物闪避了你的攻击<')
                            print('miss')
                            hh=1
                            wq['4:砍刀->>']-=1
                    else:
                        print('>>你没有该装备<<')
            elif wqxh=='5':
                    if '5:钩爪=~3' not in wq:
                        print('>>你没有该装备<<')
                    elif wq['5:钩爪=~3']>0:
                        if R1<=6:
                            if '[]' in gwhd:
                                print('>怪物有护盾<')
                                print('>使用钩爪，攻击造成1点伤害')
                                print(player+' '+'=~3'+' '+'-1')
                                gwhd.pop()
                                life2.pop()
                                soul+=1
                                wq['5:钩爪=~3']-=1
                                m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                                if len(life2)<=0:
                                    Q=False
                                    return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                                zdxl(life2,tools,soul,gwhd)
                                hh=1
                            else:
                                print('>使用钩爪，攻击造成2点伤害')
                                print(player+' '+'=~3'+' '+'-2')
                                life2.pop()
                                soul+=1
                                wq['5:钩爪=~3']-=1
                                life.append(0)
                                print('|吸血成功|')
                                m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                                if len(life2)<=0:
                                    Q=False
                                    return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                                life2.pop()
                                soul+=1
                                m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                                if len(life2)<=0:
                                    Q=False
                                    return hh,Tb,sb,Q,soul,key,money,js,xmzs                                     
                                zdxl(life2,tools,soul,gwhd)
                                hh=1
                        elif 7<=R1<=8:
                            if '[]' in gwhd:
                                print('>怪物有护盾<')
                                print('>>无法造成伤害<<')
                                print(player+' '+'=~3'+' '+'-0')
                                gwhd.pop()
                                wq['5:钩爪=~3']-=1
                                zdxl(life2,tools,soul,gwhd)
                                hh=1
                            else:
                                print('>使用钩爪，攻击造成1点伤害')
                                print(player+' '+'=~3'+' '+'-1')
                                life2.pop()
                                soul+=1
                                wq['5:钩爪=~3']-=1
                                life.append(0)
                                print('|吸血成功|')
                                m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                                if len(life2)<=0:
                                    Q=False
                                    return hh,Tb,sb,Q,soul,key,money,js,xmzs 
                                zdxl(life2,tools,soul,gwhd)
                                hh=1
                        else:
                            print('>怪物闪避了你的攻击<')
                            print('miss')
                            hh=1
                            wq['5:钩爪=~3']-=1
                    else:
                        print('>>你没有该装备<<')
            elif wqxh=='6':
                if '6:重盾{:}' not in wq:
                    print('>>你没有该装备<<') 
                elif wq['6:重盾{:}']>0:
                    if R1<=10:
                        if '[]' in gwhd:
                                print('>怪物有护盾<')
                                print('>>无法造成伤害<<')
                                print(player+' '+'{:}'+' '+'-0')
                                gwhd.pop()
                                wq['6:重盾{:}']-=1
                                tools['[]']+=2
                                zdxl(life2,tools,soul,gwhd)
                                hh=1
                        else:
                            print('>使用重盾,造成1点伤害')
                            print(player+' '+'{:}'+' '+'-1')
                            life2.pop()
                            tools['[]']+=2
                            wq['6:重盾{:}']-=1
                            m,n,x,y,key,money,tools,js,life2,xmzs=zspd(m,n,x,y,key,money,tools,js,life2,xmzs)
                            if len(life2)<=0:
                                Q=False
                                return hh,Tb,sb,Q,soul,key,money,js,xmzs ,xmzs
                            zdxl(life2,tools,soul,gwhd)
                            hh=1
                    else:
                        print('>>格挡失败<<')
                        hh=1
                else:
                    print('>>你没有该装备<<')
            else:
                print('>>无效步骤<<')        
        else:
            print('>>无效步骤<<')
    return hh,Tb,sb,Q,soul,key,money,js,xmzs                 
def zdxl(life2,tools,soul,gwhd):
    print('怪物血量:',life2)
    print('怪物护盾:',gwhd)
    print('工具栏:',tools,'精华:',soul)
def chju(money,js,key,soul,cj,bf,lj):
    if money>8:
        print('\获得成就:钱多不压身/')
    if js>4:
        print('\获得成就:怪物猎手/')
    if key>5:
        print('\获得成就:无锁畏惧/')
    if soul>9:
        print('\获得成就:元气满满/')
    if cj>4:
        print('\获得成就:考古专家/')
    if bf>5:
        print('\获得成就:变废为宝/')
    if lj>5:
        print('\获得成就:垃圾大王/')
def sdzt(tools,money):
    print('工具栏:',tools)
    print('金币:',money)
    print('|购买成功|')
    return tools,money
def sy():
    if '神秘眼镜ee' in dj:
        for i in range(5):
            sight[i]=s[x-2+i][y-4:y+5]
            print(sight[i])
    else:
        for i in range(3):
            sight[i+1]=s[x-1+i][y-2:y+3]
            print(sight[i+1])
def SY():
    for i in range(7):
        Sight[i]=s[x-3+i][y-6:y+7]
        print(Sight[i])
def zlp(key,money,tools,gw,xmzs):
    print('>你获得了战利品<')
    rr=randint(1,5)
    if 1<=rr<=2:
            print('[钥匙+2]')
            key+=2            
    if 2<=rr<=4:
            print('[金币+3]')
            money+=3
    if rr==3:
            print('[获得长矛]')
            tools['/']+=2
    if rr==4 or rr==1:
            print('[获得盾牌]')
            tools['[]']+=2
    if 3<rr<=5:
            print('[获得弩箭]')
            tools['=}']+=2
    if gw=='&':
        if randint(1,3)==1:
            if '护身符δ' not in dj:
                dj['护身符δ']=dj.get('护身符δ',0)+1
                print('[获得护身符]')
        if randint(1,3)==2:
            if not xmzs:
                xmzs=True
                print('|无意间你学会了血魔之手|')
        wq['3:奶盾[+]']=wq.get('3:奶盾[+]',0)+3
        print('获得奶盾*3')
        wq['5:钩爪=~3']=wq.get('5:钩爪=~3',0)+3
        print('获得钩爪*3')        
    if gw=='%':
        wq['6:重盾{:}']=wq.get('6:重盾{:}',0)+4
        print('[获得重盾*4]')
        wq['1:长剑+--']=wq.get('1:长剑+--',0)+4
        print('[获得长剑*4]')
        wq['2:弩炮=<}']=wq.get('2:弩炮=<}',0)+4
        print('[获得弩炮*4]')
    if gw=='W':
        print('[金币+10]')
        money+=10
        print('[获得炸弹*2]')
        dj['1.炸弹Q']=dj.get('1.炸弹Q',0)+2
        print('\获得成就:地牢勇士/')
    return key,money,tools,xmzs        
def ww(x,y,m,n,key,life,money,soul,tools,js,cj,bf,lj,TB,wzsy,dscj,ngqj,xmzs,T5g):
    if s[m][n]==' ':
        s[m]=s[m][0:n]+player+s[m][n+1:]
        s[x]=s[x][0:y]+' '+s[x][y+1:]
        x,y=m,n 
    elif s[m][n]=='M':
        print('您进入了铁匠铺,请选择您要合成的装备')
        print('每次合成消耗一点精华')
        K=True
        while K:
            print('1:长矛/;2:盾牌[];3:弩箭=};4:镐子T')
            print('输入两个序号(如:12;可以合成长矛和盾牌)(如果不合成，则输入0)')
            HC=input('序号:')
            if HC=='14' or HC=='41':
                if  soul>0 and tools['/']>0 and tools['T']>0:
                    soul-=1
                    tools['/']-=1
                    tools['T']-=1
                    print('/'+'+'+'T')
                    print('合成长剑+--')
                    wq['1:长剑+--']=wq.get('1:长剑+--',0)+3
                else:
                    print('>>材料不足<<')
            elif HC=='34' or HC=='43':
                if  soul>0 and tools['=}']>0 and tools['T']>0:
                    soul-=1
                    tools['=}']-=1
                    tools['T']-=1
                    print('=}'+'+'+'T')
                    print('合成弩炮=<}')
                    wq['2:弩炮=<}']=wq.get('2:弩炮=<}',0)+3
                else:
                    print('>>材料不足<<')        
            elif HC=='24' or HC=='42':        
                if  soul>0 and tools['[]']>0 and tools['T']>0:
                    soul-=1
                    tools['[]']-=1
                    tools['T']-=1
                    print('[]'+'+'+'T')
                    print('合成奶盾[+]')
                    wq['3:奶盾[+]']=wq.get('3:奶盾[+]',0)+3
                else:
                    print('>>材料不足<<')
            elif HC=='12' or HC=='21':
                if  soul>0 and tools['/']>0 and tools['[]']>0:
                    soul-=1
                    tools['/']-=1
                    tools['[]']-=1
                    print('/'+'+'+'[]')
                    print('合成砍刀->>')
                    wq['4:砍刀->>']=wq.get('4:砍刀->>',0)+2
                else:
                    print('>>材料不足<<')
            elif HC=='13' or HC=='31':
                if  soul>0 and tools['/']>0 and tools['=}']>0:
                    soul-=1
                    tools['/']-=1
                    tools['=}']-=1
                    print('/'+'+'+'=}')
                    print('合成钩爪=~3')
                    wq['5:钩爪=~3']=wq.get('5:钩爪=~3',0)+2
                else:
                    print('>>材料不足<<')
            elif HC=='32' or HC=='23':
                if  soul>0 and tools['=}']>0 and tools['[]']>0:
                    soul-=1
                    tools['=}']-=1
                    tools['[]']-=1
                    print('=}'+'+'+'[]')
                    print('合成重盾{:}')
                    wq['6:重盾{:}']=wq.get('6:重盾{:}',0)+2
                else:
                    print('>>材料不足<<')        
            elif HC=='0':
                K=False
            else:
                print('>>无效步骤<<')        
    elif s[m][n]=='@':
        print('您进入了魔法祭台,请选择您想学习的法术')
        D=True
        while D:
            print('1:无中生有=6精华 ;2:隐身咒语=5精华;3:血魔之手=9精华')
            print('4:点石成金=6精华 ;5:能工巧匠=9精华;6:元素萃取=9精华')
            print('精华:',soul)
            buy=input('序号:')
            if buy=='1':
                if soul-6<0:
                    print('>>精华不够<<')
                elif wzsy:
                    print('>>不能重复学习<<')
                else: 
                    soul-=6
                    wzsy=True
                    print('精华:',soul)
                    print('|学习成功|')
            elif buy=='2':
                if soul-5<0:
                    print('>>精华不够<<')
                elif TB:
                    print('>>不能重复学习<<')    
                else: 
                    soul-=5
                    TB=True
                    print('精华:',soul)
                    print('|学习成功|')
            elif buy=='3':
                if soul-9<0:
                    print('>>精华不够<<')
                elif xmzs:
                    print('>>不能重复学习<<')
                else: 
                    soul-=9
                    xmzs=True
                    print('精华:',soul)
                    print('|学习成功|')
            elif buy=='4':
                if soul-6<0:
                    print('>>精华不够<<')
                elif dscj:
                    print('>>不能重复学习<<')    
                else:
                    soul-=6
                    dscj=True
                    print('精华:',soul)
                    print('|学习成功|')
            elif buy=='5':
                if soul-9<0:
                    print('>>精华不够<<')
                elif ngqj:
                    print('>>不能重复学习<<')    
                else:
                    soul-=9
                    ngqj=True
                    print('精华:',soul)
                    print('|学习成功|')
            elif buy=='6':
                if soul-9<0:
                    print('>>精华不够<<')
                elif fp!={}:
                    print('>>不能重复学习<<')    
                else:
                    soul-=9
                    fp[0]=1
                    print('精华:',soul)
                    print('|学习成功|')
            else:
                D=False
    elif s[m][n]=='B':
        if tools['T']==0:
            print(">这是墙,走不通<")
        if tools['T']>0:
            zq=input('请你选择是否要凿开墙壁(yes或no):')
            if zq=='yes':
                tools['T']-=1
                if dscj:
                    if randint(0,2)!=0:
                        print('|挖出金币|')
                        cj+=1
                        money+=1
                s[m]=s[m][0:n]+' '+s[m][n+1:]
    elif s[m][n]=='G':
        print('您进入了神秘商店，请挑选您想购买的道具')
        d=True
        while d:
            print('1:/长矛=1金币 ;2:[]盾牌=1金币;3:=}弩箭=1金币')
            print('4:T镐子=2金币 ;5:0 血瓶=2金币;6:ee神秘眼镜=5金币')
            print('金币:',money)
            buy=input('商品序号:')
            if buy=='1':
                if money-1<0:
                    print('>>钱不够<<')
                else: 
                    money-=1
                    tools['/']+=1
                    tools,money=sdzt(tools,money)
            elif buy=='2':
                if money-1<0:
                    print('>>钱不够<<')
                else:
                    money-=1
                    tools['[]']+=1
                    tools,money=sdzt(tools,money)
            elif buy=='3':
                if money-1<0:
                    print('>>钱不够<<')
                else:
                    money-=1
                    tools['=}']+=1
                    tools,money=sdzt(tools,money)
            elif buy=='4':
                if money-2<0:
                    print('>>钱不够<<')
                else:
                    money-=2
                    tools['T']+=1
                    tools,money=sdzt(tools,money)
            elif buy=='5':
                if money-2<0:
                    print('>>钱不够<<')
                else:
                    money-=2
                    life.append(0)
                    print('金币:',money)
                    print('|购买成功|')        
            elif buy=='6':
                if money-5<0:
                    print('>>钱不够<<')
                elif '神秘眼镜ee' in dj:
                    print('>你已经拥有该装备<')
                else:
                    money-=5
                    dj['神秘眼镜ee']=dj.get('神秘眼镜ee',0)+1
                    print('金币:',money)
                    print('|购买成功|')
            else:
                d=False
    elif s[m][n]=='g':
        print('你遇到了神秘商人')
        print('神秘商人:“你好!我的朋友。请问你需要什么?”')
        dd=True
        while dd:
            gg=input('选项:1:交易;2:对话;3:离开  :')
            if gg=='1':
                print('1:地图=3钥匙;2:T镐子=1金币(上限五个)')
                gbuy=input('商品序号(如果不购买，则输入0):')
                if gbuy=='1':
                    if key-3<0:
                        print('>>钥匙不够<<')
                    else: 
                        key-=3
                        print('|购买成功|')
                        for gi in range(0,len(s)):
                            print(s[gi])
                elif gbuy=='2':
                    if money-1<0:
                        print('>>钱不够<<')
                    if T5g>4:
                        print('>已达购买上限<')
                    else:
                        money-=1
                        tools['T']+=1
                        T5g+=1
                        tools,money=sdzt(tools,money)
                elif gbuy=='0':
                    dd=False
                else:
                    print('>>无效步骤<<')
            elif gg=='2':
                gd=True
                while gd:
                    print('------------------')
                    print('1:关于地牢;2:关于商人')
                    print('3:关于僵尸;4:关于异兽;5:关于骷髅')
                    gcon=input('序号(回车退出):')
                    if gcon=='1':
                        print(player+':这地牢是什么来历?')
                        print('神秘商人:这里以前其实是一座繁华的地下城邦。')
                        time.sleep(1.7)
                        print('神秘商人:其科技水平和魔法造诣远超我们。')
                        time.sleep(1.7)
                        print('神秘商人:但是之后因为一些未知的原因衰败了。')
                        time.sleep(1.7)
                    elif gcon=='2':
                        print(player+':你为什么在这里?')
                        print('神秘商人:我跟你一样,都是来这里探索的冒险家。')
                        time.sleep(1.6)
                        print('神秘商人:不过显然。')
                        time.sleep(0.8)
                        print('神秘商人:我来得比你早得多。')
                        time.sleep(1.0)
                    elif gcon=='3':
                        print('神秘商人:僵尸是个缠人的家伙。')
                        time.sleep(1.2)
                        print('神秘商人:闻着味就会赶来吃你。')
                        time.sleep(1.2)
                        print('神秘商人:不过你可以在异兽的肚子里找到护身符。')
                        time.sleep(1.7)
                        print('神秘商人:因为它们曾吃了不少魔法学院的人。')
                        time.sleep(1.6)
                    elif gcon=='4':
                        print('神秘商人:这些异兽毫无疑问,都是从地上跑来在这地牢里栖身的。')
                        time.sleep(2.1)
                        print('神秘商人:这种生物生命力极其顽强。')
                        time.sleep(1.5)
                        print('神秘商人:无论在世界的哪一个角落。')
                        time.sleep(1.5)
                        print('神秘商人:你都能看到它们的身影。')
                        time.sleep(1.5)
                    elif gcon=='5':
                        print(player+':哪些骷髅...')
                        print('神秘商人:有人说那是逃亡的落魄骑士的残骸。')
                        time.sleep(1.7)
                        print('神秘商人:也有人说那是曾经古老城邦的士兵。')
                        time.sleep(1.7)
                        print('神秘商人:总之,我建议你不要去接近那被诅咒的邪物。')
                        time.sleep(1.9)
                    else:
                        gd=False
            elif gg=='3':
                dd=False
            else:
                print('>>无效步骤<<')
    elif s[m][n]=='W':
        print('你发现了一些奇怪机械')
        print('请你选择是否要前去观察')
        aa=input('请输入yes或no:')
        if aa=='no':
            print('你选择了离开')
        else:
            print('>钢铁零件开始震动<')
            print('你唤醒了古城守卫')
            print('你进入了一场战斗')
            print('{       V  }')
            print('{ '+player+' '+'vs'+' '+'/W\ }')
            life2=[0,0,0,0,0,0,0,0,0,0,0,0]
            gwhd=['[]','[]','[]','[]','[]','[]']
            print('怪物血量:',life2)
            print('怪物护盾:',gwhd)
            Tb=7
            if TB:
                Tb=12
            hh=0
            Q=True
            while Q:
                R1=randint(1,12);R2=randint(1,12);R3=randint(1,12);R4=randint(1,12)
                hh,Tb,sb,Q,soul,key,money,js,xmzs=playerfight(hh,R1,R4,Tb,Q,soul,m,n,x,y,key,money,tools,js,dj,life2,gwhd,xmzs)
                if hh==1:
                    print('>--------<')
                    print('古城守卫的回合')                    
                    if R2<=3:
                        print('>>古城守卫劈下了重剑')
                        print('W +=> 5-')
                        if sb:
                            if R3<=7:
                                print('|你闪避成功了|')
                                if wzsy:
                                    print('|触发无中生有|')
                                    print('[获得长矛]')
                                    tools['/']+=2
                                    print('[获得弩箭]')
                                    tools['=}']+=2
                                    print('[获得盾牌]')
                                    tools['[]']+=2
                                hh=0
                            else:
                                print('>>你闪避失败了<<')
                                if tools['[]']>0:
                                    print('|你有盾牌，抵挡了一点伤害|')
                                    life.pop()
                                    tools['[]']-=1
                                    print('工具栏:',tools)
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    print('你的精力值:',life)
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    hh=0
                                else:
                                    print('>>你遭受五点攻击<<')
                                    life.pop()
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    print('你的精力值:',life)
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    
                                    hh=0
                        else:
                            if tools['[]']>0:
                                print('|你有盾牌，抵挡了一点伤害|')
                                tools['[]']-=1
                                print('工具栏:',tools)
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                print('你的精力值:',life)
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break                                    
                                hh=0
                            else:
                                print('>>你遭受五点攻击<<')
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                print('你的精力值:',life)
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break                                    
                                hh=0
                    if 4<=R2<=6:
                        print('>>古城守卫发射了火炮')
                        print('W X== 3-')
                        if sb:
                            if R3<=6:
                                print('|你闪避成功了|')
                                if wzsy:
                                    print('[获得长矛]')
                                    tools['/']+=2                                  
                                    print('[获得弩箭]')
                                    tools['=}']+=2
                                    print('[获得盾牌]')
                                    tools['[]']+=2
                                hh=0
                            else:
                                print('>>你闪避失败了<<')
                                if tools['[]']>0:
                                    print('|你有盾牌，抵挡了一点伤害|')
                                    tools['[]']-=1
                                    print('工具栏:',tools)
                                    life.pop()
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    print('你的精力值:',life)
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    hh=0
                                else:
                                    print('>>你遭受三点攻击<<')
                                    life.pop()
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    print('你的精力值:',life)
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    hh=0
                        else:
                            if tools['[]']>0:
                                print('|你有盾牌，抵挡了一点伤害|')
                                tools['[]']-=1
                                print('工具栏:',tools)
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                print('你的精力值:',life)
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break         
                                hh=0
                            else:
                                print('>>你遭受三点攻击<<')
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                print('你的精力值:',life)
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                hh=0                        
                    if 7<=R2<=9:
                        print('>>古城守卫启动了能量脉冲')
                        print('W XΣ＝ 4-')
                        if sb:
                            if R3<=9:
                                print('|你闪避成功了|')
                                if wzsy:
                                    print('|触发无中生有|')
                                    print('[获得长矛]')
                                    tools['/']+=2
                                    print('[获得弩箭]')
                                    tools['=}']+=2
                                    print('[获得盾牌]')
                                    tools['[]']+=2
                                hh=0
                            else:
                                print('>>你闪避失败了<<')
                                if tools['[]']>0:
                                    print('|你有盾牌，抵挡了一点伤害|')
                                    tools['[]']-=1
                                    life.pop()
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    print('你的精力值:',life)
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    print('工具栏:',tools)
                                    hh=0
                                else:
                                    print('>>你遭受四点攻击<<')
                                    life.pop()
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    print('你的精力值:',life)
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    hh=0
                        else:
                            if tools['[]']>0:
                                print('|你有盾牌，抵挡了一点伤害|')
                                tools['[]']-=1
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                print('工具栏:',tools)
                                print('你的精力值:',life)        
                                hh=0
                            else:
                                print('>>你遭受四点攻击<<')
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                print('你的精力值:',life)
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                hh=0
                    if 6<=R2<=10:
                        print('>>一股远古的力量侵袭了你')
                        if soul-6<0:
                            soul=0
                            print('>>你的精华已经耗尽')
                            print('>>你损失一点精力值')
                            life.pop()
                            print('你的精力值:',life)
                            if len(life)<=0:
                                print('>>你精力值没了<<')
                                break
                        else:
                            print('>>你的精华流失了')
                            soul-=6
                            print('soul:'+str(soul))
                        hh=0
                    if 10<=R2<=12 and len(life2)<=6:
                        print('>>古城守卫使用了洞察之心')
                        print('W (φ) ')
                        print('你的护盾被消解了')
                        tools['[]']=0
                        print('工具栏:',tools)
                        hh=0
                    if  10<=R2<=12 and len(life2)>4:
                        print('>>古城守卫恢复了护盾')
                        print('W {Ψ} +[]*2')
                        gwhd.append('[]')
                        gwhd.append('[]')
                        print('怪物护盾:',gwhd)
                        hh=0  
    
    
    elif s[m][n]=='%':
        print('你发现了一具带盔甲的骷髅')
        print('请你选择是否要拿走它的盔甲')
        aa=input('请输入yes或no:')
        if aa=='no':
            print('你选择了收手')
        else:
            print('你唤醒了骷髅骑士')
            print('你进入了一场战斗')
            print('{ '+player+' '+'vs'+' '+'%'+' }')
            life2=[0,0,0,0,0]
            gwhd=['[]','[]','[]']
            print('怪物血量:',life2)
            print('怪物护盾:',gwhd)
            Tb=7
            if TB:
                Tb=12
            hh=0
            Q=True
            while Q:
                R1=randint(1,12);R2=randint(1,12);R3=randint(1,12);R4=randint(1,12)
                hh,Tb,sb,Q,soul,key,money,js,xmzs=playerfight(hh,R1,R4,Tb,Q,soul,m,n,x,y,key,money,tools,js,dj,life2,gwhd,xmzs)
                if hh==1:
                    print('>--------<')
                    print('骷髅骑士的回合')                    
                    if R2<=2:
                        print('>>骷髅骑士发出了暴击(三点)')
                        print('% +== 3-')
                        if sb:
                            if R3<=7:
                                print('|你闪避成功了|')
                                if wzsy:
                                    print('|触发无中生有|')
                                    print('[获得长矛]')
                                    tools['/']+=2
                                    print('[获得弩箭]')
                                    tools['=}']+=2
                                    print('[获得盾牌]')
                                    tools['[]']+=2
                                hh=0
                            else:
                                print('>>你闪避失败了<<')
                                if tools['[]']>0:
                                    print('|你有盾牌，抵挡了一点伤害|')
                                    life.pop()
                                    tools['[]']-=1
                                    print('工具栏:',tools)
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    print('你的精力值:',life)
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    hh=0
                                else:
                                    print('>>你遭受三点攻击<<')
                                    life.pop()
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    print('你的精力值:',life)
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    hh=0
                        else:
                            if tools['[]']>0:
                                print('|你有盾牌，抵挡了一点伤害|')
                                tools['[]']-=1
                                print('工具栏:',tools)
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                print('你的精力值:',life)
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break         
                                hh=0
                            else:
                                print('>>你遭受三点攻击<<')
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                print('你的精力值:',life)
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                hh=0
                    if 3<=R2<=4:
                        print('>>骷髅骑士发出了攻击(两点)')
                        print('%'+' '+'+=='+' '+'2-')
                        if sb:
                            if R3<=8:
                                print('|你闪避成功了|')
                                if wzsy:
                                    print('|触发无中生有|')
                                    print('[获得长矛]')
                                    tools['/']+=2
                                    print('[获得弩箭]')
                                    tools['=}']+=2
                                    print('[获得盾牌]')
                                    tools['[]']+=2 
                                hh=0
                            else:
                                print('>>你闪避失败了<<')
                                if tools['[]']>0:
                                    print('|你有盾牌，抵挡了一点伤害|')
                                    tools['[]']-=1
                                    print('工具栏:',tools)
                                    life.pop()
                                    print('你的精力值:',life)
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    hh=0
                                else:
                                    print('>>你遭受两点攻击<<')
                                    life.pop()
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    print('你的精力值:',life)
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    hh=0
                        else:
                            if tools['[]']>0:
                                print('|你有盾牌，抵挡了一点伤害|')
                                tools['[]']-=1
                                print('工具栏:',tools)
                                life.pop()
                                print('你的精力值:',life)
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break         
                                hh=0
                            else:
                                print('>>你遭受两点攻击<<')
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                print('你的精力值:',life)
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                hh=0                        
                    if 5<=R2<=9:
                        print('>>骷髅骑士发出了攻击(一点)')
                        print('%'+' '+'+=='+' '+'1-')
                        if sb:
                            if R3<=9:
                                print('|你闪避成功了|')
                                if wzsy:
                                    print('|触发无中生有|')
                                    print('[获得长矛]')
                                    tools['/']+=2
                                    print('[获得弩箭]')
                                    tools['=}']+=2
                                    print('[获得盾牌]')
                                    tools['[]']+=2  
                                hh=0
                            else:
                                print('>>你闪避失败了<<')
                                if tools['[]']>0:
                                    print('|你有盾牌，抵挡了伤害|')
                                    tools['[]']-=1
                                    print('工具栏:',tools)
                                    print('你的精力值:',life)
                                    hh=0
                                else:
                                    print('>>你遭受一点攻击<<')
                                    life.pop()
                                    print('你的精力值:',life)
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    hh=0
                        else:
                            if tools['[]']>0:
                                print('|你有盾牌，抵挡了伤害|')
                                tools['[]']-=1
                                print('工具栏:',tools)
                                print('你的精力值:',life)        
                                hh=0
                            else:
                                print('>>你遭受一点攻击<<')
                                life.pop()
                                print('你的精力值:',life)
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                hh=0
                    if 8<=R2<=12:
                        print('>>骷髅骑士举起了盾牌')
                        print('% {:} +[]')
                        gwhd.append('[]')
                        hh=0
                        print('怪物护盾:',gwhd)
                    if R2==4 or R2==6:
                        print('>>骷髅骑士使用了翻滚')
                        print('% ~~')
                        print('|触发连击|')
                        hh=1                               
    elif s[m][n]=='&':
        print('一只沉睡的异兽堵住了你的去路')
        print('请你选择是否要攻击它')
        aa=input('请输入yes或no:')
        if aa=='no':
            print('你选择了撤退')
        else:
            print('你进入了一场战斗')
            print('{ '+player+' '+'vs'+' '+'&'+' }')
            life2=[0,0,0,0,0,0]
            gwhd=[]
            print('怪物血量:',life2)
            print('怪物护盾:',gwhd)
            Tb=7
            if TB:
                Tb=12
            hh=0
            Q=True
            while Q:
                R1=randint(1,12);R2=randint(1,12);R3=randint(1,12);R4=randint(1,12)
                hh,Tb,sb,Q,soul,key,money,js,xmzs=playerfight(hh,R1,R4,Tb,Q,soul,m,n,x,y,key,money,tools,js,dj,life2,gwhd,xmzs)
                if hh==1:
                    print('>--------<')
                    print('异兽的回合')                    
                    if R2<=5:
                        print('>>异兽发出了攻击')
                        print('&'+' '+'->'+' '+'2-')
                        if sb:
                            if R3<=7:
                                print('|你闪避成功了|')
                                if wzsy:
                                    print('|触发无中生有|')
                                    print('[获得长矛]')
                                    tools['/']+=2
                                    print('[获得弩箭]')
                                    tools['=}']+=2
                                    print('[获得盾牌]')
                                    tools['[]']+=2  
                                hh=0
                            else:
                                print('>>你闪避失败了<<')
                                if tools['[]']>0:
                                    print('|你有盾牌，抵挡了一点伤害|')
                                    life.pop()
                                    tools['[]']-=1
                                    print('工具栏:',tools)
                                    print('你的精力值:',life)
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break                                                                              
                                    hh=0
                                else:
                                    print('>>你遭受两点攻击<<')
                                    life.pop()
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    life.pop()
                                    print('你的精力值:',life)
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    hh=0
                        else:
                            if tools['[]']>0:
                                print('|你有盾牌，抵挡了一点伤害|')
                                life.pop()
                                tools['[]']-=1
                                print('工具栏:',tools)
                                print('你的精力值:',life)
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break         
                                hh=0
                            else:
                                print('>>你遭受两点攻击<<')
                                life.pop()
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                life.pop()
                                print('你的精力值:',life)
                                if len(life)<=0:
                                    print('>>你精力值没了<<')
                                    break
                                hh=0
                    if 6<=R2<=9:
                        print('>>异兽使用了吸血')
                        print('&'+' '+'>>'+' '+'1-')
                        if sb:
                            if R3<8:
                                print('|你闪避成功了|')
                                if wzsy:
                                    print('|触发无中生有|')
                                    print('[获得长矛]')
                                    tools['/']+=2
                                    print('[获得弩箭]')
                                    tools['=}']+=2
                                    print('[获得盾牌]')
                                    tools['[]']+=2
                                hh=0
                            else:
                                print('>>你闪避失败了<<')
                                if tools['[]']>0:
                                    print('|你有盾牌，抵挡了伤害|')
                                    tools['[]']-=1
                                    print('工具栏:',tools)
                                    print('你的精力值:',life)
                                    hh=0
                                else:
                                    print('>>你遭受吸血,异兽血量+1<<')
                                    life.pop()
                                    life2.append(0)
                                    print('异兽血量:',life2)
                                    print('你的精力值:',life)
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    hh=0
                        else:
                            if tools['[]']>0:
                                tools['[]']-=1
                                print('|你有盾牌，抵挡了伤害|')
                                print('工具栏:',tools)
                                print('你的精力值:',life)
                                hh=0
                            else:
                                print('>>你遭受吸血,异兽血量+1<<')
                                life.pop()
                                life2.append(0)
                                print('异兽血量:',life2)
                                print('你的精力值:',life)
                                if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                hh=0                        
                    if 10<=R2:
                        print('>>异兽进行了回血')
                        print('&'+' '+'0'+' '+'+1')
                        life2.append(0)
                        print('怪物血量:',life2)
                        hh=0
    elif s[m][n]=='Z':
        print('一只僵尸堵住了你的去路')
        print('请你选择是否要攻击它')
        aa=input('请输入yes或no:')
        if aa=='no':
            print('你选择了撤退')
        else:
            print('你进入了一场战斗')
            print('{ '+player+' '+'vs'+' '+'Z'+' }')
            life2=[0,0,0,0]
            gwhd=['[]','[]']
            print('怪物血量:',life2)
            print('怪物护盾:',gwhd)
            Tb=7
            if TB:
                Tb=12
            hh=0
            Q=True
            while Q:
                R1=randint(1,12);R2=randint(1,12);R3=randint(1,12);R4=randint(1,12)
                hh,Tb,sb,Q,soul,key,money,js,xmzs=playerfight(hh,R1,R4,Tb,Q,soul,m,n,x,y,key,money,tools,js,dj,life2,gwhd,xmzs)
                if hh==1:
                    print('>--------<')
                    print('僵尸的回合')                    
                    if R2<=5:
                        print('>>僵尸进行了发呆')
                        hh=0
                    if 6<=R2:
                        print('>>僵尸进行了攻击')
                        print('Z'+' '+'->'+' '+'1-')
                        if sb:
                            if R3<6:
                                print('|你闪避成功了|')
                                if wzsy:
                                    print('|触发无中生有|')
                                    print('[获得长矛]')
                                    tools['/']+=2
                                    print('[获得弩箭]')
                                    tools['=}']+=2
                                    print('[获得盾牌]')
                                    tools['[]']+=2
                                hh=0
                            else:
                                print('>>你闪避失败了<<')
                                if tools['[]']>0:
                                    print('|你有盾牌，抵挡了伤害|')
                                    tools['[]']-=1
                                    print('工具栏:',tools)
                                    print('你的精力值:',life)
                                    hh=0
                                else:
                                    print('>>你遭受一点攻击<<')
                                    life.pop()
                                    zr=randint(1,3)
                                    if zr==1:
                                        if money>1:
                                            money-=2
                                            print('>>你丢失两枚金币<<')
                                    if zr==2:
                                        if key>1:
                                            key-=2
                                            print('>>你丢失两把钥匙<<')
                                    if zr==3:
                                        if money>0 and key>0:
                                            key-=1;money-=1
                                            print('>>你丢失一枚金币和一把钥匙<<')                      
                                    print('僵尸血量:',life2)
                                    print('你的精力值:',life)
                                    if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                    hh=0
                        else:
                            if tools['[]']>0:
                                tools['[]']-=1
                                print('|你有盾牌，抵挡了伤害|')
                                print('工具栏:',tools)
                                print('你的精力值:',life)
                                hh=0
                            else:
                                print('>>你遭受一点攻击<<')
                                life.pop()
                                zr=randint(1,3)
                                if zr==1:
                                    if money>1:
                                        money-=2
                                        print('>>你丢失两枚金币<<')
                                if zr==2:
                                    if key>1:
                                        key-=2
                                        print('>>你丢失两把钥匙<<')
                                if zr==3:
                                    if money>0 and key>0:
                                        key-=1;money-=1
                                        print('>>你丢失一枚金币和一把钥匙<<')
                                print('僵尸血量:',life2)
                                print('你的精力值:',life)
                                if len(life)<=0:
                                        print('>>你精力值没了<<')
                                        break
                                hh=0                                              
    elif s[m][n]=='Q':
        drzd=input('是否点燃炸弹(yes or no):')
        if drzd=='yes':
            if soul-2>0 and key>0:
                soul-=3;key-=1
                print('|爆炸成功|')
                s[m]=s[m][0:n]+' '+s[m][n+1:]
                if f=='d':
                    if s[m-1][n-2] not in 'XW#':
                        s[m-1]=s[m-1][0:n-2]+' '+s[m-1][n-1:]
                    if s[m-1][n+2] not in 'XW#':
                        s[m-1]=s[m-1][0:n+2]+' '+s[m-1][n+3:]
                    if s[m+1][n-2] not in 'XW#':
                        s[m+1]=s[m+1][0:n-2]+' '+s[m+1][n-1:]
                    if s[m+1][n+2] not in 'XW#':
                        s[m+1]=s[m+1][0:n+2]+' '+s[m+1][n+3:]                        
                    if s[m-1][n] not in 'XW#':
                        s[m-1]=s[m-1][0:n]+' '+s[m-1][n+1:]
                    if s[m+1][n] not in 'XW#':
                        s[m+1]=s[m+1][0:n]+' '+s[m+1][n+1:]
                    if s[m][n+2] not in 'XW#':
                        s[m]=s[m][0:n+2]+' '+s[m][n+3:]
                elif f=='s':
                    if s[m-1][n-2] not in 'XW#':
                        s[m-1]=s[m-1][0:n-2]+' '+s[m-1][n-1:]
                    if s[m-1][n+2] not in 'XW#':
                        s[m-1]=s[m-1][0:n+2]+' '+s[m-1][n+3:]
                    if s[m+1][n-2] not in 'XW#':
                        s[m+1]=s[m+1][0:n-2]+' '+s[m+1][n-1:]
                    if s[m+1][n+2] not in 'XW#':
                        s[m+1]=s[m+1][0:n+2]+' '+s[m+1][n+3:]                        
                    if s[m+1][n-2] not in 'XW#':
                        s[m+1]=s[m+1][0:n-2]+' '+s[m+1][n-1:]
                    if s[m+1][n] not in 'XW#':
                        s[m+1]=s[m+1][0:n]+' '+s[m+1][n+1:]
                    if s[m][n+2] not in 'XW#':
                        s[m]=s[m][0:n+2]+' '+s[m][n+3:]
                elif f=='a':
                    if s[m-1][n-2] not in 'XW#':
                        s[m-1]=s[m-1][0:n-2]+' '+s[m-1][n-1:]
                    if s[m-1][n+2] not in 'XW#':
                        s[m-1]=s[m-1][0:n+2]+' '+s[m-1][n+3:]
                    if s[m+1][n-2] not in 'XW#':
                        s[m+1]=s[m+1][0:n-2]+' '+s[m+1][n-1:]
                    if s[m+1][n+2] not in 'XW#':
                        s[m+1]=s[m+1][0:n+2]+' '+s[m+1][n+3:]                        
                    if s[m-1][n] not in 'XW#':
                        s[m-1]=s[m-1][0:n]+' '+s[m-1][n+1:]
                    if s[m+1][n] not in 'XW#':
                        s[m+1]=s[m+1][0:n]+' '+s[m+1][n+1:]
                    if s[m][n-2] not in 'XW#':
                        s[m]=s[m][0:n-2]+' '+s[m][n-1:]
                elif f=='w':
                    if s[m-1][n-2] not in 'XW#':
                        s[m-1]=s[m-1][0:n-2]+' '+s[m-1][n-1:]
                    if s[m-1][n+2] not in 'XW#':
                        s[m-1]=s[m-1][0:n+2]+' '+s[m-1][n+3:]
                    if s[m+1][n-2] not in 'XW#':
                        s[m+1]=s[m+1][0:n-2]+' '+s[m+1][n-1:]
                    if s[m+1][n+2] not in 'XW#':
                        s[m+1]=s[m+1][0:n+2]+' '+s[m+1][n+3:]                        
                    if s[m-1][n] not in 'XW#':
                        s[m-1]=s[m-1][0:n]+' '+s[m-1][n+1:]
                    if s[m][n-2] not in 'XW#':
                        s[m]=s[m][0:n-2]+' '+s[m][n-1:]
                    if s[m][n+2] not in 'XW#':
                        s[m]=s[m][0:n+2]+' '+s[m][n+3:]                        
            else:
                print('>>材料不足<<')                    
    elif s[m][n]=='*':
        s[m]=s[m][0:n]+player+s[m][n+1:]
        s[x]=s[x][0:y]+' '+s[x][y+1:]
        print('[精华+1]')
        soul+=1
        x,y=m,n        
    elif s[m][n]=='^':
        s[m]=s[m][0:n]+player+s[m][n+1:]
        s[x]=s[x][0:y]+' '+s[x][y+1:]
        print('[钥匙+1]')
        key+=1
        x,y=m,n
    elif s[m][n]=='?':
        s[m]=s[m][0:n]+player+s[m][n+1:]
        s[x]=s[x][0:y]+' '+s[x][y+1:]
        x,y=m,n
        print('>你翻了翻垃圾堆<')
        rr=randint(1,14)
        if fp!={}:
            rr=randint(9,12)
        if rr<=4:
            print('[金币+1]')
            money+=1
            bf+=1
        if 5<=rr<=9:
            print('[你什么都没发现,精力值-1]')
            lj+=1
            life.pop()
        if 10<=rr<=11:
            print('[金币+2]')
            bf+=1
            money+=2
        if 12<=rr<=13:
            print('[钥匙+1]')
            bf+=1
            key+=1
        if rr==14:
            print('[镐子+1]')
            tools['T']+=1
    elif s[m][n]=='$':
         if key>0:
             s[m]=s[m][0:n]+player+s[m][n+1:]
             s[x]=s[x][0:y]+' '+s[x][y+1:]
             print('>你打开了宝箱<')
             if ngqj:
                 if randint(0,1)!=0:
                     print('|触发能工巧匠,不消耗钥匙|')
                 else:
                     key-=1
             else:
                 key-=1   
             x,y=m,n
             r5=randint(1,20)
             if r5<=3:
                 print('[金币+1]')
                 money+=2
             elif 4<=r5<=9:
                 print('[你发现了血瓶,精力值+1]')
                 life.append(0)
             elif 10<=r5<=15:
                 print('[金币+2]')
                 money+=3
             elif r5==16:
                 if '神秘眼镜ee' in dj:
                     print('[金币+4]')
                     money+=4
                 else:
                     print('[获得神秘眼镜]')
                     dj['神秘眼镜ee']=dj.get('神秘眼镜ee',0)+1
             elif 17<=r5<=20:
                 print('[获得长矛,盾牌,弩箭]')
                 tools['/']+=1;tools['[]']+=1;tools['=}']+=1
         else:
             print('>>没钥匙<<')
    elif s[m][n]=='w':
        print('>这是篝火<')
    elif s[m][n]=='i':
        print('>这是一根蜡烛<')
    elif s[m][n]=='I':
        print('>这是火炬<')
    elif s[m][n]=='v':
        print('------------------')
        if 'v' not in fp:
            print('猎人v:新来的冒险家?')
            time.sleep(0.7)
            print('猎人v:这地牢可是很危险的,祝你好运吧!')
            time.sleep(1.0)
            fp['v']=1
        else:
            print('猎人v:……')
            time.sleep(0.4)
    elif s[m][n]=='d':
        print('------------------')
        if 'd' not in fp:            
            print('d:嘿!新来的,想试试我这大炮吗?')
            time.sleep(0.8)
            print('d:抱歉,吓到你了。')
            time.sleep(0.5)
            print('d:我叫Bob,幸会。')
            time.sleep(0.5)
        
    elif s[m][n]=='!':
        print('>不知是谁放在这里的一个宝箱<')
        dk=input('是否打开(yes or no):')
        if dk=='yes':
            s[m]=s[m][0:n]+' '+s[m][n+1:]
            dkk=randint(0,6)
            if 0<=dkk<=1:
                print('>>这是空的<<')
            if dkk==2:
                print('[金币+2]')
                money+=2
            if 3<=dkk<=4:
                wq['1:长剑+--']=wq.get('1:长剑+--',0)+1
                print('[获得一把破锈的长剑]')
            if 5<=dkk<=6:
                print('[获得盾牌*2]')
                tools['[]']+=2        
    return x,y,key,life,money,soul,tools,js,cj,bf,lj,TB,wzsy,dscj,ngqj,xmzs,T5g
def ZDFZ(zdfx):
    if zdfx=='w':
        if s[x-1][y] in 'XW#':
            print('>>无法安装<<')
        else:
            print('|已安置炸弹|')
            dj['1.炸弹Q']-=1
            s[x-1]=s[x-1][0:y]+'Q'+s[x-1][y+1:]
    elif zdfx=='a':
        if s[x][y-2] in 'XW#':
            print('>>无法安装<<')
        else:
            print('|已安置炸弹|')
            dj['1.炸弹Q']-=1
            s[x]=s[x][0:y-2]+'Q'+s[x][y-1:]
    elif zdfx=='s':
        if s[x+1][y] in 'XW#':
            print('>>无法安装<<')
        else:
            print('|已安置炸弹|')
            dj['1.炸弹Q']-=1
            s[x+1]=s[x+1][0:y]+'Q'+s[x+1][y+1:]
    elif zdfx=='d':
        if s[x][y+2] in 'XW#':
            print('>>无法安装<<')
        else:
            print('|已安置炸弹|')
            dj['1.炸弹Q']-=1
            s[x]=s[x][0:y+2]+'Q'+s[x][y+3:]
    else:
        print('>>无效步骤<<')
    return dj
def jrz(x,y,zjr,zx,zy,zydx,zydy):
    zjr=False
    if '护身符δ' in dj:
        zjr=False
    elif s[x-1][y]=='Z':
        print('>>你惊动了僵尸')
        zx=x-1;zy=y
        zydx,zydy=x,y
        zjr=True
    elif s[x+1][y]=='Z':
        print('>>你惊动了僵尸')
        zx=x+1;zy=y
        zydx,zydy=x,y
        zjr=True
    elif s[x][y-2]=='Z':
        print('>>你惊动了僵尸')
        zx=x;zy=y-2
        zydx,zydy=x,y
        zjr=True
    elif s[x][y+2]=='Z':
        print('>>你惊动了僵尸')
        zx=x;zy=y+2
        zydx,zydy=x,y
        zjr=True
    elif s[x+1][y+2]=='Z':
        print('>>你惊动了僵尸')
        zx=x+1;zy=y+2
        zydx,zydy=x,y
        zjr=True
    elif s[x+1][y-2]=='Z':
        print('>>你惊动了僵尸')
        zx=x+1;zy=y-2
        zydx,zydy=x,y
        zjr=True
    elif s[x-1][y+2]=='Z':
        print('>>你惊动了僵尸')
        zx=x-1;zy=y+2
        zydx,zydy=x,y
        zjr=True
    elif s[x-1][y-2]=='Z':
        print('>>你惊动了僵尸')
        zx=x-1;zy=y-2
        zydx,zydy=x,y
        zjr=True
    return zx,zy,zjr,zydx,zydy
def zyd(zx,zy,zydx,zydy):
    if zydx!=x or zydy!=y:
        s[zydx]=s[zydx][0:zydy]+'Z'+s[zydx][zydy+1:]
        s[zx]=s[zx][0:zy]+' '+s[zx][zy+1:]          
flag=False
dl=0
while not flag:
    s=map1
    print('--生成地形中--')
    for I in range(7):
        print('.'*I)
        time.sleep(0.2)
    if dl==0:
        s=map2
        x,y=7,18
        s[x]=s[x][0:y]+player+s[x][y+1:]
        fx=randint(3,6);fy=6
        s[fx]=s[fx][0:fy]+'f'+s[fx][fy+1:]
        s[fx+1]=s[fx+1][0:fy+2]+'i'+s[fx+1][fy+3:]     
        dx=randint(3,6);dy=14
        s[dx]=s[dx][0:dy]+'d'+s[dx][dy+1:]
        js,cj,bf,lj=0,0,0,0
        SY()
    elif (dl+1)%6==0:
        print('你来到一座废弃的战壕')
        s=['X X X X X X X X X',
           'X X X X X X X X X',
           'X X           X X',
           'X X   X W X   X X',
           'X X   W # W   X X',
           'X X   X W X   X X',
           'X X           X X',
           'X X X X X X X X X',
           'X X X X X X X X X']
        dl+=1
        x,y=2,4
        s[x]=s[x][0:y]+player+s[x][y+1:]
        sy()
        js,cj,bf,lj=0,0,0,0
    elif randint(1,3)!=1:         #2,3;怪物较多
        for i in range(2,19):
            for j in range(4,37,2):
                RR=randint(1,289)
                if RR<=134:
                    s[i]=s[i][0:j]+' '+s[i][j+1:]
                if 135<=RR<=144:
                    s[i]=s[i][0:j]+'&'+s[i][j+1:]
                if 145<=RR<=229:
                    s[i]=s[i][0:j]+'B'+s[i][j+1:]
                if 230<=RR<=243:
                    s[i]=s[i][0:j]+'Z'+s[i][j+1:]
                if 244<=RR<=250:
                    s[i]=s[i][0:j]+'^'+s[i][j+1:]
                if 251<=RR<=259:
                    s[i]=s[i][0:j]+'$'+s[i][j+1:]
                if 260<=RR<=261:
                    s[i]=s[i][0:j]+'G'+s[i][j+1:]
                if 262<=RR<=263:
                    s[i]=s[i][0:j]+'@'+s[i][j+1:]
                if 264<=RR<=265:
                    s[i]=s[i][0:j]+'M'+s[i][j+1:]
                if 266<=RR<=266:
                    s[i]=s[i][0:j]+'#'+s[i][j+1:]
                if 267<=RR<=276:
                    s[i]=s[i][0:j]+'%'+s[i][j+1:]
                if 277<=RR<=280:
                    s[i]=s[i][0:j]+'*'+s[i][j+1:]
                if 280<=RR<=289:
                    s[i]=s[i][0:j]+'?'+s[i][j+1:]   
        print('--生成完成--')
        x,y=2,4
        s[x]=s[x][0:y]+player+s[x][y+1:]
        s[17]=s[17][0:32]+'#'+s[17][33:]
        rr=randint(2,3)
        if dl%rr==0:
            gx=randint(5,8)
            gy=22
            s[gx]=s[gx][0:gy]+'g'+s[gx][gy+1:]
        sy()
        js,cj,bf,lj=0,0,0,0
    else:                          #1;奖励较多
        for i in range(2,19):
            for j in range(4,37,2):
                RR=randint(1,289)
                if RR<=154:
                    s[i]=s[i][0:j]+' '+s[i][j+1:]
                if 155<=RR<=174:
                    s[i]=s[i][0:j]+'&'+s[i][j+1:]
                if 175<=RR<=208:
                    s[i]=s[i][0:j]+'B'+s[i][j+1:]
                if 209<=RR<=230:
                    s[i]=s[i][0:j]+'Z'+s[i][j+1:]
                if 231<=RR<=234:
                    s[i]=s[i][0:j]+'^'+s[i][j+1:]
                if 235<=RR<=243:
                    s[i]=s[i][0:j]+'$'+s[i][j+1:]
                if 244<=RR<=245:
                    s[i]=s[i][0:j]+'G'+s[i][j+1:]
                if 246<=RR<=247:
                    s[i]=s[i][0:j]+'@'+s[i][j+1:]
                if 248<=RR<=249:
                    s[i]=s[i][0:j]+'M'+s[i][j+1:]
                if 250<=RR<=250:
                    s[i]=s[i][0:j]+'#'+s[i][j+1:]
                if 251<=RR<=270:
                    s[i]=s[i][0:j]+'%'+s[i][j+1:]
                if 271<=RR<=275:
                    s[i]=s[i][0:j]+'*'+s[i][j+1:]
                if 276<=RR<=289:
                    s[i]=s[i][0:j]+'?'+s[i][j+1:]   
        print('--生成完成--')
        x,y=2,4
        s[x]=s[x][0:y]+player+s[x][y+1:]
        s[17]=s[17][0:32]+'#'+s[17][33:]
        rr=randint(2,3)
        if dl%rr==0:
            gx=randint(5,8)
            gy=22
            s[gx]=s[gx][0:gy]+'g'+s[gx][gy+1:]
        sy()
        js,cj,bf,lj=0,0,0,0
    zx,zy=0,0
    zydx,zydy=0,0
    zjr=False
    T5g=0
    Flag=False
    while not Flag:
        if len(life)<=0:
            print('>>game over<<')
            print('您到达的地牢层数:第'+str(dl)+'层')
            chju(money,js,key,soul,cj,bf,lj)
            flag=True
            break
        zx,zy,zjr,zydx,zydy=jrz(x,y,zjr,zx,zy,zydx,zydy)
        f=input("方向:")
        m,n=0,0
        print('{第'+str(dl)+'层地牢}')
        if f=='w':
            m=x-1
            n=y
            zt()
            x,y,key,life,money,soul,tools,js,cj,bf,lj,TB,wzsy,dscj,ngqj,xmzs,T5g=ww(x,y,m,n,key,life,money,soul,tools,js,cj,bf,lj,TB,wzsy,dscj,ngqj,xmzs,T5g)            
            if dl==0:
                SY()
            else:
                if zjr:
                    zyd(zx,zy,zydx,zydy)
                sy()               
        elif f=='a':
            m=x
            n=y-2
            zt()
            x,y,key,life,money,soul,tools,js,cj,bf,lj,TB,wzsy,dscj,ngqj,xmzs,T5g=ww(x,y,m,n,key,life,money,soul,tools,js,cj,bf,lj,TB,wzsy,dscj,ngqj,xmzs,T5g)
            if dl==0:
                SY()
            else:
                if zjr:
                    zyd(zx,zy,zydx,zydy)
                sy()                           
        elif  f=='s':
            m=x+1
            n=y
            zt()
            x,y,key,life,money,soul,tools,js,cj,bf,lj,TB,wzsy,dscj,ngqj,xmzs,T5g=ww(x,y,m,n,key,life,money,soul,tools,js,cj,bf,lj,TB,wzsy,dscj,ngqj,xmzs,T5g)
            if dl==0:
                SY()
            else:
                if zjr:
                    zyd(zx,zy,zydx,zydy)
                sy()
        elif f=='d':
            m=x
            n=y+2
            zt()
            x,y,key,life,money,soul,tools,js,cj,bf,lj,TB,wzsy,dscj,ngqj,xmzs,T5g=ww(x,y,m,n,key,life,money,soul,tools,js,cj,bf,lj,TB,wzsy,dscj,ngqj,xmzs,T5g)
            if dl==0:
                SY()
            else:
                if zjr:
                    zyd(zx,zy,zydx,zydy)
                sy()
        elif f=='esc':
            print('game over')
            print('您到达的地牢层数:第'+str(dl)+'层')
            chju(money,js,key,soul,cj,bf,lj)
            flag=True
            break
        elif f=='wq':
            print('武器栏:',wq)
        elif f=='dj':
            print('道具栏:',dj)
            djxh=input('输入使用道具的序号(按回车退出):')
            if djxh=='1':
                if '1.炸弹Q' not in dj:
                    print('>>你没有该道具<<')
                elif dj['1.炸弹Q']==0:
                    print('>>你没有该道具<<')
                else:
                    sy()
                    zdfx=input('已准备炸弹，请选择放置方向:')
                    ZDFZ(zdfx);sy()
            else:
                if dl==0:
                    SY()
                else:
                    sy()
        else:
            print('>>无效步骤<<')
        if s[m][n]=='#':
            s[m]=s[m][0:n]+player+s[m][n+1:]
            s[x]=s[x][0:y]+' '+s[x][y+1:]
            if dl==0:
                SY()
                print('--进入地牢--')
            else:
                sy()
                chju(money,js,key,soul,cj,bf,lj)
                print('--进入下一层地牢--')
            dl+=1
            if dl==10 and nd=='1':
                print('\\获得称号:铜牌探险家//')
            if dl==10 and nd=='2':
                print('\\获得称号:银牌探险家//')
            if dl==10 and nd=='3':
                print('\\获得称号:金牌探险家//')                
            Flag=True

