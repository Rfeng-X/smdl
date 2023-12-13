from random import randint
from tkinter import *
from tkinter.messagebox import *
root = Tk()
root.title("神秘地牢")
root.iconbitmap('./tupian/smdl2.ico')
imgs = [PhotoImage(file='./tupian/[B].gif'),
        PhotoImage(file='./tupian/[D].gif'),
        PhotoImage(file='./tupian/[key].gif'),
        PhotoImage(file='./tupian/[X].gif'),
        PhotoImage(file='./tupian/[#].gif'),
        PhotoImage(file='./tupian/[Z].gif'),
        PhotoImage(file='./tupian/[%].gif'),
        PhotoImage(file='./tupian/[ys].gif'),
        PhotoImage(file='./tupian/[ljd].gif'),
        PhotoImage(file='./tupian/[M].gif'),
        PhotoImage(file='./tupian/[W].gif'),
        PhotoImage(file='./tupian/[@].gif'),
        PhotoImage(file='./tupian/[g].gif'),
        PhotoImage(file='./tupian/[.].gif'),
        PhotoImage(file='./tupian/[GG].gif'),
        PhotoImage(file='./tupian/[$].gif'),
        PhotoImage(file='./tupian/[K].gif'),
        PhotoImage(file='./tupian/[S].gif'),
        PhotoImage(file='./tupian/[V].gif'),
        PhotoImage(file='./tupian/[F].gif'),
        PhotoImage(file='./tupian/[Y].gif'),
        PhotoImage(file='./tupian/[H].gif'),
        PhotoImage(file='./tupian/[R].gif'),
        PhotoImage(file='./tupian/[bg].gif'),
        PhotoImage(file='./tupian/[Q].gif')]   #素材图片
cv = Canvas(root, bg='#646464', width=600, height=475)#绘制画布
cv.create_rectangle(379, 0, 600, 475, fill='#646464',outline = '#646464')  #绘制右侧页面矩形
map1=['XXXXXXXXXXXXXXXXXXXXX',
      'XXXXXXXXXXXXXXXXXXXXX',
      'XX                 XX',
      'XX                 XX',
      'XX                 XX',
      'XX                 XX',
      'XX                 XX',
      'XX                 XX',
      'XX                 XX',
      'XX                 XX',
      'XX                 XX',
      'XX                 XX',
      'XX                 XX',
      'XX                 XX',
      'XX                 XX',
      'XX                 XX',
      'XX                 XX',
      'XX                 XX',
      'XX                 XX',
      'XXXXXXXXXXXXXXXXXXXXX',
      'XXXXXXXXXXXXXXXXXXXXX']   #地图范围17*17
sight=['     ',
       '     ',
       '     ',
       '     ',
       '     ']                  #视野范围5*5
dl=0                   #地牢层数
TB=False               #隐身咒语
wzsy=False             #无中生有
dscj=False             #点石成金
ngqj=False             #能工巧匠
xmzs=False             #血魔之手
fp={}                  #眼疾手快
hh={'0':0}             #战斗状态,0是非战斗状态,1是战斗状态
qq={'0':0}             #炸弹放置状态,0不是,1是
life=0;key=0;money=0;soul=0
dj={}                  #道具栏
tools={'/':0,'[]':0,'=}':0,'T':0}
wq={}                  #武器栏
player=" "                       #各种变量定义
R1=0;R4=0
m=0;n=0
def xlxs():                      #玩家血量显示
    global life
    if 0<life<=28:   
        cv.create_text(50+6*(life-1),404,text='❤'*life,fill='#DE1E3E')
    else:
        cv.create_text(64,404,text='❤*'+str(life),fill='#DE1E3E')

def gwxlxs():                   #怪物血量显示
    global life2      
    cv.create_text(492+6*(life2-1),50,text='❤'*life2,fill='#DE1E3E')
def gwhdxs():                   #怪物护盾显示
    global gwhd
    cv.create_text(493+6*(len(gwhd)-1),64,text='[] '*len(gwhd),fill='#A9A9A9')
def zt():                       #状态栏显示
    global life ,key, money, soul, dl
    cv.create_rectangle(0, 379, 378, 478, fill='#646464',outline = 'black')   #(0, 375, 378, 560)范围内状态栏刷新#646464
    cv.create_text(30,390,text='第'+str(dl)+'层地牢')
    cv.create_text(22,404,text='精力值:',fill='#DC143C')
    xlxs()
    cv.create_text(20,417,text='金币:'+str(money),fill='#FFD700')
    cv.create_text(60,417,text='钥匙:'+str(key),fill='#798999')
    cv.create_text(102,417,text='精华:'+str(soul),fill='#1E90FF')
    cv.create_text(230,417,text='物品栏:'+str(tools),fill='#A9A9A9')
    cv.create_text(22,432,text='武器栏:',fill='#222222')
    cv.create_text(190,445,text=str(wq),fill='#222222')
    cv.create_text(22,462,text='道具栏:')
    cv.create_text(145,462,text=str(dj))
def sy_ee():                   #有洞察戒指的视野背景显示
    for i in range(0,5):       #5*5范围
        for j in range(0,5):
            cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[23])
def sy_noee():                 #无洞察戒指的视野背景显示
    cv.create_rectangle(0, 0, 378, 378,fill='black',outline = 'black',width = 2)
    for i in range(1,4):       #中间3*3范围
        for j in range(1,4):
            cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[23])
def sy():
    if '洞察戒指' in dj:
        for i in range(5):
            sight[i]=s[x-2+i][y-2:y+3]    #地图中5*5的存入视野的5*5
        sy_ee()    
    else:
        for i in range(3):
            sight[i+1]=' '+s[x-1+i][y-1:y+2]+' '#地图中3*3的存入视野的3*3
        sy_noee()    

    for i in range(0,5):
        for j in range(0,5):
            if sight[i][j]=='D':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[1])
                cv.pack()
            elif sight[i][j]=='B':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[0])
                cv.pack()
            elif sight[i][j]=='^':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[2])
                cv.pack()     
            elif sight[i][j]=='X':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[3])
                cv.pack()     
            elif sight[i][j]=='#':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[4])
                cv.pack()     
            elif sight[i][j]=='Z':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[5])
                cv.pack()     
            elif sight[i][j]=='%':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[6])
                cv.pack()     
            elif sight[i][j]=='&':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[7])
                cv.pack()     
            elif sight[i][j]=='?':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[8])
                cv.pack()     
            elif sight[i][j]=='M':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[9])
                cv.pack()     
            elif sight[i][j]=='W':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[10])
                cv.pack()     
            elif sight[i][j]=='@':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[11])
                cv.pack()     
            elif sight[i][j]=='g':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[12])
                cv.pack()     
            elif sight[i][j]=='*':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[13])
                cv.pack()     
            elif sight[i][j]=='G':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[14])
                cv.pack()     
            elif sight[i][j]=='$':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[15])
                cv.pack()
            elif sight[i][j]=='K':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[16])
                cv.pack()
            elif sight[i][j]=='S':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[17])
                cv.pack()
            elif sight[i][j]=='V':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[18])
                cv.pack()
            elif sight[i][j]=='F':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[19])
                cv.pack()
            elif sight[i][j]=='Y':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[20])
                cv.pack()
            elif sight[i][j]=='H':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[21])
                cv.pack()
            elif sight[i][j]=='R':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[22])
                cv.pack()
            elif sight[i][j]=='Q':
                cv.create_image((j * 75 + 40, i * 75 + 40), image=imgs[24])
                cv.pack()    
def jrz():
    global zjr,zx,zy,zydx,zydy
    zjr=False
    if '护身符δ' in dj:
        zjr=False
    elif s[x-1][y]=='Z':            #鬼魂惊扰判定
        zx=x-1;zy=y
        zydx,zydy=x,y
        zjr=True
    elif s[x+1][y]=='Z':
        zx=x+1;zy=y
        zydx,zydy=x,y
        zjr=True
    elif s[x][y-1]=='Z':
        zx=x;zy=y-1
        zydx,zydy=x,y
        zjr=True
    elif s[x][y+1]=='Z':
        zx=x;zy=y+1
        zydx,zydy=x,y
        zjr=True
    elif s[x+1][y+1]=='Z':
        zx=x+1;zy=y+1
        zydx,zydy=x,y
        zjr=True
    elif s[x+1][y-1]=='Z':
        zx=x+1;zy=y-1
        zydx,zydy=x,y
        zjr=True
    elif s[x-1][y+1]=='Z':
        zx=x-1;zy=y+1
        zydx,zydy=x,y
        zjr=True
    elif s[x-1][y-1]=='Z':
        zx=x-1;zy=y-1
        zydx,zydy=x,y
        zjr=True
def zyd():                         #僵尸移动
    global zx,zy,zydx,zydy
    if zydx!=x or zydy!=y:
        s[zydx]="".join([s[zydx][0:zydy],'Z',s[zydx][zydy+1:]])
        s[zx]="".join([s[zx][0:zy],' ',s[zx][zy+1:]])
