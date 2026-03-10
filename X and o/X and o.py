
#game board
board=["","",""]
board1=["","",""]
board2=["","",""]
#gameboard entered 
n=[]
#game info
game_username=''
game_username2=''
gu=''
gu2=''
#game points
xpoints=0
opoints=0

try:
  def game_user():
    global user_letter
    global game_username
    global n
    global board
    global board1
    global board2
    global xpoints
    global opoints
    user_letter=input('Enter the letter you want to make use of (x or o):').lower()
    if user_letter.replace(" "," ").isalpha():
       if user_letter=='x' or user_letter=='o':
         rc=input("Enter the position you what "+user_letter+" to be (only number): ")
         if int(rc)==1 and rc not in n:
            n.extend([rc])
            board[0]+=user_letter
            print(board) 
            print(board1) 
            print(board2)
            print(n)
            if_win()
         elif int(rc)==2 and rc not in n:
            n.extend([rc])
            board[1]+=user_letter
            print(board) 
            print(board1) 
            print(board2)
            print(n)
            if_win()
         elif int(rc)==3 and rc not  in n:
            n.extend([rc])
            board[2]+=user_letter
            print(board) 
            print(board1) 
            print(board2)
            print(n)
            if_win()
         elif int(rc)==4 and rc not  in n:
            n.extend([rc])
            board1[0]+=user_letter
            print(board) 
            print(board1) 
            print(board2)
            print(n)
            if_win()
         elif int(rc)==5 and rc not  in n:
            n.extend([rc])
            board1[1]+=user_letter
            print(board) 
            print(board1) 
            print(board2[0:3])
            print(n)
            if_win()
         elif int(rc)==6 and rc not  in n:
            n.extend([rc])
            board1[2]+=user_letter
            print(board) 
            print(board1) 
            print(board2)
            print(n)
            if_win()
         elif int(rc)==7 and rc not  in n:
            n.extend([rc])
            board2[0]+=user_letter
            print(board) 
            print(board1) 
            print(board2)
            print(n)
            if_win()
         elif int(rc)==8 and rc not  in n:
            n.extend([rc])
            board2[1]+=user_letter
            print(board) 
            print(board1) 
            print(board2)
            print(n)
            if_win()
         elif int(rc)==9 and rc not  in n:
            n.extend([rc])
            board2[2]+=user_letter
            print(board) 
            print(board1) 
            print(board2)
            print(n)
            if_win()
         else:
             print("invalid data type")
       else:
            print("invalid letter make sure it is either x or o")
    else:
      print("invalid letter choose letters not numbers")

  def if_win():
    global board
    global board1
    global board2
    global game_username
    global game_username2
    global xpoints
    global opoints
    global n
# straight win (horizontal)
    # x
    if board[0]=='x' and board[1]=='x'and board[2]=='x':
       xpoints+=3
       print(game_username+" You have just won and you have "+str(xpoints)+" points")
       board=["","",""]
       board1=["","",""]
       board2=["","",""]
       n=[]
       game_user()
    # o    
    elif board[0]=='o' and board[1]=='o'and board[2]=='o':
       opoints+=3  
       print(game_username2+" You have just won and you have "+str(opoints)+" points")
       board=["","",""]
       board1=["","",""]
       board2=["","",""]
       n=[]
       game_user()
    # x
    elif board1[0]=='x' and board1[1]=='x'and board1[2]=='x':
       xpoints+=3 
       print(game_username2+" You have just won and you have "+str(xpoints)+" points")
       board=["","",""]
       board1=["","",""]
       board2=["","",""]
       n=[]
       game_user()
    # o   
    elif board1[0]=='o' and board1[1]=='o'and board1[2]=='o':
       opoints+=3 
       print(game_username2+" You have just won and you have "+str(opoints)+" points")
       board=["","",""]
       board1=["","",""]
       board2=["","",""]
       n=[]
       game_user()
    # x
    elif board2[0]=='x' and board2[1]=='x'and board2[2]=='x':
       xpoints+=3 
       print(game_username2+" You have just won and you have "+str(xpoints)+" points")
       board=["","",""]
       board1=["","",""]
       board2=["","",""]
       n=[]
       game_user()
    # o   
    elif board2[0]=='o' and board2[1]=='o'and board2[2]=='o':
       opoints+=3 
       print(game_username2+" You have just won and you have "+str(opoints)+" points")
       board=["","",""]
       board1=["","",""]
       board2=["","",""]
       n=[]
       game_user()
