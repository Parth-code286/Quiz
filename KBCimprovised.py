a = input("Enter Your Name : ")
# b = int(input("Enter Your Age : "))
print("Welcome",a,"to KBC Quiz Game")
print('''Read the instructions carefully
      1]After display of the question you have to select any of the four options
      2]If you don't know the answer you have lifeline
      3]For every correct answer you get 100 points
      🔥🔥LESS GO!🔥🔥''')  
print("You have 3 questions")
question1 = ["While buying a laptop what should be looked for ?","Which is the best laptop for coding ?","Which is best OS ?"]  
print(question1[0])
print('''
1)Processor       2)Display
3)Battery Life    4)Depends upon the use case
             5)Lifeline''')
x = int(input("Give Your Answer as Option No. "))
match x:
    case 1: print("Wrong Answer")
    case 2: print("Wrong Answer")
    case 3: print("Wrong Answer")
    case 4: print("Correct Answer")
    case 5: print('''Choose Your Answer again : ''')
if x==5 :
    print('''1)Processor 2)---  3)----    4)Depends upon the use case
                        ''')
    q = int(input("Give Your Answer again"))        
    match q:
        case 1: print("Wrong Answer")
        case 2: print("Correct Answer")
else :
    print("GO Ahead")        
print(question1[1])
print('''
1)ACER Nitro V       2)ASUS Vivobook S15 OLED
3)HP Victus 15    4)MacBook Air M1
       5)Lifeline''')
y = int(input("Give Your Answer as Option No. "))
match y:
    case 1: print("Wrong Answer")
    case 2: print("Wrong Answer")
    case 3: print("Wrong Answer")
    case 4: print("Correct Answer")
    case 5: print('''Choose Your Answer again : ''')
if y==5 :
    print("1)----       2)---   3)HP Victus 15   4)MacBook Air M1 ")
    f = int(input("Give Your Answer again"))        
    match f:
        case 3: print("Wrong Answer")
        case 4: print("Correct Answer")
else :
    print("GO Ahead")          
        
print(question1[2])
print('''1)Windows 2)Mac OS 3)Kali Linux 4)Ubuntu 5)Lifeline''')
z = int(input("Give Your Answer as Option No. "))
match z:
    case 1: print("Wrong Answer")
    case 2: print("Wrong Answer")
    case 3: print("Wrong Answer")
    case 4: print("Correct Answer")
    case 5: print('''Choose Your Answer again : ''')
if z==5 : 
    print('''1)Windows 2)Mac OS 3)----    4)----
                        ''')
    o = int(input("Give Your Answer again"))        
    match o:
        case 1: print("You're Wrong")
        case 2: print("You're correct")        
s = int(input("Enter Your Score : "))
if s>50 :
    print("Good Score")  
elif s>200 :
    print("Awesome Score")    
elif s==300 :
    print("Full Score !")   


    