def ww():
    global x,y,m,n,key,life,money,soul,tools,js,cj,bf,lj,TB,wzsy,dscj,ngqj,xmzs,T5g,R1,R4,Tb,Q,life2,gwhd,sb,KeyCode,zjr
    cv.delete("all")                                                             #清除原有图像,性能优化的关键
    cv.create_rectangle(379, 394, 600, 475, fill='#646464',outline = '#646464')  #右下角全侧页面
    if zjr:
        cv.create_text(418,388,text='你吸引了鬼魂!',fill='#D1EEEE')
    cv.create_rectangle(378, 1, 603, 379, fill='#646464',outline = '#000000')    #右上角页面
    cv.unbind("<KeyPress-e>")                                                    #按键绑定重置
    cv.unbind("<KeyPress-1>");cv.unbind("<KeyPress-2>");cv.unbind("<KeyPress-3>")
    cv.unbind("<KeyPress-4>");cv.unbind("<KeyPress-5>");cv.unbind("<KeyPress-6>") 
    if s[m][n]==' ':
        s[m]="".join([s[m][0:n],player,s[m][n+1:]])
        s[x]="".join([s[x][0:y],' ',s[x][y+1:]])
        x,y=m,n
    elif s[m][n]=='$':
        cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
        if key>0:
            s[m]="".join([s[m][0:n],player,s[m][n+1:]])
            s[x]="".join([s[x][0:y],' ',s[x][y+1:]])
            cv.create_text(416,388,text='你打开了宝箱') 
            if ngqj:
                if randint(0,1)!=0:
                    cv.create_text(528,388,text='|触发能工巧匠,不消耗钥匙|',fill='#FFA500') 
                else:
                    key-=1
            else:
                key-=1   
            x,y=m,n
            r5=randint(1,20)
            if r5<=3:
                cv.create_text(400,402,text='金币+2',fill='#FFD700') 
                money+=2
            elif 4<=r5<=9:
                cv.create_text(442,402,text='你发现了血瓶,精力值+1',fill='#DE1E3E') 
                life+=1
            elif 10<=r5<=15:
                cv.create_text(400,402,text='金币+3',fill='#FFD700') 
                money+=3
            elif r5==16:
                if '洞察戒指' in dj:                    
                    cv.create_text(400,402,text='金币+4',fill='#FFD700') 
                    money+=4
                else:
                    cv.create_text(418,402,text='获得洞察戒指',fill='#A9A9A9') 
                    dj['洞察戒指']=dj.get('洞察戒指',0)+1
            elif 17<=r5<=20:
                cv.create_text(446,402,text='长矛+1 盾牌+1 弩箭+1',fill='#A9A9A9') 
                tools['/']+=1;tools['[]']+=1;tools['=}']+=1
        else:
            cv.create_text(424,388,text='没钥匙,无法打开')
        zt()
    elif s[m][n]=='?':                                            
        s[m]="".join([s[m][0:n],player,s[m][n+1:]])
        s[x]="".join([s[x][0:y],' ',s[x][y+1:]])
        x,y=m,n
        cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
        cv.create_text(434,388,text='你打开了腐烂的宝箱') 
        rr=randint(1,14)
        if fp!={}:
            rr=randint(10,14)
        if rr<=4:
            cv.create_text(400,402,text='金币+1',fill='#FFD700') 
            money+=1
            bf+=1
        if 5<=rr<=9:
            cv.create_text(459,402,text='你被宝箱怪咬了一口,精力值-1',fill='#8B0000') 
            lj+=1
            life-=1
        if 10<=rr<=11:
            cv.create_text(400,402,text='金币+3',fill='#FFD700') 
            bf+=1
            money+=3
        if 12<=rr<=13:
            cv.create_text(400,402,text='钥匙+1',fill='#798999') 
            bf+=1
            key+=1
        if rr==14:
            cv.create_text(400,402,text='镐子+1',fill='#A9A9A9') 
            tools['T']+=1
        zt()
    elif s[m][n]=='*':                                            
        s[m]="".join([s[m][0:n],player,s[m][n+1:]])
        s[x]="".join([s[x][0:y],' ',s[x][y+1:]])
        cv.create_text(400,402,text='精华+1',fill='#1E90FF')  
        soul+=1
        zt()
        x,y=m,n        
    elif s[m][n]=='^':                                           
        s[m]="".join([s[m][0:n],player,s[m][n+1:]])
        s[x]="".join([s[x][0:y],' ',s[x][y+1:]])
        cv.create_text(400,402,text='钥匙+1',fill='#798999')  
        key+=1
        zt()
        x,y=m,n
    elif s[m][n]=='B':
        if tools['T']<=0:
            cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
            cv.create_text(435,388,text='这是一面墙,无法通过')                                 
        if tools['T']>0:
            cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
            cv.create_text(450,388,text='是否要凿开墙壁(按e确定)') 
            cv.bind("<KeyPress-e>", ZQ)
    elif s[m][n]=='G':
        cv.create_text(477,10,text='您进入了神秘商店,按对应数字键购买')
        cv.create_text(475,25,text='1:/长矛=1金币   2:[]盾牌=1金币')
        cv.create_text(477,40,text='3:=}弩箭=1金币 4:T镐子=2金币 ')
        cv.create_text(483,55,text='5:0 血瓶=2金币 6:洞察戒指=5金币')
        cv.bind("<KeyPress-1>", Gcm)
        cv.bind("<KeyPress-2>", Gdp)
        cv.bind("<KeyPress-3>", Gnj)
        cv.bind("<KeyPress-4>", Ggz)
        cv.bind("<KeyPress-5>", Gxp)
        cv.bind("<KeyPress-6>", Gdc)

    elif s[m][n]=='M':
        cv.create_text(490,10,text='您进入了合成祭台,按对应数字键选择合成')
        cv.create_text(440,25,text='每次合成消耗一点精华')
        cv.create_text(475,40,text='1: 长矛/+镐子T  2: 弩箭=}+镐子T')
        cv.create_text(471,55,text='3: 盾牌[]+镐子T 4: 长矛/+盾牌[]') 
        cv.create_text(476,70,text='5: 弩箭=}+长矛/ 6: 盾牌[]+弩箭=}')
        cv.bind("<KeyPress-1>", M1)
        cv.bind("<KeyPress-2>", M2)
        cv.bind("<KeyPress-3>", M3)
        cv.bind("<KeyPress-4>", M4)
        cv.bind("<KeyPress-5>", M5)
        cv.bind("<KeyPress-6>", M6)   
    elif s[m][n]=='@':
        cv.create_text(490,10,text='您进入了魔法祭台,按对应数字键选择学习')
        cv.create_text(484,25,text='1:无中生有=7精华  2:隐身咒语=5精华')
        cv.create_text(484,40,text='3:血魔之手=9精华  4:点石成金=6精华')
        cv.create_text(484,55,text='5:能工巧匠=9精华  6:眼疾手快=9精华')
        cv.bind("<KeyPress-1>", Gwzsy)
        cv.bind("<KeyPress-2>", GTB)
        cv.bind("<KeyPress-3>", Gxmzs)
        cv.bind("<KeyPress-4>", Gdscj)
        cv.bind("<KeyPress-5>", Gngqj)
        cv.bind("<KeyPress-6>", Gfp)
    elif s[m][n]=='Z':
        cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
        cv.create_text(446,388,text='一只鬼魂堵住了你的去路') 
        cv.create_text(442,402,text='是否要攻击它(按e确定)')
        cv.bind("<KeyPress-e>", ZD_Z)
    elif s[m][n]=='&':
        cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
        cv.create_text(446,388,text='一只异兽堵住了你的去路') 
        cv.create_text(442,402,text='是否要攻击它(按e确定)')
        cv.bind("<KeyPress-e>", ZD_ys)
    elif s[m][n]=='#':
        chju()
        scmap()  
    elif s[m][n]=='W':
        cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
        cv.create_text(446,388,text='古城守卫堵住了你的去路') 
        cv.create_text(442,402,text='是否要攻击它(按e确定)')
        cv.bind("<KeyPress-e>", ZD_W)
    
    elif s[m][n]=='%':
        cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
        cv.create_text(422,388,text='你发现游荡骑士')
        cv.create_text(465,402,text='请你选择是否要袭击它(按e确定)')
        cv.bind("<KeyPress-e>", ZD_qs)
                             
    elif s[m][n]=='&':
        cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
        cv.create_text(446,388,text='一只异兽堵住了你的去路') 
        cv.create_text(442,402,text='是否要攻击它(按e确定)')
        cv.bind("<KeyPress-e>", ZD_ys)
    elif s[m][n]=='Q':
        cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
        cv.create_text(455,388,text='是否点燃爆破炸弹(按e确定):')
        cv.bind("<KeyPress-e>", DRZD)
    elif s[m][n]=='g':
        cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
        cv.create_text(428,388,text='你遇到了神秘商人')
        cv.create_text(490,10,text='神秘商人:“你好!我的朋友。请问我能帮到')
        cv.create_text(405,25,text='你什么?”')
        cv.create_text(420,45,text='1:对话  2:交易')
        cv.bind("<KeyPress-1>", gdh)
        cv.bind("<KeyPress-2>", gjy)    
    zt()

def zspd():
    global m,n,key,money,tools,js,life2,xmzs,gw
    if life2<=0:
        cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
        cv.create_text(420,388,text='你战胜了怪物!',fill='#DAA520')
        cv.create_text(414,402,text='获得战利品:',fill='#FF8C00')
        hh['0']=0                       #战斗状态解除
        gw=s[m][n]                      #获取怪物种类
        s[m]=s[m][0:n]+' '+s[m][n+1:]   #怪物清除
        sy()
        zlp()
        js+=1                 
def zdxl(life2,gwhd):
    cv.create_rectangle(455, 40, 600, 75, fill='#646464',outline = '#646464')
    cv.create_text(470,50,text='血量:',fill='#DC143C')
    gwxlxs()
    cv.create_text(470,65,text='护盾:',fill='#A9A9A9')
    gwhdxs()                                           
    cv.pack()
def chju():
    global money,js,key,soul,cj,bf,lj
    cv.create_rectangle(378, 1, 603, 379, fill='#646464',outline = '#000000')
    cv.create_text(427,20,text='结算:',fill='#FFA500')
    if money>10:
        cv.create_text(477,40,text='获得成就:<钱多不压身>',fill='#FF8C00')
    if js>4:
        cv.create_text(475,55,text='获得成就:  <怪物猎手>',fill='#FF8C00')
    if key>6:
        cv.create_text(475,70,text='获得成就:  <无锁畏惧>',fill='#FF8C00')
    if soul>11:
        cv.create_text(475,85,text='获得成就:  <元气满满>',fill='#FF8C00')
    if cj>4:
        cv.create_text(475,100,text='获得成就:  <黄金矿工>',fill='#FF8C00')
    if bf>6:
        cv.create_text(475,115,text='获得成就:  <探索高手>',fill='#FF8C00')
    if lj>5:
        cv.create_text(477,130,text='获得成就:<宝箱怪挚爱>',fill='#FF8C00')
    if not(money>10 or js>4 or key>6 or soul>11 or cj>4 or bf>6 or lj>5):
        cv.create_text(433,40,text='无成就')
def zlp():
    global key,money,tools,gw,xmzs
    rr=randint(1,6)
    if rr==1:
            cv.create_text(402,416,text='金币+3',fill='#FFD700') 
            money+=3          
    elif rr==2:
            cv.create_text(402,416,text='金币+2',fill='#FFD700')
            cv.create_text(445,416,text='长矛+1',fill='#A9A9A9') 
            tools['/']+=1
            money+=2
    elif rr==3:
            cv.create_text(402,416,text='金币+2',fill='#FFD700')
            cv.create_text(445,416,text='弩箭+1',fill='#A9A9A9')
            tools['=}']+=1
            money+=2
    elif rr==4:
            cv.create_text(402,416,text='钥匙+2',fill='#798999')
            cv.create_text(445,416,text='盾牌+1',fill='#A9A9A9') 
            key+=2
            tools['[]']+=1
    elif rr==5:
            cv.create_text(402,416,text='钥匙+1',fill='#798999')
            key+=1
            cv.create_text(490,416,text='长矛+1 盾牌+1 弩箭+1',fill='#A9A9A9') 
            tools['/']+=1;tools['[]']+=1;tools['=}']+=1
    else:
            cv.create_text(402,416,text='金币+4',fill='#FFD700') 
            money+=4           
    if gw=='&':
        rrr=randint(1,4)
        if rrr==1:
            if '护身符δ' not in dj:
                dj['护身符δ']=dj.get('护身符δ',0)+1
                cv.create_text(412,430,text='获得护身符',fill='#000000') 
        if rrr==2:
            if not xmzs:
                xmzs=True
                cv.create_text(448,430,text='无意间你学会了血魔之手',fill='#EE0000') 
        wq['3:奶盾']=wq.get('3:奶盾',0)+3
        cv.create_text(412,444,text='获得奶盾*3',fill='#222222')
        wq['5:钩爪']=wq.get('5:钩爪',0)+3
        cv.create_text(412,458,text='获得钩爪*3',fill='#222222')
    if gw=='%':
        wq['6:重盾']=wq.get('6:重盾',0)+4
        cv.create_text(412,430,text='获得重盾*4',fill='#222222')
        wq['1:长刀']=wq.get('1:长刀',0)+4
        cv.create_text(412,444,text='获得长刀*4',fill='#222222')
        wq['2:弩炮']=wq.get('2:弩炮',0)+2
        cv.create_text(412,458,text='获得弩炮*2',fill='#222222')
    if gw=='W':
        cv.create_text(405,430,text='金币+20',fill='#FFD700')
        money+=20
        cv.create_text(424,445,text='获得爆破炸弹*2',fill='#000000')
        dj['爆破炸弹']=dj.get('爆破炸弹',0)+2
    zt()
def fight_1():              #战斗的第一分支
    global x,y,m,n,key,life,money,soul,tools,js,TB,wzsy,xmzs,R1,R4,Tb,Q,life2,gwhd,sb
    R1=randint(1,12);R4=randint(1,12)              #R1：玩家的攻击命中概率和攻击状态
    sb=False                                       #sb是闪避选择,Tb和R4组成逃跑概率
    cv.create_rectangle(380, 100, 600, 133, fill='#708090',outline = '#708090')
    cv.create_text(488,110,text='你的回合,请选择你的操作(按对应数字键)')
    cv.create_text(479,125,text='1:普通攻击 2:武器攻击 3:闪避 4:逃跑')
    cv.bind("<KeyPress-1>", fight_1_1)
    cv.bind("<KeyPress-2>", fight_1_2)
    cv.bind("<KeyPress-3>", fight_1_3)
    cv.bind("<KeyPress-4>", fight_1_4)


def fight_1_1(G):              #战斗的第二分支之普通攻击
    global x,y,m,n,key,life,money,soul,tools,js,TB,wzsy,xmzs,R1,R4,Tb,Q,life2,gwhd,sb
    cv.unbind("<KeyPress-1>")
    cv.unbind("<KeyPress-2>")
    cv.unbind("<KeyPress-3>")
    cv.unbind("<KeyPress-4>")
    cv.create_rectangle(382, 120, 599, 132, fill='#798999',outline = '#798999')
    cv.create_text(450,125,text='1:拳头  2:长矛/  3:弩箭=}')
    cv.bind("<KeyPress-1>", fight_1_1_1)
    cv.bind("<KeyPress-2>", fight_1_1_2)
    cv.bind("<KeyPress-3>", fight_1_1_3)
