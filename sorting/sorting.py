# insertion sorting
def insertion_sort(arr):
    # 1~len(arr)까지 반복
    for i in range(1, len(arr)):
        key = arr[i]  # 현재 원소를 key에 저장

        # 정렬되어있는 배열에서 key값과 비교 후 보다 큰 원소들을 한 칸씩 오른쪽으로 이동
        j = i - 1 
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # key값보다 큰 원소를 오른쪽으로 이동
            j -= 1
        # key값을 정렬된 위치에 삽입
        arr[j + 1] = key
    return arr

# merge sorting
# merge sort 함수
def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        # 배열을 반으로 나누어 merge_sort 함수에 넣어 정렬
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)

        # 정렬된 배열을 merge 함수에 넣어 합치기
        merge(arr, p, q, r)


# merge 함수
def merge(arr, p, q, r):
    # 배열을 두 부분으로 나누기
    n1 = q - p + 1
    n2 = r - q
    # 임시 배열 생성
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    # 임시 배열 L[]과 R[]에 데이터를 복사
    for i in range(n1):
        L[i] = arr[p + i]
    for j in range(n2):
        R[j] = arr[q + 1 + j]
    
    # 각 배열의 끝을 표시하기 위한 센티넬 값
    L[n1] = float('inf')
    R[n2] = float('inf')
    
    i = 0
    j = 0
    
    # 임시 배열을 arr[p..r]에 병합
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
    
    
# Combining insertion sort and merge sort
# 병합정렬 따르다가 k=5를 기준으로 삽입정렬을 수행
# 삽입정렬 최악의 복잡도를 피하기 위해 k=5로 설정
def merge_insertion_sort(arr, k=5):
    if len(arr) <= k:
        return insertion_sort(arr)
    else:
        merge_sort(arr, 0, len(arr) - 1)
    return arr
    
    
# 입력을 읽고 출력을 쓰는 메인 함수
def main():
    # 'input.txt'에서 입력을 읽음
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())  # 배열의 길이를 읽음
        arr = list(map(int, f.readline().strip().split()))  # 배열 요소를 읽음
    
    # 삽입 정렬 적용
    insertion_sorted = arr[:]
    insertion_sort(insertion_sorted)
    print("insertion sorting done")
    
    # 병합 정렬 적용
    merge_sorted = arr[:]
    merge_sort(merge_sorted, 0, len(merge_sorted) - 1)
    print("merge sorting done")
    
    # 병합-삽입 정렬 적용
    merge_insertion_sorted = arr[:]
    merge_insertion_sort(merge_insertion_sorted)
    print("merge-insertion sorting done")
    
    # 결과를 'output.txt'에 씁니다.
    with open('output.txt', 'w') as f:
        f.write(" ".join(map(str, insertion_sorted)) + "\n")
        f.write(" ".join(map(str, merge_sorted)) + "\n")
        f.write(" ".join(map(str, merge_insertion_sorted)) + "\n")
    
# main 함수 호출
if __name__ == "__main__":
    main()