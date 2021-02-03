def BINARY_SEARCH(C, m):
# 참조 리스트의 절반을 나눈다.
    # 리스트 요소 갯수가 홀수일때 소수가 나오는 것을 대비하기 위하여,
    # 정수형으로 바꾸어 홀수가 나오도록 한다.
    # 슬라이싱을 이용하여 리스트 A와 B를 저장한다.
    A = C[0 : int(len(C) / 2)]
    B = C[int(len(C) / 2) :]
    # 참조 리스트의 어디 절반에 위치하는지 파악한다.
      # 리스트 A에 있는지, B에 있는지...
        # 만약 두 리스트 모두에 없으면, -1을 반환한다.
        # 어떤 리스트에 존재하고, 그 리스트의 요소 개수가 1이면, 그 숫자를 반환한다.
        # 어떤 리스트에 존재하고, 그 리스트의 요소 개수가 1보다 크면, 다시 이진탐색을 실시한다.
    # 그 리스트를 바탕으로 값을 찾는다.    
    if (m in A) and (len(A) == 1):
        return list_n.index(A[0]) + 1
    elif (m in B) and (len(B) == 1):
        return list_n.index(B[0]) + 1
    elif (m in A) and (len(A) > 1):
        return BINARY_SEARCH(A, m)
    elif (m in B) and (len(B) > 1):
        return BINARY_SEARCH(B, m)
    else:
        return -1

def SEARCH_PLATFORM(list_n, list_m): #list_m의 요소값을 모두 검색하여 리스트로 반환
    return [BINARY_SEARCH(list_n, m) for m in list_m]

n = 5
m = 6
list_n = [10, 20, 30, 40, 50] # 검색 키 리스트
list_m = [40, 10, 35, 15, 40, 20] # 검색 리스트

list_answer = SEARCH_PLATFORM(list_n, list_m) 
for a in list_answer:
    print(f"{a}", end = ' ') # 리스트 요소 한 줄로 출력