def fight_1_2(G):              #战斗的第二分支之武器攻击
    global x,y,m,n,key,life,money,soul,tools,js,TB,wzsy,xmzs,R1,R4,Tb,Q,life2,gwhd,sb
    cv.unbind("<KeyPress-1>")
    cv.unbind("<KeyPress-2>")
    cv.unbind("<KeyPress-3>")
    cv.unbind("<KeyPress-4>")
    cv.create_rectangle(382, 120, 599, 132, fill='#798999',outline = '#798999')
    cv.create_text(436,125,text='按武器栏对应数字键')
    cv.bind("<KeyPress-1>", fight_1_2_1)
    cv.bind("<KeyPress-2>", fight_1_2_2)
    cv.bind("<KeyPress-3>", fight_1_2_3)
    cv.bind("<KeyPress-4>", fight_1_2_4)
    cv.bind("<KeyPress-5>", fight_1_2_5)
    cv.bind("<KeyPress-6>", fight_1_2_6)
def fight_1_2_1(G):            #战斗的第三分支
    global x,y,m,n,key,life,money,soul,tools,js,TB,wzsy,xmzs,R1,R4,Tb,Q,life2,gwhd,sb
    cv.unbind("<KeyPress-1>")
    cv.unbind("<KeyPress-2>")
    cv.unbind("<KeyPress-3>")
    cv.unbind("<KeyPress-4>")
    cv.unbind("<KeyPress-5>")
    cv.unbind("<KeyPress-6>")
    cv.create_rectangle(380, 132, 600, 378, fill='#717171',outline = '#717171')
    if ('1:长刀' not in wq) or wq['1:长刀']<=0:
        cv.create_text(418,145,text='你没有该装备');fight_1()
    else:
        cv.create_text(408,145,text='使用长刀',fill='#222222')
        if R1<=8:
            if '[]' in gwhd:
                cv.create_text(434,160,text='怪物有护盾抵抗 -[]',fill='#A9A9A9')
                cv.create_text(444,175,text='攻击造成 1 点伤害 -❤',fill='#8B0000')
                gwhd.pop();life2-=1;soul+=1;wq['1:长刀']-=1     #攻击命中扣多少血即获得多少精华
                zdxl(life2,gwhd)
                zt()
                zspd()            #战胜判定,判定怪物是否死亡
                if life2>0:
                    gwfight()     #进入怪物的回合
            else:
                cv.create_text(450,160,text='攻击造成 2 点伤害 -❤❤',fill='#8B0000')
                life2-=1;soul+=1;wq['1:长刀']-=1    #扣一滴
                zdxl(life2,gwhd);zt()
                zspd()
                if life2>0:                         #没死?再扣一滴
                    life2-=1;soul+=1
                    zdxl(life2,gwhd);zt()
                    zspd()
                    gwfight()
        else:
            if '[]' in gwhd:
                cv.create_text(434,160,text='怪物有护盾抵抗 -[]',fill='#A9A9A9')
                cv.create_text(420,175,text='无法造成伤害',fill='#363636')
                wq['1:长刀']-=1
                gwhd.pop()
                zdxl(life2,gwhd)
                zt()
                cv.create_text(408,190,text='触发连击',fill='#FFA500')
                fight_1()         #连击,还是玩家的回合
            else:
                cv.create_text(444,160,text='攻击造成 1 点伤害 -❤',fill='#8B0000')
                life2-=1;soul+=1;wq['1:长刀']-=1
                zdxl(life2,gwhd)
                zt()
                zspd()
                cv.create_text(408,175,text='触发连击',fill='#FFA500')
                fight_1()
def fight_1_2_2(G):
    global x,y,m,n,key,life,money,soul,tools,js,TB,wzsy,xmzs,R1,R4,Tb,Q,life2,gwhd,sb
    cv.unbind("<KeyPress-1>")
    cv.unbind("<KeyPress-2>")
    cv.unbind("<KeyPress-3>")
    cv.unbind("<KeyPress-4>")
    cv.unbind("<KeyPress-5>")
    cv.unbind("<KeyPress-6>")
    cv.create_rectangle(380, 132, 600, 378, fill='#717171',outline = '#717171')
    if ('2:弩炮' not in wq) or wq['2:弩炮']<=0:
        cv.create_text(418,145,text='你没有该装备');fight_1()
    else:
        cv.create_text(408,145,text='使用弩炮',fill='#222222')
        if R1==1:
            if '[]' in gwhd:
                cv.create_text(434,160,text='怪物有护盾抵抗 -[]',fill='#A9A9A9')
                cv.create_text(450,175,text='攻击造成 2 点伤害 -❤❤',fill='#8B0000')
                gwhd.pop();wq['2:弩炮']-=1
                life2-=1;soul+=1
                zdxl(life2,gwhd);zt()
                zspd()
                if life2>0:
                    life2-=1;soul+=1
                    zdxl(life2,gwhd);zt()
                    zspd()
                    gwfight()
            else:
                cv.create_text(456,160,text='暴击造成 3 点伤害 -❤❤❤',fill='#8B0000')
                wq['2:弩炮']-=1
                life2-=1;soul+=1
                zdxl(life2,gwhd);zt()
                zspd()
                if life2>0:
                    life2-=1;soul+=1
                    zdxl(life2,gwhd);zt()
                    zspd()
                if life2>0:
                    life2-=1;soul+=1
                    zdxl(life2,gwhd);zt()
                    zspd()
                    gwfight()
        elif 1<R1<=6:
            if '[]' in gwhd:
                cv.create_text(434,160,text='怪物有护盾抵抗 -[]',fill='#A9A9A9')
                cv.create_text(444,175,text='攻击造成 1 点伤害 -❤',fill='#8B0000')
                gwhd.pop();life2-=1;soul+=1;wq['2:弩炮']-=1
                zdxl(life2,gwhd)
                zt()
                zspd()
                cv.create_text(408,190,text='触发连击',fill='#FFA500')
                fight_1()
            else:
                cv.create_text(450,160,text='攻击造成 2 点伤害 -❤❤',fill='#8B0000')
                wq['2:弩炮']-=1
                life2-=1;soul+=1
                zdxl(life2,gwhd);zt()
                zspd()
                if life2>0:
                    life2-=1;soul+=1
                    zdxl(life2,gwhd);zt()
                    zspd()
                cv.create_text(408,175,text='触发连击',fill='#FFA500')
                fight_1()
        elif 6<R1<10:
            if '[]' in gwhd:
                cv.create_text(434,160,text='怪物有护盾抵抗 -[]',fill='#A9A9A9')
                cv.create_text(420,175,text='无法造成伤害',fill='#363636')
                gwhd.pop();wq['2:弩炮']-=1
                zdxl(life2,gwhd)
                zt()
                cv.create_text(408,190,text='触发连击',fill='#FFA500')
                fight_1()
            else:
                cv.create_text(444,160,text='攻击造成 1 点伤害 -❤',fill='#8B0000')
                wq['2:弩炮']-=1
                life2-=1;soul+=1
                zdxl(life2,gwhd);zt()
                zspd()
                cv.create_text(408,175,text='触发连击',fill='#FFA500')
                fight_1()
        else:
             cv.create_text(438,160,text='怪物闪避了你的攻击',fill='#E0EEE0')
             wq['2:弩炮']-=1;zt()
             gwfight()
def fight_1_2_3(G):
    global x,y,m,n,key,life,money,soul,tools,js,TB,wzsy,xmzs,R1,R4,Tb,Q,life2,gwhd,sb
    cv.unbind("<KeyPress-1>")
    cv.unbind("<KeyPress-2>")
    cv.unbind("<KeyPress-3>")
    cv.unbind("<KeyPress-4>")
    cv.unbind("<KeyPress-5>")
    cv.unbind("<KeyPress-6>")
    cv.create_rectangle(380, 132, 600, 378, fill='#717171',outline = '#717171')
    if ('3:奶盾' not in wq) or wq['3:奶盾']<=0:
        cv.create_text(418,145,text='你没有该装备');fight_1()
    else:
        cv.create_text(408,145,text='使用奶盾',fill='#222222')
        if R1<=10:
            cv.create_text(408,160,text='格挡成功',fill='#FFA500')
            life+=2
            tools['[]']+=2
            wq['3:奶盾']-=1
            zt()
            gwfight()
        else:
            cv.create_text(408,160,text='格挡失败',fill='#363636')
            gwfight()
def fight_1_2_4(G):
    global x,y,m,n,key,life,money,soul,tools,js,TB,wzsy,xmzs,R1,R4,Tb,Q,life2,gwhd,sb
    cv.unbind("<KeyPress-1>")
    cv.unbind("<KeyPress-2>")
    cv.unbind("<KeyPress-3>")
    cv.unbind("<KeyPress-4>")
    cv.unbind("<KeyPress-5>")
    cv.unbind("<KeyPress-6>")
    cv.create_rectangle(380, 132, 600, 378, fill='#717171',outline = '#717171')
    if ('4:巨剑' not in wq) or wq['4:巨剑']<=0:
        cv.create_text(418,145,text='你没有该装备');fight_1()
    else:
        cv.create_text(408,145,text='使用巨剑',fill='#222222')
        if R1<=6:
            if '[]' in gwhd:
                cv.create_text(434,160,text='怪物有护盾抵抗 -[]',fill='#A9A9A9')
                cv.create_text(450,175,text='攻击造成 2 点伤害 -❤❤',fill='#8B0000')
                gwhd.pop();wq['4:巨剑']-=1
                life2-=1;soul+=1
                zdxl(life2,gwhd);zt()
                zspd()
                if life2>0:
                    life2-=1;soul+=1
                    zdxl(life2,gwhd);zt()
                    zspd()
                    gwfight()
            else:
                cv.create_text(456,160,text='暴击造成 3 点伤害 -❤❤❤',fill='#8B0000')
                wq['4:巨剑']-=1
                life2-=1;soul+=1
                zdxl(life2,gwhd);zt()
                zspd()
                if life2>0:
                    life2-=1;soul+=1
                    zdxl(life2,gwhd);zt()
                    zspd()
                if life2>0:
                    life2-=1;soul+=1
                    zdxl(life2,gwhd);zt()
                    zspd()
                    gwfight()
        elif 7<=R1<=8:
             if '[]' in gwhd:
                cv.create_text(434,160,text='怪物有护盾抵抗 -[]',fill='#A9A9A9')
                cv.create_text(444,175,text='攻击造成 1 点伤害 -❤',fill='#8B0000')
                gwhd.pop();life2-=1;soul+=1;wq['4:巨剑']-=1
                zdxl(life2,gwhd)
                zt()
                zspd()
                if life2>0:
                    gwfight()
             else:
                cv.create_text(450,160,text='攻击造成 2 点伤害 -❤❤',fill='#8B0000')
                wq['4:巨剑']-=1
                life2-=1;soul+=1
                zdxl(life2,gwhd);zt()
                zspd()
                if life2>0:
                    life2-=1;soul+=1
                    zdxl(life2,gwhd);zt()
                    zspd()
                    gwfight()
        else:
             cv.create_text(438,160,text='怪物闪避了你的攻击',fill='#E0EEE0')
             wq['4:巨剑']-=1;zt()
             gwfight()
def fight_1_2_5(G):
    global x,y,m,n,key,life,money,soul,tools,js,TB,wzsy,xmzs,R1,R4,Tb,Q,life2,gwhd,sb
    cv.unbind("<KeyPress-1>")
    cv.unbind("<KeyPress-2>")
    cv.unbind("<KeyPress-3>")
    cv.unbind("<KeyPress-4>")
    cv.unbind("<KeyPress-5>")
    cv.unbind("<KeyPress-6>")
    cv.create_rectangle(380, 132, 600, 378, fill='#717171',outline = '#717171')
    if ('5:钩爪' not in wq) or wq['5:钩爪']<=0:
        cv.create_text(418,145,text='你没有该装备');fight_1()
    else:
        cv.create_text(408,145,text='使用钩爪',fill='#222222')
        if R1<=6:
            if '[]' in gwhd:
                cv.create_text(434,160,text='怪物有护盾抵抗 -[]',fill='#A9A9A9')
                cv.create_text(444,175,text='攻击造成 1 点伤害 -❤',fill='#8B0000')
                gwhd.pop();life2-=1;soul+=1;wq['5:钩爪']-=1
                zdxl(life2,gwhd)
                life+=1;cv.create_text(420,190,text='吸血成功 +❤',fill='#DE1E3E')
                zt()
                zspd()
                if life2>0:
                    gwfight()
            else:
                cv.create_text(450,160,text='攻击造成 2 点伤害 -❤❤',fill='#8B0000')
                wq['5:钩爪']-=1
                life2-=1;soul+=1
                life+=1;cv.create_text(420,175,text='吸血成功 +❤',fill='#DE1E3E')
                zdxl(life2,gwhd);zt()
                zspd()
                if life2>0:
                    life2-=1;soul+=1
                    life+=1;cv.create_text(420,190,text='吸血成功 +❤',fill='#DE1E3E')
                    zdxl(life2,gwhd);zt()
                    zspd()
                    gwfight()
        elif 7<=R1<=9:
            if '[]' in gwhd:
                cv.create_text(434,160,text='怪物有护盾抵抗 -[]',fill='#A9A9A9')
                cv.create_text(420,175,text='无法造成伤害',fill='#363636')
                gwhd.pop();wq['5:钩爪']-=1
                zdxl(life2,gwhd)
                zt()
                gwfight()
            else:
                cv.create_text(444,160,text='攻击造成 1 点伤害 -❤',fill='#8B0000')
                wq['5:钩爪']-=1
                life2-=1;soul+=1
                life+=1;cv.create_text(420,175,text='吸血成功 +❤',fill='#DE1E3E')
                zdxl(life2,gwhd);zt()
                zspd()
                if life2>0:
                    gwfight()
        else:
             cv.create_text(438,160,text='怪物闪避了你的攻击',fill='#E0EEE0')
             wq['5:钩爪']-=1;zt()
             gwfight()
