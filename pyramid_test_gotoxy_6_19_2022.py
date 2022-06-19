#RSM pyramid test last uses gotoxy
import time
import os
def gotoxy(x,y):
      #range start of x y is x =1 to up, y =1 to up
      print ("%c[%d;%df" % (0x1B, y, x), end='')
def fPyr_test(n):
      os.system("clear")
      #sa screen nakabase ang gotoxy at hindi sa next line
      gotoxy(2, 3)
      #kaylangan flush = True para gumalaw kada sleep ng print
      print(f"\nTriangle height is: {n}\n\n\n", end="", flush= True)
      i_y = 0
      #left side using "*" gilid ng triangle
      #aditional +2 for top botton and left border
      while i_y < n+2:
            j_x = 0
            j_x_len = i_y +1 
            #            +2 left and right border
            while j_x < n+2:
                  #staring top left at top right ung range ng x y
                  gotoxy(j_x +2, i_y+ 5)                  
                  if i_y == 0 or i_y == ( (n+2) -2) + 1:
                        print("*", end = "", flush =True)
                  else: #reverse version ng condition ng fPyr_left_blank
                        if j_x == 0 or ( j_x >= j_x_len and j_x <= ( (n+2 )-2) +1 ):
                              print("*", end = "", flush =True)
                        else:
                              print(" ", end = "", flush =True) 
                  j_x+=1
                  time.sleep(.1)
            i_y+=1
      print()
print("input height of triangle max 10:  ", end="")
inp = int(input())
fPyr_test(inp)