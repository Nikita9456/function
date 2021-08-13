# question_list=["1.how many continents are there?",
#                "2.what is the capital of india?",
#                "3.ng ki miss navgurukul kon hai?"]
# option_list=[["1.four","2.nine","3.seven","4.eight"],
#              ["1.chandigarh","2.bhopal","3chennai","4.delhi"],
#              ["1.nikita","pooja","teena","rekha"]]
# solution_list=[3,4,1]
# answer_list=["3.seven","4.eight","3.chennai","4.delhi","1.nkita","2.teena"]
def kbc(question,option,solution,answer):
def option(option):
def sel(solution):
def ans(answer):
def lyf(life):
    i=0
    n=1
    m=0
    count=0
    amount=10000
    while i<len(question):
        print(question[i])
        j=0 
        while j<len(option[i]):
            #print(option[i][j])
            kbc("1. how many containes are there")
            j+=1
        lifeline=input("do you want 5050 lifeline")
        if lifeline=="yes":
            #print(5050)
            lyf(5050)
            if count==0:
                print(answer[m+i])
                print(answer[m+n])
                num=int(input("enter the answer"))
                if num==solution[i]:
                    print("your answer is correct")
                    print("you won",amount)
                else:
                    print("your answer is wrong")
                    print("you loose the game")
                    break
                count+=1
            else:
                print("you already used lifeline")
                e=int(input("enter the answer"))
                if e==solution[i]:
                    print("your answer is correct")
                    print("you won",amount)
                else:
                    print("your answer is wrong")
                    print("you loose the game")
                    break
        elif lifeline=="no":
            f=int(input("enter the answer"))
            if f==solution[i]:
                print("your answer is correct")
                print("you won",amount)
            else:
                print("your answer is wrong")
                print("you loose the game")
                break
        else:
            print("nothing")
        amount=amount+1000
        i=i+1
        n=n+1
        m=m+1
kbc((["1.how many continaines are there","2.what is the capital of india","3.who is the miss navgurukul"]),
([["1.one","2.seven","4.eight","5.five"],["1.aagra","2.punjab","3.mumbai","4delhi"],["1.priya","2.riya","3.nikita","4.teena"]]),([2,4,3]),
(["5.five","2.seven","2.punjab","4.delhi","1.priya","3.nikita"]))