def fight_1_2_6(G):
    global x,y,m,n,key,life,money,soul,tools,js,TB,wzsy,xmzs,R1,R4,Tb,Q,life2,gwhd,sb
    cv.unbind("<KeyPress-1>")
    cv.unbind("<KeyPress-2>")
    cv.unbind("<KeyPress-3>")
    cv.unbind("<KeyPress-4>")
    cv.unbind("<KeyPress-5>")
    cv.unbind("<KeyPress-6>")
    cv.create_rectangle(380, 132, 600, 378, fill='#717171',outline = '#717171')
    if ('6:重盾' not in wq) or wq['6:重盾']<=0:
        cv.create_text(418,145,text='你没有该装备');fight_1()
    else:
        cv.create_text(408,145,text='使用重盾',fill='#222222')
        if R1<=11:
            cv.create_text(408,160,text='格挡成功',fill='#FFA500')
            if '[]' in gwhd:
                cv.create_text(434,175,text='怪物有护盾抵抗 -[]',fill='#A9A9A9')
                cv.create_text(420,190,text='无法造成伤害',fill='#363636')
                gwhd.pop();wq['6:重盾']-=1
                tools['[]']+=3
                zdxl(life2,gwhd)
                zt()
                gwfight()
            else:
                cv.create_text(444,175,text='攻击造成 1 点伤害 -❤',fill='#8B0000')
                wq['6:重盾']-=1
                life2-=1;soul+=1
                tools['[]']+=3
                zdxl(life2,gwhd);zt()
                zspd()
                if life2>0:
                    gwfight()
        else:
            cv.create_text(408,160,text='格挡失败',fill='#363636')
            gwfight()
def fight_1_3(G):              #战斗的第二分支之闪避
    global sb
    sb=True    #选择闪避
    cv.create_rectangle(380, 132, 600, 378, fill='#717171',outline = '#717171')
    gwfight()
def fight_1_4(G):              #战斗的第二分支之逃跑
    global R4,Tb
    cv.create_rectangle(380, 132, 600, 378, fill='#717171',outline = '#717171')
    if R4<=Tb:
        hh['0']=0
        cv.create_text(408,140,text='逃跑成功')
    else:
        cv.create_text(408,140,text='逃跑失败')
        gwfight()
def fight_1_1_1(G):
    global x,y,m,n,key,life,money,soul,tools,js,TB,wzsy,xmzs,R1,R4,Tb,Q,life2,gwhd,sb
    cv.unbind("<KeyPress-1>")
    cv.unbind("<KeyPress-2>")
    cv.unbind("<KeyPress-3>")
    cv.create_rectangle(380, 132, 600, 378, fill='#717171',outline = '#717171')
    cv.create_text(408,145,text='使用拳头',fill='#A9A9A9')
    if R1<=10:
        if '[]' in gwhd:
            cv.create_text(434,160,text='怪物有护盾抵抗 -[]',fill='#A9A9A9')
            cv.create_text(420,175,text='无法造成伤害',fill='#363636')
            gwhd.pop()
            zdxl(life2,gwhd)
            zt()
            gwfight()
        else:
            cv.create_text(444,160,text='攻击造成 1 点伤害 -❤',fill='#8B0000')
            life2-=1;soul+=1
            if xmzs:
                life+=1
                cv.create_text(420,175,text='触发血魔之手',fill='#EE0000')
                cv.create_text(424,190,text='精力值恢复+❤',fill='#DE1E3E')
            zdxl(life2,gwhd)
            zt()
            zspd()
            if life2>0:
                gwfight()
    else:
        cv.create_text(438,160,text='怪物闪避了你的攻击',fill='#E0EEE0')
        gwfight()
def fight_1_1_2(G):
    global x,y,m,n,key,life,money,soul,tools,js,TB,wzsy,xmzs,R1,R4,Tb,Q,life2,gwhd,sb
    cv.unbind("<KeyPress-1>")
    cv.unbind("<KeyPress-2>")
    cv.unbind("<KeyPress-3>")
    cv.create_rectangle(380, 132, 600, 378, fill='#717171',outline = '#717171')
    if tools['/']>0:
        cv.create_text(408,145,text='使用长矛',fill='#A9A9A9')
        if R1<=7:
            if '[]' in gwhd:
                cv.create_text(434,160,text='怪物有护盾抵抗 -[]',fill='#A9A9A9')
                cv.create_text(444,175,text='攻击造成 1 点伤害 -❤',fill='#8B0000')
                gwhd.pop();life2-=1;soul+=1;tools['/']-=1
                zdxl(life2,gwhd)
                zt()
                zspd()
                if life2>0:
                    gwfight()
            else:
                cv.create_text(450,160,text='攻击造成 2 点伤害 -❤❤',fill='#8B0000')
                life2-=1;soul+=1;tools['/']-=1
                zdxl(life2,gwhd);zt()
                zspd()
                
                life2-=1;soul+=1
                zdxl(life2,gwhd);zt()
                zspd()
                if life2>0:
                    gwfight()                
        else:
            cv.create_text(438,160,text='怪物闪避了你的攻击',fill='#E0EEE0')
            tools['/']-=1;zt()
            gwfight()
    else:
        cv.create_text(412,145,text='你没有长矛')
        fight_1()
def fight_1_1_3(G):
    global x,y,m,n,key,life,money,soul,tools,js,TB,wzsy,xmzs,R1,R4,Tb,Q,life2,gwhd,sb
    cv.unbind("<KeyPress-1>")
    cv.unbind("<KeyPress-2>")
    cv.unbind("<KeyPress-3>")
    cv.create_rectangle(380, 132, 600, 378, fill='#717171',outline = '#717171')
    if tools['=}']>0:
        cv.create_text(408,145,text='使用弩箭',fill='#A9A9A9')
        if R1<=7:
            if '[]' in gwhd:
                cv.create_text(434,160,text='怪物有护盾抵抗 -[]',fill='#A9A9A9')
                cv.create_text(420,175,text='无法造成伤害',fill='#363636')
                gwhd.pop();tools['=}']-=1
                zdxl(life2,gwhd)
                zt()
                cv.create_text(408,190,text='触发连击',fill='#FFA500')
                fight_1()
            else:
                cv.create_text(444,160,text='攻击造成 1 点伤害 -❤',fill='#8B0000')
                life2-=1;soul+=1;tools['=}']-=1
                zdxl(life2,gwhd);zt()
                zspd()
                if life2>0:
                    cv.create_text(408,175,text='触发连击',fill='#FFA500')
                    fight_1()
        else:
            cv.create_text(438,160,text='怪物闪避了你的攻击',fill='#E0EEE0')
            tools['=}']-=1;zt()
            gwfight()
    else:
        cv.create_text(412,145,text='你没有弩箭')
        fight_1()
