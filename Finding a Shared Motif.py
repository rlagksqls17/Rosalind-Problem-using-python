# LCS.py
# 최장 공통부분 문자열(LCS, long common substring) 분석법  
# 분석할 문자열의 길이가 모두 같을 때만 이용

def clear_rosalind(link): # 데이터 정제
    f = open(link,'r') # 정해진 경로에 저장된 파일을 연 뒤 
    f.readline() # 한 줄을 건너 뜀, sample.txt 파일 형식 참고
    lines = f.readlines() # 이후의 모든 데이터를 저장 
    Seq = [] # 정제된 데이터 저장소 리스트
    temp = [] # 임시 저장소 리스트
    for line in lines: # 한 줄씩 읽어서 
        if '>' in line: # '>' 표기가 있는 줄이 있을 경우
            Seq.append(("".join(temp)).replace('\n','')) # 여태껏 저장된 서열들을 저장하고 
            temp = [] # 임시 저장소를 초기화시킴
            continue # 아래 줄을 실행시키지 않고 다음 줄을 읽음
        temp.append(line) # '>' 표기가 없는 실제 서열들은 임시저장소에 묶어둠
    Seq.append(("".join(temp)).replace('\n','')) # 저장이 안된 마지막 줄의 정보를 저장
    f.close() # 파일 닫음
    return Seq

def long_substr(data): 
    substr = '' # 공통서열이 저장될 변수
    if len(data) > 1 and len(data[0]) > 0: # 최소한 2개 이상의 문자열이 있어야 작동함  ex) data =  ["ABCDEF", "BCDEFG"]
        for i in range(len(data[0])): # ex) data[0] == "ABCDEF" 일때, i = 0 ~ 5 의 범위를 가짐
            for j in range(len(data[0])-i+1): # ex) i = 0 >> j = 0 ~ 6,  . . . i = 5 >> j = 0 ~ 1 
                if j > len(substr) and is_substr(data[0][i:i+j], data): # ex) j = 0 ~ 6 >> data[0][0:0~6] ('A', 'AB', ...'ABCDEF'), 
                                                                        #     j = 0 ~ 5 >> data[0][1:1~6] ('B', 'BC', ...'BCDEF')
                    substr = data[0][i:i+j] # 비교된 문자열이 이전의 substring 보다 길 경우 substring은 새로 갱신됨  
    return substr

def is_substr(find, data): # 예제처럼 'A', 'AB', ... 'ABCDEF', 'B', 'BC', ... 'BCDEF', ... 'F' 글자가 다른 문자열에 있는지 비교될 것임
    if len(data) < 1 and len(find) < 1:  # 비교할 문자열이 없을 경우 False값 반환
        return False
    for i in range(len(data)): # 다른 문자열 안에 find 문자열이 있는지 확인하고 불리언 값을 반환
        if find not in data[i]:
            return False
    return True

# main

link = "/content/drive/MyDrive/workspace/finding shared motif.txt"  # 파일의 경로
seq = clear_rosalind(link)
print(long_substr(seq))
