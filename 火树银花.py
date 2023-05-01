import turtle  
import random as rm
angle=[15,5,10,20,25,30]
color=['yellow','green','blue','red','pink','cyan']

def draw_tree(branchlen,t,cr):
    t.color(cr)
    t.pensize(1)

    new_color=color[:]
    new_color.remove(cr)
    new_cr=rm.choice(new_color)


    ag1=rm.choice(angle)
    ag2=rm.choice(angle)

    newbranchlen=branchlen

    if branchlen>120:
        newbranchlen=branchlen-20
    elif branchlen>=60:
        newbranchlen=branchlen-15
    elif branchlen>=20:
        newbranchlen=branchlen-10
    else:
        
        newbranchlen=branchlen-5
    if 10 >=branchlen:
        pass
    else:
        t.fd(branchlen)
        t.right(ag1)
        draw_tree(newbranchlen,t,new_cr)
        t.left(ag1+ag2)
        draw_tree(newbranchlen,t,new_cr)
        t.right(ag2)
        t.color(cr)
        t.backward(branchlen)

#开始绘制整棵树
def  draw_fire_ciliver():
    
    t = turtle.Turtle()
    w = turtle.Screen()
    w.bgcolor('black')
   
    w.setup(1200, 800, 200, 50)
    t.left(90)

    t.speed(10)   
    t.up()
    t.backward(250)
    t.down()
    
    turtle.tracer(5)
    
    t.left(15)
    for i in range(0,3):
        print('===绘制第['+str(i+1)+']棵树')
        draw_tree(120,t,'cyan')
        t.right(5)
    

#主程序入口
if __name__== '__main__':
    
    print('开始绘制火树银花')
    draw_fire_ciliver()
    print('结束绘制火树银花')
    input('暂停，等待输入（输入任意内容按回车键可退出）：')


### 导入海龟作图模块
##import turtle
### 导入随机数模块
##import random as rm
##
### 角度
##angle = [15, 5, 10, 20, 25, 30]
### 颜色数组，多种颜色供绘制时随机选择，青、红、粉、蓝、绿、黄
##color = ['yellow', 'green', 'blue', 'red', 'pink', 'cyan']
##
### 绘制树干，传入长度、画布对象
### 绘制思路：根据长度的不同，生成的角度不同，树干会分为2个树枝，然后树枝再递归分叉
### 直到树枝的长度过小，变为树枝末梢，不再分叉
##def draw_tree(branch_len, t, cr):
##    # 树干颜色
##    t.color(cr)
##    # 设置画笔的粗细
##    t.pensize(1)
##    # 随机选择颜色，不等于树干颜色，用于分叉树枝
##    new_color = color[:]
##    new_color.remove(cr)
##    new_cr = rm.choice(new_color)
##    # 随机转动角度，用于分叉树枝
##    ag1 = rm.choice(angle)
##    ag2 = rm.choice(angle)
##    # 分叉树枝的长度，默认等于树干的长度
##    new_branch_len = branch_len
##    # 分叉树枝的长度重新计算，越来越短
##    if branch_len > 120:
##        new_branch_len = branch_len - 20
##    elif branch_len >= 60:
##        new_branch_len = branch_len - 15
##    elif branch_len >= 20:
##        new_branch_len = branch_len - 10
##    else:
##        new_branch_len = branch_len - 5
##    # 开始绘制
##    if 10 >= branch_len:
##        # 树枝太短，无需绘制，递归结束
##        pass
##    else:
##        # 向前移动，绘制树干
##        t.forward(branch_len)
##        # 右转指定角度1，分叉
##        t.right(ag1)
##        # 递归画树干，可以理解成子树
##        draw_tree(new_branch_len, t, new_cr)
##        # 左转指定角度2，分叉
##        t.left(ag1 + ag2)
##        draw_tree(new_branch_len, t, new_cr)
##        # 角度回正，右转指定角度2
##        t.right(ag2)
##        # 恢复颜色并后退
##        t.color(cr)
##        t.backward(branch_len)
##
### 开始绘制整棵树
##def draw_fire_cilver():
##    t = turtle.Turtle()
##    w = turtle.Screen()
##    # 设置背景为黑色
##    w.bgcolor('black')
##    # 设置弹框大小，4个参数：宽度、高度、起始值x轴、起始值y轴
##    w.setup(1200, 800, 200, 50)
##    # 加快速度
##    t.speed(10)
##    # 调整画笔的位置，开始的位置在中间偏下方
##    t.left(90)
##    t.up()
##    t.backward(400)
##    t.down()
##    # 跟踪画笔，可以看到整个绘制轨迹
##    turtle.tracer(5)
##    # 垂直位置绘制1棵，左右边再各绘制3棵，共7棵
##    t.left(15)
##    for i in range(0,7):
##        # 绘制1棵，右转5度
##        print('====绘制第[' + str(i + 1) + ']棵树')
##        draw_tree(150, t, 'cyan')
##        t.right(5)
##    # 单机退出
##    w.exitonclick()
##
### 主程序入口
##if __name__ == '__main__':
##    print('开始绘制火树银花')
##    draw_fire_cilver()
##    print('结束绘制火树银花')
##    # input('暂停，等待输入（输入任意内容按回车键可退出）：')
##