def gwfight():
    global x,y,m,n,key,life,money,soul,tools,js,TB,wzsy,xmzs,R1,R4,Tb,Q,life2,gwhd,sb
    R2=randint(1,12);R3=randint(1,12)                           #R2:怪物的攻击状态,R3:玩家闪避概率
    cv.create_rectangle(380, 196, 600, 212, fill='#708090',outline = '#708090')
    cv.create_text(412,205,text='怪物的回合',fill='#000000')
    if s[m][n]=='W':
        if R2<=3:
            cv.create_text(437,220,text='古城守卫劈下了重剑')
            if sb:
                if R3<7:
                    cv.create_text(418,235,text='你闪避成功了',fill='#E0EEE0')
                    cv.create_text(424,145,text='精力值恢复+❤',fill='#DE1E3E')
                    life+=1
                    if wzsy:
                        cv.create_text(420,160,text='触发无中生有',fill='#436EEE')
                        cv.create_text(435,175,text='获得长矛,弩箭,盾牌',fill='#A9A9A9')
                        tools['/']+=2
                        tools['=}']+=2
                        tools['[]']+=2
                    zt()
                    fight_1()
                else:
                   cv.create_text(418,235,text='你闪避失败了')
                   if tools['[]']>0:
                        cv.create_text(444,250,text='你的盾牌抵挡了伤害 -[]',fill='#A9A9A9')
                        tools['[]']-=1
                        cv.create_text(454,265,text='你遭受 4 点伤害 -❤❤❤❤',fill='#8B0000')
                        life-=4
                        if life<=0:
                            chju()
                            zt()
                            showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                        zt()
                        fight_1()
                   else:
                       cv.create_text(460,250,text='你遭受 5 点暴击 -❤❤❤❤❤',fill='#8B0000')
                       life-=5
                       if life<=0:
                           chju()
                           zt()
                           showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                       zt()
                       fight_1()
            else:
                if tools['[]']>0:
                    cv.create_text(444,235,text='你的盾牌抵挡了伤害 -[]',fill='#A9A9A9')
                    tools['[]']-=1
                    cv.create_text(454,250,text='你遭受 4 点伤害 -❤❤❤❤',fill='#8B0000')
                    life-=4
                    if life<=0:
                        chju()
                        zt()
                        showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                    zt()
                    fight_1()
                else:
                    cv.create_text(460,235,text='你遭受 5 点暴击 -❤❤❤❤❤',fill='#8B0000')
                    life-=5
                    if life<=0:
                        chju()
                        zt()
                        showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                    zt()
                    fight_1()
        if 6<=R2<=10:   
            cv.create_text(449,280,text='一股远古的力量侵袭了你')
            if soul-5<0:
                soul=0 
                cv.create_text(465,295,text='你的精华已经耗尽,损失精力 -❤',fill='#8B0000')
                life-=1               
                if life<=0:
                    chju()
                    zt()
                    showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")    
            else:
                soul-=5
                cv.create_text(425,295,text='你的精华流失了')
            zt()
        if 4<=R2<=6:
            cv.create_text(437,220,text='古城守卫发射了火炮')
            if sb:
                if R3<6:
                    cv.create_text(418,235,text='你闪避成功了',fill='#E0EEE0')
                    cv.create_text(424,145,text='精力值恢复+❤',fill='#DE1E3E')
                    life+=1
                    if wzsy:
                        cv.create_text(420,160,text='触发无中生有',fill='#436EEE')
                        cv.create_text(435,175,text='获得长矛,弩箭,盾牌',fill='#A9A9A9')
                        tools['/']+=2
                        tools['=}']+=2
                        tools['[]']+=2
                    zt()
                    fight_1()
                else:
                   cv.create_text(418,235,text='你闪避失败了')
                   if tools['[]']>0:
                        cv.create_text(444,250,text='你的盾牌抵挡了伤害 -[]',fill='#A9A9A9')
                        tools['[]']-=1
                        cv.create_text(442,265,text='你遭受 2 点伤害 -❤❤',fill='#8B0000')
                        life-=2
                        if life<=0:
                            chju()
                            zt()
                            showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                        zt()
                        fight_1()
                   else:
                       cv.create_text(448,250,text='你遭受 3 点攻击 -❤❤❤',fill='#8B0000')
                       life-=3
                       if life<=0:
                           chju()
                           zt()
                           showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                       zt()
                       fight_1()
            else:
                if tools['[]']>0:
                    cv.create_text(444,235,text='你的盾牌抵挡了伤害 -[]',fill='#A9A9A9')
                    tools['[]']-=1
                    cv.create_text(442,250,text='你遭受 2 点伤害 -❤❤',fill='#8B0000')
                    life-=2
                    if life<=0:
                        chju()
                        zt()
                        showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                    zt()
                    fight_1()
                else:
                    cv.create_text(448,235,text='你遭受 3 点攻击 -❤❤❤',fill='#8B0000')
                    life-=3
                    if life<=0:
                        chju()
                        zt()
                        showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                    zt()
                    fight_1()
        if 7<=R2<=9:
            cv.create_text(449,220,text='古城守卫启动了能量脉冲')
            if sb:
                if R3<5:
                    cv.create_text(418,235,text='你闪避成功了',fill='#E0EEE0')
                    cv.create_text(424,145,text='精力值恢复+❤',fill='#DE1E3E')
                    life+=1
                    if wzsy:
                        cv.create_text(420,160,text='触发无中生有',fill='#436EEE')
                        cv.create_text(435,175,text='获得长矛,弩箭,盾牌',fill='#A9A9A9')
                        tools['/']+=2
                        tools['=}']+=2
                        tools['[]']+=2
                    zt()
                    fight_1()
                else:
                   cv.create_text(418,235,text='你闪避失败了')
                   if tools['[]']>0:
                        cv.create_text(444,250,text='你的盾牌抵挡了伤害 -[]',fill='#A9A9A9')
                        tools['[]']-=1
                        cv.create_text(448,265,text='你遭受 3 点伤害 -❤❤❤',fill='#8B0000')
                        life-=3
                        if life<=0:
                            chju()
                            zt()
                            showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                        zt()
                        fight_1()
                   else:
                       cv.create_text(454,250,text='你遭受 4 点攻击 -❤❤❤❤',fill='#8B0000')
                       life-=4
                       if life<=0:
                           chju()
                           zt()
                           showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                       zt()
                       fight_1()
            else:
                if tools['[]']>0:
                    cv.create_text(444,235,text='你的盾牌抵挡了伤害 -[]',fill='#A9A9A9')
                    tools['[]']-=1
                    cv.create_text(448,250,text='你遭受 3 点伤害 -❤❤❤',fill='#8B0000')
                    life-=3
                    if life<=0:
                        chju()
                        zt()
                        showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                    zt()
                    fight_1()
                else:
                    cv.create_text(454,235,text='你遭受 4 点攻击 -❤❤❤❤',fill='#8B0000')
                    life-=4
                    if life<=0:
                        chju()
                        zt()
                        showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                    zt()
                    fight_1()
        if 10<=R2<=12 and life2<=5:
            cv.create_text(449,220,text='古城守卫使用了洞察之心')
            if tools['[]']!=0:
                cv.create_text(431,235,text='你的护盾被消解了')
                tools['[]']=0
            else:
                cv.create_text(457,235,text='古城守卫恢复了精力, +❤❤',fill='#DE1E3E')
                life2+=2;zdxl(life2,gwhd)
            zt()
            fight_1()
        if 10<=R2<=12 and life2>5:
            cv.create_text(437,220,text='古城守卫恢复了护盾')
            gwhd.append('[]');gwhd.append('[]')
            zdxl(life2,gwhd)
            fight_1()
    elif s[m][n]=='%':
        if R2<=2:
            cv.create_text(437,220,text='游荡骑士发出了暴击',fill='#352f2a')
            if sb:
                if R3<7:
                    cv.create_text(418,235,text='你闪避成功了',fill='#E0EEE0')
                    cv.create_text(424,145,text='精力值恢复+❤',fill='#DE1E3E')
                    life+=1
                    if wzsy:
                        cv.create_text(420,160,text='触发无中生有',fill='#436EEE')
                        cv.create_text(435,175,text='获得长矛,弩箭,盾牌',fill='#A9A9A9')
                        tools['/']+=2
                        tools['=}']+=2
                        tools['[]']+=2
                    zt()
                    fight_1()
                else:
                   cv.create_text(418,235,text='你闪避失败了')
                   if tools['[]']>0:
                        cv.create_text(444,250,text='你的盾牌抵挡了伤害 -[]',fill='#A9A9A9')
                        tools['[]']-=1
                        cv.create_text(442,265,text='你遭受 2 点伤害 -❤❤',fill='#8B0000')
                        life-=2
                        if life<=0:
                            chju()
                            zt()
                            showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                        zt()
                        fight_1()
                   else:
                       cv.create_text(448,250,text='你遭受 3 点暴击 -❤❤❤',fill='#8B0000')
                       life-=3
                       if life<=0:
                           chju()
                           zt()
                           showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                       zt()
                       fight_1()
            else:
                if tools['[]']>0:
                    cv.create_text(444,235,text='你的盾牌抵挡了伤害 -[]',fill='#A9A9A9')
                    tools['[]']-=1
                    cv.create_text(442,250,text='你遭受 2 点伤害 -❤❤',fill='#8B0000')
                    life-=2
                    if life<=0:
                        chju()
                        zt()
                        showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                    zt()
                    fight_1()
                else:
                    cv.create_text(448,235,text='你遭受 3 点暴击 -❤❤❤',fill='#8B0000')
                    life-=3
                    if life<=0:
                        chju()
                        zt()
                        showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                    zt()
                    fight_1()
        if 3<=R2<=4:
            cv.create_text(437,220,text='游荡骑士进行了攻击',fill='#352f2a')
            if sb:
                if R3<=7:
                    cv.create_text(418,235,text='你闪避成功了',fill='#E0EEE0')
                    cv.create_text(424,145,text='精力值恢复+❤',fill='#DE1E3E')
                    life+=1
                    if wzsy:
                        cv.create_text(420,160,text='触发无中生有',fill='#436EEE')
                        cv.create_text(435,175,text='获得长矛,弩箭,盾牌',fill='#A9A9A9')
                        tools['/']+=2
                        tools['=}']+=2
                        tools['[]']+=2
                    zt()
                    fight_1()
                else:
                   cv.create_text(418,235,text='你闪避失败了')
                   if tools['[]']>0:
                        cv.create_text(444,250,text='你的盾牌抵挡了伤害 -[]',fill='#A9A9A9')
                        tools['[]']-=1
                        cv.create_text(436,265,text='你遭受 1 点伤害 -❤',fill='#8B0000')
                        life-=1
                        if life<=0:
                            chju()
                            zt()
                            showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                        zt()
                        fight_1()
                   else:
                       cv.create_text(442,250,text='你遭受 2 点伤害 -❤❤',fill='#8B0000')
                       life-=2
                       if life<=0:
                           chju()
                           zt()
                           showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                       zt()
                       fight_1()
            else:
                if tools['[]']>0:
                    cv.create_text(444,235,text='你的盾牌抵挡了伤害 -[]',fill='#A9A9A9')
                    tools['[]']-=1
                    cv.create_text(436,250,text='你遭受 1 点伤害 -❤',fill='#8B0000')
                    life-=1
                    if life<=0:
                        chju()
                        zt()
                        showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                    zt()
                    fight_1()
                else:
                    cv.create_text(442,235,text='你遭受 2 点伤害 -❤❤',fill='#8B0000')
                    life-=2
                    if life<=0:
                        chju()
                        zt()
                        showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                    zt()
                    fight_1()
        if 5<=R2<=9:
            cv.create_text(437,220,text='游荡骑士进行了反击',fill='#352f2a')
            if sb:
                if R3<7:
                    cv.create_text(418,235,text='你闪避成功了',fill='#E0EEE0')
                    cv.create_text(424,145,text='精力值恢复+❤',fill='#DE1E3E')
                    life+=1
                    if wzsy:
                        cv.create_text(420,160,text='触发无中生有',fill='#436EEE')
                        cv.create_text(435,175,text='获得长矛,弩箭,盾牌',fill='#A9A9A9')
                        tools['/']+=2
                        tools['=}']+=2
                        tools['[]']+=2
                    zt()
                    fight_1()
                else:
                   cv.create_text(418,235,text='你闪避失败了')
                   if tools['[]']>0:
                        cv.create_text(444,250,text='你的盾牌抵挡了攻击 -[]',fill='#A9A9A9')
                        tools['[]']-=1
                        zt()
                        fight_1()
                   else:
                       cv.create_text(436,235,text='你遭受 1 点伤害 -❤',fill='#8B0000')
                       life-=1
                       if life<=0:
                           chju()
                           zt()
                           showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                       zt()
                       fight_1()
            else:
                if tools['[]']>0:
                    cv.create_text(444,235,text='你的盾牌抵挡了攻击 -[]',fill='#A9A9A9')
                    tools['[]']-=1
                    zt()
                    fight_1()
                else:
                    cv.create_text(436,235,text='你遭受 1 点伤害 -❤',fill='#8B0000')
                    life-=1
                    if life<=0:
                        chju()
                        zt()
                        showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                    zt()
                    fight_1()
        if 8<=R2<=12:
            cv.create_text(437,265,text='游荡骑士举起了盾牌',fill='#352f2a')
            gwhd.append('[]')
            zdxl(life2,gwhd)
            fight_1()
        if R2==6 or R2==7:    
            cv.create_text(437,265,text='游荡骑士使用了破盾',fill='#352f2a')
            if tools['[]']<=1:
                tools['[]']=0
            else:
                tools['[]']-=2
            zt()
            fight_1()
            
    elif s[m][n]=='&':
        if R2<=5:
            cv.create_text(425,220,text='异兽进行了攻击',fill='#A52A2A')
            if sb:
                if R3<=7:
                    cv.create_text(418,235,text='你闪避成功了',fill='#E0EEE0')
                    cv.create_text(424,145,text='精力值恢复+❤',fill='#DE1E3E')
                    life+=1
                    if wzsy:
                        cv.create_text(420,160,text='触发无中生有',fill='#436EEE')
                        cv.create_text(435,175,text='获得长矛,弩箭,盾牌',fill='#A9A9A9')
                        tools['/']+=2
                        tools['=}']+=2
                        tools['[]']+=2
                    zt()
                    fight_1()
                else:
                   cv.create_text(418,235,text='你闪避失败了')
                   if tools['[]']>0:
                        cv.create_text(444,250,text='你的盾牌抵挡了伤害 -[]',fill='#A9A9A9')
                        tools['[]']-=1
                        cv.create_text(436,265,text='你遭受 1 点伤害 -❤',fill='#8B0000')
                        life-=1
                        if life<=0:
                            chju()
                            zt()
                            showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                        zt()
                        fight_1()
                   else:
                       cv.create_text(442,250,text='你遭受 2 点伤害 -❤❤',fill='#8B0000')
                       life-=2
                       if life<=0:
                           chju()
                           zt()
                           showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                       zt()
                       fight_1()
            else:
                if tools['[]']>0:
                    cv.create_text(444,235,text='你的盾牌抵挡了伤害 -[]',fill='#A9A9A9')
                    tools['[]']-=1
                    cv.create_text(436,250,text='你遭受 1 点伤害 -❤',fill='#8B0000')
                    life-=1
                    if life<=0:
                        chju()
                        zt()
                        showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                    zt()
                    fight_1()
                else:
                    cv.create_text(442,235,text='你遭受 2 点伤害 -❤❤',fill='#8B0000')
                    life-=2
                    if life<=0:
                        chju()
                        zt()
                        showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                    zt()
                    fight_1()
        if 6<=R2<=9:
            cv.create_text(425,220,text='异兽使用了吸血',fill='#A52A2A')
            if sb:
                if R3<5:
                    cv.create_text(418,235,text='你闪避成功了',fill='#E0EEE0')
                    cv.create_text(424,145,text='精力值恢复+❤',fill='#DE1E3E')
                    life+=1
                    if wzsy:
                        cv.create_text(420,160,text='触发无中生有',fill='#436EEE')
                        cv.create_text(435,175,text='获得长矛,弩箭,盾牌',fill='#A9A9A9')
                        tools['/']+=2
                        tools['=}']+=2
                        tools['[]']+=2
                    zt()
                    fight_1()
                else:
                   cv.create_text(418,235,text='你闪避失败了')
                   if tools['[]']>0:
                        cv.create_text(444,250,text='你的盾牌抵挡了攻击 -[]',fill='#A9A9A9')
                        tools['[]']-=1
                        zt()
                        fight_1()
                   else:
                       cv.create_text(422,250,text='你遭受吸血 -❤',fill='#8B0000')
                       life-=1
                       life2+=1;zdxl(life2,gwhd)
                       if life<=0:
                           chju()
                           zt()
                           showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                       zt()
                       fight_1()
            else:
                if tools['[]']>0:
                    cv.create_text(444,235,text='你的盾牌抵挡了攻击 -[]',fill='#A9A9A9')
                    tools['[]']-=1
                    zt()
                    fight_1()
                else:
                    cv.create_text(422,235,text='你遭受吸血 -❤',fill='#8B0000')
                    life-=1
                    life2+=1;zdxl(life2,gwhd)
                    if life<=0:
                        chju()
                        zt()
                        showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                    zt()
                    fight_1()
        if 10<=R2:
            cv.create_text(436,220,text='异兽进行了回血 +❤',fill='#A52A2A')
            life2+=1;zdxl(life2,gwhd)
            fight_1()
    elif s[m][n]=='Z':
        if R2<=5:
            cv.create_text(425,220,text='鬼魂陷入了呆滞',fill='#D1EEEE')
            if sb:
                cv.create_text(408,235,text='闪避失效',fill='#E0EEE0')
            fight_1()
        else:
            cv.create_text(425,220,text='鬼魂进行了攻击',fill='#D1EEEE')
            if sb:
                if R3<4:
                    cv.create_text(418,235,text='你闪避成功了',fill='#E0EEE0')
                    cv.create_text(424,145,text='精力值恢复+❤',fill='#DE1E3E')
                    life+=1
                    if wzsy:
                        cv.create_text(420,160,text='触发无中生有',fill='#436EEE')
                        cv.create_text(435,175,text='获得长矛,弩箭,盾牌',fill='#A9A9A9')
                        tools['/']+=2
                        tools['=}']+=2
                        tools['[]']+=2
                    zt()
                    fight_1()
                else:
                    cv.create_text(418,235,text='你闪避失败了')
                    if tools['[]']>0:
                        cv.create_text(444,250,text='你的盾牌抵挡了伤害 -[]',fill='#A9A9A9')
                        tools['[]']-=1
                    else:
                        cv.create_text(436,250,text='你遭受 1 点伤害 -❤',fill='#8B0000')
                        life-=1
                        zr=randint(1,4)
                        if zr==1:
                            if money>1:
                                money-=2
                                cv.create_text(424,265,text='你丢失两枚金币')
                            if money==1:
                                money-=1
                                cv.create_text(424,265,text='你丢失一枚金币')    
                        if zr==2:
                            if key>0:
                                key-=1
                                cv.create_text(424,265,text='你丢失一把钥匙')
                        if zr==3:
                            if money>0 and key>0:
                                key-=1;money-=1
                                cv.create_text(455,265,text='你丢失一枚金币和一把钥匙')         
                        if zr==4:
                            if soul>1:
                                soul-=2
                                cv.create_text(424,265,text='你流失两点精华')
                            if soul==1:
                                soul-=1
                                cv.create_text(424,265,text='你流失一点精华')

                        if life<=0:
                            chju()
                            zt()
                            showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                    zt()
                    fight_1()
            else:
                if tools['[]']>0:
                    tools['[]']-=1
                    cv.create_text(444,235,text='你的盾牌抵挡了伤害 -[]',fill='#A9A9A9')
                    zt()
                    fight_1()
                else:
                    cv.create_text(436,235,text='你遭受 1 点伤害 -❤',fill='#8B0000')
                    life-=1
                    zr=randint(1,3)
                    if zr==1:
                        if money>1:
                            money-=2
                            cv.create_text(424,250,text='你丢失两枚金币')
                        if money==1:
                            money-=1
                            cv.create_text(424,250,text='你丢失一枚金币')
                    
                    if zr==2:
                        if key>1:
                            key-=2
                            cv.create_text(424,250,text='你丢失两把钥匙')
                        if key==1:
                            key-=1
                            cv.create_text(424,250,text='你丢失一把钥匙')    
                    if zr==3:
                        if money>0 and key>0:
                            key-=1;money-=1
                            cv.create_text(455,250,text='你丢失一枚金币和一把钥匙')
                    if life<=0:
                            chju()
                            zt()
                            showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")
                    zt()
                    fight_1()
