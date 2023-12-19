# 현재=부모노드 일때 전위) 부모 왼 오 // 중위) 왼 부모 오 // 후위) 왼 오 부모
# 인덱스 1로 시작하는 형태로 변형된 답안이다.
def preorder(nodes, idx):  # 부모 - 왼 - 오 순회하기 (재귀)
    if idx < len(nodes): # idx = 현재 인덱스 위치
        result = str(nodes[idx]) + " "  # 현재 노드값 + 띄어쓰기 공백 저장
        result += preorder(nodes, idx*2) # 왼쪽 노드 재귀
        result += preorder(nodes, idx*2 + 1) # 오른쪽 노드 재귀
        return result
    else: # 길이 넘어가면 빈 문자열
        return ""

def inorder(nodes, idx): # 왼 - 부모 - 오 순회하기
    if idx < len(nodes):
        result = inorder(nodes, idx * 2) # 왼쪽 노드 재귀
        result += str(nodes[idx]) + " "  # 부모 노드
        result += inorder(nodes, idx * 2 + 1)  # 오른쪽 노드 재귀
        return result
    else:
        return ""

def postorder(nodes, idx): # 왼 - 오 - 부모
    if idx < len(nodes):
        result = postorder(nodes, idx * 2) # 왼쪽 노드 재귀
        result += postorder(nodes, idx * 2 + 1) # 오른쪽 노드 재귀
        result += str(nodes[idx]) + " " # 부모 노드
        return result
    else:
        return ""

def solution(nodes):
    nodes = [-1] + nodes # 인덱스 0자리에 아무거나 삽입
    return [preorder(nodes, 1)[:-1], inorder(nodes, 1)[:-1], postorder(nodes, 1)[:-1]]



assert solution([1,2,3,4,5,6,7]) == ["1 2 4 5 3 6 7", "4 2 5 1 6 3 7", "4 5 2 6 7 3 1"]