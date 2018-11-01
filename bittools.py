def tc(n,width=4):
    a="{:0{width}}".format(int(str(bin(n))[2:]),width=8*width)
    b=a.replace('1','2').replace('0','1').replace('2','0')
    b=int(b,2)+1
    return b