def DRZD(G):    #点燃炸弹
    global soul,KeyCode
    if soul-2>0:
        soul-=3
        cv.create_text(406,402,text='爆炸成功',fill='#FF7F00')
        s[m]=s[m][0:n]+' '+s[m][n+1:]      #炸弹炸毁周围八格
        if KeyCode=='d':
            if s[m-1][n-1] not in 'XW#':
                s[m-1]=s[m-1][0:n-1]+' '+s[m-1][n:]
            if s[m-1][n+1] not in 'XW#':
                s[m-1]=s[m-1][0:n+1]+' '+s[m-1][n+2:]
            if s[m+1][n-1] not in 'XW#':
                s[m+1]=s[m+1][0:n-1]+' '+s[m+1][n:]
            if s[m+1][n+1] not in 'XW#':
                s[m+1]=s[m+1][0:n+1]+' '+s[m+1][n+2:]                        
            if s[m-1][n] not in 'XW#':
                s[m-1]=s[m-1][0:n]+' '+s[m-1][n+1:]
            if s[m+1][n] not in 'XW#':
                s[m+1]=s[m+1][0:n]+' '+s[m+1][n+1:]
            if s[m][n+1] not in 'XW#':
                s[m]=s[m][0:n+1]+' '+s[m][n+2:]   
        elif KeyCode=='s':
            if s[m-1][n-1] not in 'XW#':
                s[m-1]=s[m-1][0:n-1]+' '+s[m-1][n:]
            if s[m-1][n+1] not in 'XW#':
                s[m-1]=s[m-1][0:n+1]+' '+s[m-1][n+2:]
            if s[m+1][n-1] not in 'XW#':
                s[m+1]=s[m+1][0:n-1]+' '+s[m+1][n:]
            if s[m+1][n+1] not in 'XW#':
                s[m+1]=s[m+1][0:n+1]+' '+s[m+1][n+2:]                        
            if s[m+1][n-1] not in 'XW#':
                s[m+1]=s[m+1][0:n-1]+' '+s[m+1][n:]
            if s[m+1][n] not in 'XW#':
                s[m+1]=s[m+1][0:n]+' '+s[m+1][n+1:]
            if s[m][n+1] not in 'XW#':
                s[m]=s[m][0:n+1]+' '+s[m][n+2:]
        elif KeyCode=='a':
            if s[m-1][n-1] not in 'XW#':
                s[m-1]=s[m-1][0:n-1]+' '+s[m-1][n:]
            if s[m-1][n+1] not in 'XW#':
                s[m-1]=s[m-1][0:n+1]+' '+s[m-1][n+2:]
            if s[m+1][n-1] not in 'XW#':
                s[m+1]=s[m+1][0:n-1]+' '+s[m+1][n:]
            if s[m+1][n+1] not in 'XW#':
                s[m+1]=s[m+1][0:n+1]+' '+s[m+1][n+2:]                        
            if s[m-1][n] not in 'XW#':
                s[m-1]=s[m-1][0:n]+' '+s[m-1][n+1:]
            if s[m+1][n] not in 'XW#':
                s[m+1]=s[m+1][0:n]+' '+s[m+1][n+1:]
            if s[m][n-1] not in 'XW#':
                s[m]=s[m][0:n-1]+' '+s[m][n:]
        elif KeyCode=='w':
            if s[m-1][n-1] not in 'XW#':
                s[m-1]=s[m-1][0:n-1]+' '+s[m-1][n:]
            if s[m-1][n+1] not in 'XW#':
                s[m-1]=s[m-1][0:n+1]+' '+s[m-1][n+2:]
            if s[m+1][n-1] not in 'XW#':
                s[m+1]=s[m+1][0:n-1]+' '+s[m+1][n:]
            if s[m+1][n+1] not in 'XW#':
                s[m+1]=s[m+1][0:n+1]+' '+s[m+1][n+2:]                        
            if s[m-1][n] not in 'XW#':
                s[m-1]=s[m-1][0:n]+' '+s[m-1][n+1:]
            if s[m][n-1] not in 'XW#':
                s[m]=s[m][0:n-1]+' '+s[m][n:]
            if s[m][n+1] not in 'XW#':
                s[m]=s[m][0:n+1]+' '+s[m][n+2:]
        zt();sy()     
    else:
        cv.create_text(406,402,text='材料不足')
def ZD_Z(G):
    global x,y,m,n,key,life,money,soul,tools,js,TB,wzsy,xmzs,R1,R4,Tb,Q,life2,gwhd,sb
    cv.unbind("<KeyPress-e>")
    cv.create_rectangle(379, 380, 600, 475, fill='#646464',outline = '#646464')
    cv.create_text(428,388,text='你进入了一场战斗')
    hh['0']=1          #进入战斗状态,无法移动
    cv.create_image((415, 45), image=imgs[5])  #放置怪物图片
    cv.create_text(452,15,text='鬼魂',fill='#D1EEEE')
    life2=4;gwhd=['[]','[]']
    zdxl(life2,gwhd)
    cv.pack()
    Tb=7
    if TB:  #逃跑概率改变
        Tb=12
    fight_1()
def ZD_ys(G):
    global x,y,m,n,key,life,money,soul,tools,js,TB,wzsy,xmzs,R1,R4,Tb,Q,life2,gwhd,sb
    cv.unbind("<KeyPress-e>")
    cv.create_rectangle(379, 380, 600, 475, fill='#646464',outline = '#646464')
    cv.create_text(428,388,text='你进入了一场战斗')
    hh['0']=1
    cv.create_image((415, 45), image=imgs[7])
    cv.create_text(452,15,text='异兽',fill='#A52A2A')
    life2=6;gwhd=['[]']
    zdxl(life2,gwhd)
    cv.pack()
    Tb=7
    if TB:
        Tb=12
    fight_1()
def ZD_qs(G):
    global x,y,m,n,key,life,money,soul,tools,js,TB,wzsy,xmzs,R1,R4,Tb,Q,life2,gwhd,sb
    cv.unbind("<KeyPress-e>")
    cv.create_rectangle(379, 380, 600, 475, fill='#646464',outline = '#646464')
    cv.create_text(428,388,text='你进入了一场战斗')
    hh['0']=1
    cv.create_image((415, 45), image=imgs[6])
    cv.create_text(464,15,text='游荡骑士',fill='#352f2a')
    life2=5;gwhd=['[]','[]','[]']
    zdxl(life2,gwhd)
    cv.pack()
    Tb=7
    if TB:
        Tb=12
    fight_1()
def ZD_W(G):
    global x,y,m,n,key,life,money,soul,tools,js,TB,wzsy,xmzs,R1,R4,Tb,Q,life2,gwhd,sb
    cv.unbind("<KeyPress-e>")
    cv.create_rectangle(379, 380, 600, 475, fill='#646464',outline = '#646464')
    cv.create_text(428,388,text='你进入了一场战斗')
    hh['0']=1
    cv.create_image((415, 45), image=imgs[10])
    cv.create_text(464,15,text='古城守卫')
    life2=9;gwhd=['[]','[]','[]','[]','[]']
    zdxl(life2,gwhd)
    cv.pack()
    Tb=7
    if TB:
        Tb=12
    fight_1()    
def Gcm(G):
    global money
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if money-1<0:
        cv.create_text(408,388,text='金币不够',fill='black')
    else: 
        money-=1
        tools['/']+=1
        cv.create_text(408,388,text='购买成功',fill='#FFD700')
        zt()  
def Gdp(G):
    global money
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if money-1<0:
        cv.create_text(408,388,text='金币不够',fill='black')
    else: 
        money-=1
        tools['[]']+=1
        cv.create_text(408,388,text='购买成功',fill='#FFD700')
        zt() 
def Gnj(G):
    global money
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if money-1<0:
        cv.create_text(408,388,text='金币不够',fill='black')
    else: 
        money-=1
        tools['=}']+=1
        cv.create_text(408,388,text='购买成功',fill='#FFD700')
        zt()
def Ggz(G):
    global money
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if money-2<0:
        cv.create_text(408,388,text='金币不够',fill='black')
    else: 
        money-=2
        tools['T']+=1
        cv.create_text(408,388,text='购买成功',fill='#FFD700')
        zt()
