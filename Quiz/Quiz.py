import json
with open("quiz.json") as file:
    json1=json.load(file)
    j=json1['quiz']
    choose=int(input('Choose [1]:-Sport or [2]:-Math\n'))
    if choose==1 :
        sport=j.get('sport')
        print('question 1 is:-')
        q1=sport.get('q1')
        print(q1.get('question'))
        options=q1.get('options')
        ans1=q1.get('answer')
        for i in range(0,4):
            print(i,':-',options[i])
        ans=int(input())
        if ans==3:
            print('Congratulations your answer is right')
        else:
            print('Sorry,Your answer is wrong right ans is',ans1) 
    
    if choose==2 :
        math=j.get('maths')
        li=['q1','q2']
        for i in range(0,2):
            q1=math.get(li[i])
            print('question',i,'is:-')
            options=q1.get('options')
            ans1=q1.get('answer')
            print(q1.get('question'))
            for i in range(0,4):
                print(options[i])
            print('Write ans:-',end = ' ')
            ans=input()
            if ans1==ans:
                print('Congutunation your answer is right')
            else:
                print('Sorry,Your answer is wrong ans is',ans1)