# straight win (vertical)
    # x
    elif board[0]=='x' and board1[0]=='x'and board2[0]=='x':
       xpoints+=3
       print(game_username+" You have just won and you have "+str(xpoints)+" points")
       board=["","",""]
       board1=["","",""]
       board2=["","",""]
       n=[]
       game_user()
    # o
    elif board[0]=='o' and board1[0]=='o' and board2[0]=='o':
       opoints+=3
       print(game_username+" You have just won and you have "+str(opoints)+" points")
       board=["","",""]
       board1=["","",""]
       board2=["","",""]
       n=[]
       game_user()
    # x   
    elif board[1]=='x' and board1[1]=='x'and board2[1]=='x':
       xpoints+=3
       print(game_username+" You have just won and you have "+str(xpoints)+" points")
       board=["","",""]
       board1=["","",""]
       board2=["","",""]
       n=[]
       game_user()
    # o
    elif board[0]=='o' and board1[0]=='o' and board2[0]=='o':
       opoints+=3
       print(game_username+" You have just won and you have "+str(opoints)+" points")
       board=["","",""]
       board1=["","",""]
       board2=["","",""]
       n=[]
       game_user()
    # x   
    elif board[1]=='x' and board1[1]=='x' and board2[1]=='x':
       xpoints+=3
       print(game_username+" You have just won and you have "+str(xpoints)+" points")
       board=["","",""]
       board1=["","",""]
       board2=["","",""]
       n=[]
       game_user()
     # o   
    elif board[1]=='o' and board1[1]=='o' and board2[1]=='o':
       opoints+=3
       print(game_username+" You have just won and you have "+str(opoints)+" points")
       board=["","",""]
       board1=["","",""]
       board2=["","",""]
       n=[]
       game_user()  
    # x
    elif board[2]=='x' and board1[2]=='x' and board2[2]=='x':
       xpoints+=3
       print(game_username+" You have just won and you have "+str(xpoints)+" points")
       board=["","",""]
       board1=["","",""]
       board2=["","",""]
       n=[]
       game_user()
    # o 
    elif board[2]=='o' and board1[2]=='o' and board2[2]=='o':
       opoints+=3
       print(game_username+" You have just won and you have "+str(opoints)+" points")
       board=["","",""]
       board1=["","",""]
       board2=["","",""]
       n=[]
       game_user()     
# right cross
    # x 
    elif board[2]=='x' and board1[1]=='x' and board2[0]=='x':
            xpoints+=3
            print(game_username+" You have just won and you have "+str(xpoints)+" points")
            board=["","",""]
            board1=["","",""]
            board2=["","",""]
            n=[]
            game_user()
     # o       
    elif board[2]=='o' and board1[1]=='o' and board2[0]=='o':
            opoints+=3
            print(game_username+" You have just won and you have "+str(opoints)+" points")
            board=["","",""]
            board1=["","",""]
            board2=["","",""]
            n=[]
            game_user()
            
# left cross win          
    # x 
    elif board[0]=='x' and board1[1]=='x' and board2[2]=='x':
            xpoints+=3
            print(game_username+" You have just won and you have "+str(xpoints)+" points")
            board=["","",""]
            board1=["","",""]
            board2=["","",""]
            n=[]
            game_user()   
     # o
    elif board[0]=='o' and board1[1]=='o' and board2[2]=='o':
            opoints+=3
            print(game_username+" You have just won and you have "+str(opoints)+" points")
            board=["","",""]
            board1=["","",""]
            board2=["","",""]
            n=[]
            game_user()   



 
  def Game():
   global n
   global board
   global board1
   global board2
   global gu
   global gu2
   global game_username
   global game_username2
   print(board) 
   print(board1) 
   print(board2)
   game_username=input('Enter Your game user name 1(x): ')
   game_username2=input('Enter Your game user name 2(o): ')
   if game_username.replace(" "," ").isalpha() and game_username2.replace(" "," ").isalpha():
       gu=game_username[0].upper()+game_username[1:]
       gu2=game_username2[0].upper()+game_username2[1:]
       print("Welcome "+gu+" and "+gu2+" to X and O game")
       print("Example:(x in the 7th positions)")
       print("Example:(o in the 1st positions)")
       print("please when inputing your value for position, it must be only number")
       print("Enter the position you what x or o to be (only number):7")
       Eboard=  ["o","",""]
       Eboard1= ["","",""]
       Eboard2= ["x","",""]
       print(Eboard) 
       print(Eboard1) 
       print(Eboard2)
       while True:
          game_user()
                 
   else:
       print('invalid')
       Game()
           

  Game()


except ValueError:
    print('Value error (cause by either inputting string instead of int,or other reasons))')