def Gxp(G):
    global money,life
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if money-2<0:
        cv.create_text(408,388,text='金币不够',fill='black')
    else: 
        money-=2
        life+=1
        cv.create_text(408,388,text='购买成功',fill='#FFD700')
        zt()
def Gdc(G):
    global money
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if money-5<0:
        cv.create_text(408,388,text='金币不够',fill='black')
    elif '洞察戒指' in dj:
        cv.create_text(433,388,text='你已经拥有该装备',fill='black')
    else: 
        money-=5
        dj['洞察戒指']=dj.get('洞察戒指',0)+1
        cv.create_text(408,388,text='购买成功',fill='#FFD700')
        zt()
def Gwzsy(G):
    global soul,wzsy
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if soul-7<0:
        cv.create_text(408,388,text='精华不够',fill='black')
    elif wzsy:
        cv.create_text(420,388,text='不能重复学习',fill='black')
    else: 
        soul-=7
        wzsy=True
        cv.create_text(408,388,text='学习成功',fill='#8DEEEE')
        zt()
def GTB(G):
    global soul,TB
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if soul-5<0:
        cv.create_text(408,388,text='精华不够',fill='black')
    elif TB:
        cv.create_text(420,388,text='不能重复学习',fill='black')
    else: 
        soul-=5
        TB=True
        cv.create_text(408,388,text='学习成功',fill='#8DEEEE')
        zt()
def Gxmzs(G):
    global soul,xmzs
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if soul-9<0:
        cv.create_text(408,388,text='精华不够',fill='black')
    elif xmzs:
        cv.create_text(420,388,text='不能重复学习',fill='black')
    else: 
        soul-=9
        xmzs=True
        cv.create_text(408,388,text='学习成功',fill='#8DEEEE')
        zt()
def Gdscj(G):
    global soul,dscj
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if soul-6<0:
        cv.create_text(408,388,text='精华不够',fill='black')
    elif dscj:
        cv.create_text(420,388,text='不能重复学习',fill='black')
    else: 
        soul-=6
        dscj=True
        cv.create_text(408,388,text='学习成功',fill='#8DEEEE')
        zt()
def Gngqj(G):
    global soul,ngqj
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if soul-9<0:
        cv.create_text(408,388,text='精华不够',fill='black')
    elif ngqj:
        cv.create_text(420,388,text='不能重复学习',fill='black')
    else: 
        soul-=9
        ngqj=True
        cv.create_text(408,388,text='学习成功',fill='#8DEEEE')
        zt()
def Gfp(G):
    global soul
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if soul-9<0:
        cv.create_text(408,388,text='精华不够',fill='black')
    elif fp!={}:
        cv.create_text(420,388,text='不能重复学习',fill='black')
    else: 
        soul-=9
        fp[0]=1
        cv.create_text(408,388,text='学习成功',fill='#8DEEEE')
        zt()
def M1(G):
    global soul
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if  soul>0 and tools['/']>0 and tools['T']>0:
        soul-=1
        tools['/']-=1
        tools['T']-=1
        cv.create_text(408,388,text='合成长刀',fill='#222222')
        wq['1:长刀']=wq.get('1:长刀',0)+3
        zt()
    else:
        cv.create_text(408,388,text='材料不足',fill='black')
def M2(G):
    global soul
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if  soul>0 and tools['=}']>0 and tools['T']>0:
        soul-=1
        tools['=}']-=1
        tools['T']-=1
        cv.create_text(408,388,text='合成弩炮',fill='#222222')
        wq['2:弩炮']=wq.get('2:弩炮',0)+3
        zt()
    else:
        cv.create_text(408,388,text='材料不足',fill='black')  
def M3(G):
    global soul
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if  soul>0 and tools['[]']>0 and tools['T']>0:
        soul-=1
        tools['[]']-=1
        tools['T']-=1
        cv.create_text(408,388,text='合成奶盾',fill='#222222')
        wq['3:奶盾']=wq.get('3:奶盾',0)+3
        zt()
    else:
        cv.create_text(408,388,text='材料不足',fill='black')
def M4(G):
    global soul
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if  soul>0 and tools['/']>0 and tools['[]']>0:
        soul-=1
        tools['/']-=1
        tools['[]']-=1
        cv.create_text(408,388,text='合成巨剑',fill='#222222')
        wq['4:巨剑']=wq.get('4:巨剑',0)+3
        zt()
    else:
        cv.create_text(408,388,text='材料不足',fill='black')
def M5(G):
    global soul
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if  soul>0 and tools['/']>0 and tools['=}']>0:
        soul-=1
        tools['/']-=1
        tools['=}']-=1
        cv.create_text(408,388,text='合成钩爪',fill='#222222')
        wq['5:钩爪']=wq.get('5:钩爪',0)+3
        zt()
    else:
        cv.create_text(408,388,text='材料不足',fill='black')
def M6(G):
    global soul
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if  soul>0 and tools['=}']>0 and tools['[]']>0:
        soul-=1
        tools['=}']-=1
        tools['[]']-=1
        cv.create_text(408,388,text='合成重盾',fill='#222222')
        wq['6:重盾']=wq.get('6:重盾',0)+3
        zt()
    else:
        cv.create_text(408,388,text='材料不足',fill='black')
def gdh(G):
    cv.create_rectangle(379, 1, 603, 95, fill='#646464',outline = '#646464')
    cv.unbind("<KeyPress-1>");cv.unbind("<KeyPress-2>")
    cv.create_text(466,10,text='对话选项:1:关于地牢 2:关于商人')
    cv.create_text(472,25,text='3:关于鬼魂 4:关于异兽 5:关于骑士')
    cv.bind("<KeyPress-1>", gdh1)
    cv.bind("<KeyPress-2>", gdh2)
    cv.bind("<KeyPress-3>", gdh3)
    cv.bind("<KeyPress-4>", gdh4)
    cv.bind("<KeyPress-5>", gdh5)
def gdh1(G):
    cv.create_rectangle(379, 38, 603, 97, fill='#646464',outline = '#646464') #对话刷新
    cv.create_text(440,45,text='你:这地牢是什么来历?')
    cv.create_text(490,60,text='神秘商人:这里以前其实是一座繁华的地下')
    cv.create_text(490,75,text='城邦。其科技水平和魔法造诣远超我们。')
    cv.create_text(484,90,text='但是之后因为一些未知的原因衰败了。')
def gdh2(G):
    cv.create_rectangle(379, 38, 603, 97, fill='#646464',outline = '#646464')
    cv.create_text(435,45,text='你:你为什么在这里?')
    cv.create_text(488,60,text='神秘商人:我跟你一样,都是来这里探索的')
    cv.create_text(490,75,text='冒险家。不过显然，我来得比你早得多。')
def gdh3(G):
    cv.create_rectangle(379, 38, 603, 97, fill='#646464',outline = '#646464')
    cv.create_text(484,45,text='神秘商人:鬼魂是个缠人的家伙。闻着味')
    cv.create_text(483,60,text='就会赶来追你。不过你可以在异兽的肚')
    cv.create_text(483,75,text='子里找到护身符。因为它们曾吃了不少')
    cv.create_text(424,90,text='魔法学院的人。')
def gdh4(G):
    cv.create_rectangle(379, 38, 603, 97, fill='#646464',outline = '#646464')
    cv.create_text(487,45,text='神秘商人:这些异兽毫无疑问,都是从地上')
    cv.create_text(490,60,text='跑来在这地牢里栖身的。这种生物生命力')
    cv.create_text(490,75,text='极其顽强。无论在世界的哪一个角落。你')
    cv.create_text(442,90,text='都能看到它们的身影。')
def gdh5(G):
    cv.create_rectangle(379, 38, 603, 97, fill='#646464',outline = '#646464')
    cv.create_text(491,45,text='神秘商人:据说是与远古君王签订魔法契约')
    cv.create_text(490,60,text='的侍卫骑士团，君王死后却依然保留着原')
    cv.create_text(484,75,text='始的战斗意识。我劝你不要轻易靠近。')
def gjy(G):
    global money,key,T5g,tools
    cv.unbind("<KeyPress-1>");cv.unbind("<KeyPress-2>")
    cv.create_rectangle(379, 1, 603, 95, fill='#646464',outline = '#646464')
    cv.create_text(490,10,text='神秘商人:“我这有廉价的镐子,金币制成的')
    cv.create_text(491,25,text='钥匙，躲避鬼魂的护身符和清除四周的爆')
    cv.create_text(409,40,text='破炸弹。”')
    cv.create_text(488,58,text='1:镐子=1金币(上限六个)  2:钥匙=1金币')
    cv.create_text(488,73,text='3:护身符=6金币       4:爆破炸弹=6精华')
    cv.bind("<KeyPress-1>", gjyT)
    cv.bind("<KeyPress-2>", gjykey)
    cv.bind("<KeyPress-3>", gjyhsf)
    cv.bind("<KeyPress-4>", gjyzd)
def gjyT(G):
    global money,T5g,tools
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if money-1<0:
        cv.create_text(408,388,text='金币不够',fill='black')
    elif T5g>5:
        cv.create_text(420,388,text='已达购买上限')
    else:
        money-=1
        tools['T']+=1
        cv.create_text(408,388,text='购买成功',fill='#FFD700')
        T5g+=1
        zt()
def gjykey(G):
    global money,key
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if money-1<0:
        cv.create_text(408,388,text='金币不够',fill='black')
    else:
        money-=1
        key+=1
        cv.create_text(408,388,text='购买成功',fill='#FFD700')
        zt()
def gjyhsf(G):
    global money
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if money-6<0:
        cv.create_text(408,388,text='金币不够',fill='black')
    elif '护身符δ' in dj:
        cv.create_text(433,388,text='你已经拥有该装备',fill='black')    
    else:
        money-=6
        dj['护身符δ']=dj.get('护身符δ',0)+1
        cv.create_text(408,388,text='购买成功',fill='#FFD700')
        zt()
def gjyzd(G):
    global soul
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if soul-6<0:
        cv.create_text(408,388,text='精华不够',fill='black')
    else:
        soul-=6
        dj['爆破炸弹']=dj.get('爆破炸弹',0)+1
        cv.create_text(408,388,text='购买成功',fill='#FFD700')
        zt()
def ZQ(zq):
    global cj,money
    tools['T']-=1
    cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
    if dscj:
        if randint(0,1)!=0:
            cv.create_text(415,388,text='挖出金币+1',fill='#FFD700') 
            cj+=1
            money+=1
    s[m]=s[m][0:n]+' '+s[m][n+1:]
    zt();sy()
def ZYK(G):               #各职业选择
    global x,y,m,n,key,life,money,soul,tools,TB,wzsy,dscj,ngqj,xmzs,player,wq,dj
    player='K'
    s[x]=s[x][0:y]+player+s[x][y+1:]
    life=6
    key=3
    money=6
    soul=2
    dj={}
    tools={'/':4,'[]':5,'=}':0,'T':5}
    wq={'1:长刀':6,'6:重盾':5}
    cv.unbind("<F1>");cv.unbind("<F2>");cv.unbind("<F3>");cv.unbind("<F4>")  #禁止中途换职业
    cv.unbind("<F5>");cv.unbind("<F6>");cv.unbind("<F7>");cv.unbind("<F8>")
    sy()
def ZYF(G):
    global x,y,m,n,key,life,money,soul,tools,TB,wzsy,dscj,ngqj,xmzs,player,wq,dj
    player='F'
    s[x]=s[x][0:y]+player+s[x][y+1:]
    life=4
    key=3
    money=7
    soul=7
    dj={'护身符δ':1}
    tools={'/':3,'[]':3,'=}':0,'T':5}
    wq={'5:钩爪':5,'3:奶盾':4}
    dscj=True
    cv.unbind("<F1>");cv.unbind("<F2>");cv.unbind("<F3>");cv.unbind("<F4>")
    cv.unbind("<F5>");cv.unbind("<F6>");cv.unbind("<F7>");cv.unbind("<F8>")
    sy()
def ZYS(G):
    global x,y,m,n,key,life,money,soul,tools,TB,wzsy,dscj,ngqj,xmzs,player,wq,dj
    player='S'
    s[x]=s[x][0:y]+player+s[x][y+1:]
    life=5
    key=4
    money=6
    soul=2
    dj={'洞察戒指':1}
    tools={'/':4,'[]':4,'=}':5,'T':5}
    wq={'5:钩爪':4,'2:弩炮':4}
    TB=True
    cv.unbind("<F1>");cv.unbind("<F2>");cv.unbind("<F3>");cv.unbind("<F4>")
    cv.unbind("<F5>");cv.unbind("<F6>");cv.unbind("<F7>");cv.unbind("<F8>")
    sy()
