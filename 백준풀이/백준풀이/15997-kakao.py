import sys

def dfs(cnt,scoreDic, P):
    if cnt == 6:#�����ϴºκ�
        sortDic = sorted(list(scoreDic.items()), key = lambda k : k[1], reverse = True)
        if sortDic[0][1] == sortDic[1][1] == sortDic[2][1] == sortDic[3][1]: #���� 4���� �Ȱ������ 0.25, 0.25, 0.25. 0.25 4����
            ansDic[sortDic[0][0]] += P*1/2
            ansDic[sortDic[1][0]] += P*1/2
            ansDic[sortDic[2][0]] += P*1/2
            ansDic[sortDic[3][0]] += P*1/2
            return

        
        elif sortDic[0][1] > sortDic[1][1] == sortDic[2][1] == sortDic[3][1] :#2 3 4 ���� �Ȱ��� ���� 3����
            ansDic[sortDic[0][0]] += P
            ansDic[sortDic[1][0]] += P*1/3
            ansDic[sortDic[2][0]] += P*1/3
            ansDic[sortDic[3][0]] += P*1/3
            return

        #elif sortDic[0][1] == sortDic[1][1] == sortDic[2][1] > sortDic[3][1] :#���� 3���� �Ȱ��� ��� 0.3333,0.3333,0.3333, 0 3����
        elif sortDic[0][1] == sortDic[1][1] == sortDic[2][1] :#���� 3���� �Ȱ��� ��� 0.3333,0.3333,0.3333, 0 3����
            ansDic[sortDic[0][0]] += P*(2/3)
            ansDic[sortDic[1][0]] += P*(2/3)
            ansDic[sortDic[2][0]] += P*(2/3)
            ansDic[sortDic[3][0]] += P*0.0
            return

        #elif sortDic[0][1] > sortDic[1][1] == sortDic[2][1] > sortDic[3][1]:#2�� 3���� �Ȱ��� ��� 1, 0.5, 0.5, 0 2����

        elif sortDic[0][1] > sortDic[1][1] == sortDic[2][1] :#2�� 3���� �Ȱ��� ��� 1, 0.5, 0.5, 0 2����
            ansDic[sortDic[0][0]] += P
            ansDic[sortDic[1][0]] += P*0.5
            ansDic[sortDic[2][0]] += P*0.5
            ansDic[sortDic[3][0]] += P*0.0
            return

        else: #�� �ܴ� 1, 1, 0 ,0  
            # 1=2,3,4 / 1,2,3=4/ 1,2,3,4
            ansDic[sortDic[0][0]] += P
            ansDic[sortDic[1][0]] += P
            ansDic[sortDic[2][0]] += P*0.0
            ansDic[sortDic[3][0]] += P*0.0
            return

    
    #A�� �̱� ��
    scoreDic[stringList[cnt][0]] += 3 #A    

    dfs(cnt+1, scoreDic, P*float(stringList[cnt][2]))#dfs �Ķ���Ϳ� scoreDic�� ���� ������ ����� ����!!
    
    scoreDic[stringList[cnt][0]] -= 3 #A

    #��涧
    scoreDic[stringList[cnt][0]] += 1 #A
    scoreDic[stringList[cnt][1]] += 1 #B

    dfs(cnt+1,scoreDic, P*float(stringList[cnt][3]))
    
    scoreDic[stringList[cnt][0]] -= 1 #A
    scoreDic[stringList[cnt][1]] -= 1 #B

    #A�� �� ��
    scoreDic[stringList[cnt][1]] += 3 #B

    dfs(cnt+1,scoreDic, P*float(stringList[cnt][4]))
    
    scoreDic[stringList[cnt][1]] -= 3 #B


if __name__ == "__main__":
    name1, name2, name3, name4 = map(str,input().split())
    #�����̸� �Է¹ޱ�
    stringList = list()

    for i in range(6):
        string = list(map(str,input().split()))
        stringList.append(string)


    scoreDic = {name1:0,name2:0,name3:0,name4:0} 
    ansDic = {name1:0.0,name2:0.0,name3:0.0,name4:0.0} #�������� Ȯ�� ������ ����Ʈ

    dfs(0, scoreDic, 1)

    for key in scoreDic:
        print(ansDic[key])