def ZYH(G):
    global x,y,m,n,key,life,money,soul,tools,TB,wzsy,dscj,ngqj,xmzs,player,wq,dj
    player='H'
    s[x]=s[x][0:y]+player+s[x][y+1:]
    life=4
    key=3
    money=8
    soul=4
    dj={}
    tools={'/':4,'[]':3,'=}':4,'T':6}
    wq={'3:奶盾':7}
    fp[0]=1
    cv.unbind("<F1>");cv.unbind("<F2>");cv.unbind("<F3>");cv.unbind("<F4>")
    cv.unbind("<F5>");cv.unbind("<F6>");cv.unbind("<F7>");cv.unbind("<F8>")
    sy()
def ZYR(G):
    global x,y,m,n,key,life,money,soul,tools,TB,wzsy,dscj,ngqj,xmzs,player,wq,dj
    player='R'
    s[x]=s[x][0:y]+player+s[x][y+1:]
    life=6
    key=3
    money=6
    soul=0
    dj={}
    tools={'/':3,'[]':5,'=}':0,'T':8}
    wq={'4:巨剑':4,'6:重盾':3}
    ngqj=True
    cv.unbind("<F1>");cv.unbind("<F2>");cv.unbind("<F3>");cv.unbind("<F4>")
    cv.unbind("<F5>");cv.unbind("<F6>");cv.unbind("<F7>");cv.unbind("<F8>")
    sy()
def ZYY(G):
    global x,y,m,n,key,life,money,soul,tools,TB,wzsy,dscj,ngqj,xmzs,player,wq,dj
    player='Y'
    s[x]=s[x][0:y]+player+s[x][y+1:]
    life=6
    key=0
    money=4
    soul=5
    dj={'洞察戒指':1}
    tools={'/':4,'[]':4,'=}':0,'T':5}
    wq={'5:钩爪':5,'4:巨剑':5}
    xmzs=True
    cv.unbind("<F1>");cv.unbind("<F2>");cv.unbind("<F3>");cv.unbind("<F4>")
    cv.unbind("<F5>");cv.unbind("<F6>");cv.unbind("<F7>");cv.unbind("<F8>")
    sy()
def ZYD(G):
    global x,y,m,n,key,life,money,soul,tools,TB,wzsy,dscj,ngqj,xmzs,player,wq,dj
    player='D'
    s[x]=s[x][0:y]+player+s[x][y+1:]
    life=5
    key=3
    money=5
    soul=3
    dj={'爆破炸弹':2}
    tools={'/':3,'[]':4,'=}':3,'T':5}
    wq={'2:弩炮':5,'4:巨剑':5}
    cv.unbind("<F1>");cv.unbind("<F2>");cv.unbind("<F3>");cv.unbind("<F4>")
    cv.unbind("<F5>");cv.unbind("<F6>");cv.unbind("<F7>");cv.unbind("<F8>")
    sy()
def ZYV(G):
    global x,y,m,n,key,life,money,soul,tools,TB,wzsy,dscj,ngqj,xmzs,player,wq,dj
    player='V'
    s[x]=s[x][0:y]+player+s[x][y+1:]
    life=5
    key=3
    money=6
    soul=2
    dj={}
    tools={'/':4,'[]':4,'=}':4,'T':5}
    wq={'1:长刀':3,'2:弩炮':3,'4:巨剑':2,'5:钩爪':2,'3:奶盾':1}
    wzsy=True
    cv.unbind("<F1>");cv.unbind("<F2>");cv.unbind("<F3>");cv.unbind("<F4>")
    cv.unbind("<F5>");cv.unbind("<F6>");cv.unbind("<F7>");cv.unbind("<F8>")
    sy()
def callback(event):
    global x,y,m,n,key,life,money,soul,tools,js,cj,bf,lj,TB,wzsy,dscj,ngqj,xmzs,T5g,player,wq,dj,KeyCode
    jrz()
    KeyCode=event.keysym
    if (KeyCode=='w' or KeyCode=='W') and hh['0']==0 and qq['0']==0:    #向上移动
        m=x-1;n=y
        zt()
        ww()
        if zjr:
            zyd()
        sy()              
    elif (KeyCode=='a' or KeyCode=='A') and hh['0']==0 and qq['0']==0:  #向左移动
        m=x;n=y-1
        zt()
        ww()
        if zjr:
            zyd()
        sy()    
    elif (KeyCode=='s' or KeyCode=='S') and hh['0']==0 and qq['0']==0:  #向下移动
        m=x+1;n=y
        zt()
        ww()
        if zjr:
            zyd()
        sy()    
    elif (KeyCode=='d' or KeyCode=='D') and hh['0']==0 and qq['0']==0:  #向右移动
        m=x;n=y+1
        zt()
        ww()
        if zjr:
            zyd()
        sy()                
    elif KeyCode=='Escape': 
        chju()
        showinfo(title="游戏结束", message=" 您到达的地牢层数:第"+str(dl)+"层")

    elif KeyCode=='q' and hh['0']==0 and qq['0']==0:
        cv.create_rectangle(379, 380, 600, 475, fill='#646464',outline = '#646464')
        if '爆破炸弹' not in dj:
            cv.create_text(418,388,text='你没有该道具')  
        elif dj['爆破炸弹']==0:
            
            cv.create_text(418,388,text='你没有该道具')  
        else:
            sy()
            cv.create_text(470,388,text='爆破炸弹已就绪，请选择放置方向')
            cv.create_text(458,402,text='按方向键放置, 按 q 取消放置')
            qq['0']=1    #进入炸弹放置状态
    elif KeyCode=='q' and hh['0']==0 and qq['0']==1:
        cv.create_rectangle(379, 380, 600, 475, fill='#646464',outline = '#646464')
        qq['0']=0        #解除炸弹放置状态
        cv.create_text(400,388,text='已取消')
    elif qq['0']==1 and (KeyCode=='w' or KeyCode=='W'):
        cv.create_rectangle(379, 380, 600, 475, fill='#646464',outline = '#646464')
        if s[x-1][y] in 'XW#':
            cv.create_text(406,388,text='无法放置')
        else:
            cv.create_text(424,388,text='已安置爆破炸弹',fill='#8B0000')
            dj['爆破炸弹']-=1
            s[x-1]=s[x-1][0:y]+'Q'+s[x-1][y+1:]
            sy()
            qq['0']=0
    elif qq['0']==1 and (KeyCode=='a' or KeyCode=='A'):
        cv.create_rectangle(379, 380, 600, 475, fill='#646464',outline = '#646464')
        if s[x][y-1] in 'XW#':
            cv.create_text(406,388,text='无法放置')
        else:
            cv.create_text(424,388,text='已安置爆破炸弹',fill='#8B0000')
            dj['爆破炸弹']-=1
            s[x]=s[x][0:y-1]+'Q'+s[x][y:]
            sy()
            qq['0']=0
    elif qq['0']==1 and (KeyCode=='s' or KeyCode=='S'):
        cv.create_rectangle(379, 380, 600, 475, fill='#646464',outline = '#646464')
        if s[x+1][y] in 'XW#':
            cv.create_text(406,388,text='无法放置')
        else:
            cv.create_text(424,388,text='已安置爆破炸弹',fill='#8B0000')
            dj['爆破炸弹']-=1
            s[x+1]=s[x+1][0:y]+'Q'+s[x+1][y+1:]
            sy()
            qq['0']=0
    elif qq['0']==1 and (KeyCode=='d' or KeyCode=='D'):
        cv.create_rectangle(379, 380, 600, 475, fill='#646464',outline = '#646464')
        if s[x][y+1] in 'XW#':
            cv.create_text(406,388,text='无法放置')
        else:
            cv.create_text(424,388,text='已安置爆破炸弹',fill='#8B0000')
            dj['爆破炸弹']-=1
            s[x]=s[x][0:y+1]+'Q'+s[x][y+2:]
            sy()
            qq['0']=0
    else:
        cv.create_rectangle(379, 380, 600, 475, fill='#646464',outline = '#646464')
        cv.create_text(406,388,text='无效步骤',fill='black')    
def scmap():
    global dl,s,x,y,js,cj,bf,lj,zx,zy,zydx,zydy,zjr,T5g
    s=map1
    rr=randint(2,3)    #神秘商人出现概率
    ran=randint(1,3)   #地图种类概率
    dl+=1
    if ran!=1:                  #正常关卡
        for i in range(2,19):
            for j in range(2,19):
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
        x,y=2,2
        s[x]=s[x][0:y]+player+s[x][y+1:]
        Sx=randint(10,17);Sy=randint(10,17)
        s[Sx]=s[Sx][0:Sy]+'G'+s[Sx][Sy+1:]
        Sx=randint(14,17);Sy=randint(14,17)
        s[Sx]=s[Sx][0:Sy]+'#'+s[Sx][Sy+1:]
        if dl%rr==0:
            gx=randint(5,9)
            gy=randint(5,9)
            s[gx]=s[gx][0:gy]+'g'+s[gx][gy+1:]
        js,cj,bf,lj=0,0,0,0
    if ran==1:                 #奖励关
        for i in range(2,19):
            for j in range(2,19):
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
        x,y=2,2
        s[x]=s[x][0:y]+player+s[x][y+1:]
        Sx=randint(10,17);Sy=randint(10,17)
        s[Sx]=s[Sx][0:Sy]+'G'+s[Sx][Sy+1:]
        Sx=randint(14,17);Sy=randint(14,17)
        s[Sx]=s[Sx][0:Sy]+'#'+s[Sx][Sy+1:]            
        if dl%rr==0:
            gx=randint(5,9)
            gy=randint(5,9)
            s[gx]=s[gx][0:gy]+'g'+s[gx][gy+1:]
        js,cj,bf,lj=0,0,0,0
    if dl%6==0:              #boss房
        cv.create_rectangle(379, 380, 600, 395, fill='#646464',outline = '#646464')
        cv.create_text(418,388,text='你来到了战壕')   
        s=['XXXXXXXXX',
           'XXXXXXXXX',
           'XX     XX',
           'XX XWX XX',
           'XX W#W XX',
           'XX XWX XX',
           'XX     XX',
           'XXXXXXXXX',
           'XXXXXXXXX']
        x,y=2,2
        s[x]=s[x][0:y]+player+s[x][y+1:]
        js,cj,bf,lj=0,0,0,0
    zx,zy=0,0
    zydx,zydy=0,0
    zjr=False
    T5g=0
    zt() 
cv.pack()
def xsjc():
    showinfo(title="新手教程", message="wasd移动(英文键盘),esc退出,F1~F8选择初始职业\n按q放置炸弹(如果有)")
def zyxz():
    showinfo(title="按F1~F8选择职业", message=" F1.骑士;F2.法师;F3.游侠;F4.医生;F5.工匠;F6.魔人;F7.炮手;F8.猎人")
def tj():
    showinfo(title="图鉴", message="<魔法祭台中的魔法>:\n|{无中生有}:闪避成功获得装备|{隐身咒语}:100%逃跑|\n|{血魔之手}:拳头攻击吸血|{点石成金}:挖墙概率获得金币|\n|{能工巧匠}:开宝箱概率不消耗钥匙|{眼疾手快}:不会被宝箱怪咬到|\n<合成祭台中合成的武器>:\n|{长刀}:100%命中,伤害1~2|{弩炮}:概率连击,伤害1~3|\n|{奶盾}:加两滴血和两层护盾|巨剑:伤害2~3||{重盾}:加三层护盾,伤害1|\n|{勾爪}:伤害1~2,吸血一滴|高级护盾格挡失败不消耗")
b0 = Button(root, text="新手教程", command=xsjc).pack(side='left')
b1 = Button(root, text="职业选择", command=zyxz).pack(side='left')
b2 = Button(root, text="图鉴", command=tj).pack(side='left')
scmap()
sy()
cv.bind("<F1>", ZYK);cv.bind("<F2>", ZYF);cv.bind("<F3>", ZYS);cv.bind("<F4>", ZYH)
cv.bind("<F5>", ZYR);cv.bind("<F6>", ZYY);cv.bind("<F7>", ZYD);cv.bind("<F8>", ZYV)
cv.bind("<KeyPress>", callback)
cv.pack()
cv.focus_set()  
root.mainloop()
