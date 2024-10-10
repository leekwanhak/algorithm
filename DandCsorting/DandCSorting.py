import random


# 1. Naive quick sort함수
def partition(A, p, r):
    x = A[r]  # 피벗 설정
    i = p - 1  # 작은 원소들의 끝을 가리키는 인덱스
    for j in range(p, r):  # 피벗보다 작은 원소들을 왼쪽에 모은다
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]  # 교환
    A[i + 1], A[r] = A[r], A[i + 1]  # 피벗을 올바른 위치로 이동
    return i + 1

# Quicksort 함수
def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)  # 분할 위치 구하기
        quicksort(A, p, q - 1)  # 왼쪽 부분 정렬
        quicksort(A, q + 1, r)  # 오른쪽 부분 정렬


# 2. Randomized quick sort함수
def randomized_partition(A, p, r):
    i = random.randint(p, r)  # p와 r 사이의 랜덤하게 값 선택
    A[r], A[i] = A[i], A[r]  # 마지막 원소와 피벗을 교환
    return partition(A, p, r) 

# Randomized Quick Sort 함수
def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)  # 임의로 선택한 피벗을 기준으로 분할
        randomized_quicksort(A, p, q - 1)  # 왼쪽 부분 정렬
        randomized_quicksort(A, q + 1, r)  # 오른쪽 부분 정렬


# 3. Median-of-3 quick sort함수
def median_of_three_partition(A, p, r):
    # 세 개의 임의의 값을 선택
    first = random.randint(p, r)
    second = random.randint(p, r)
    third = random.randint(p, r)

    # 세 값의 중간 값을 피벗으로 선택
    select_pivot = [first, second, third]
    select_pivot.sort(key=lambda x: A[x]) # lambda 익명함수 이용하여 정렬
    median_index = select_pivot[1]  # 중간값의 인덱스
    
    # 피벗을 마지막으로 이동
    A[r], A[median_index] = A[median_index], A[r]
    return partition(A, p, r)

# Median-of-3 quick sort함수
def median_of_three_quicksort(A, p, r):
    if p < r:
        q = median_of_three_partition(A, p, r)  # median of 3을 사용한 피벗 선택
        median_of_three_quicksort(A, p, q - 1)  # 왼쪽 부분 정렬
        median_of_three_quicksort(A, q + 1, r)  # 오른쪽 부분 정렬


# 입력을 읽고 출력을 쓰는 메인 함수
def main():
    # 'input.txt'에서 입력을 읽음
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())  # 배열의 길이를 읽음
        arr = list(map(int, f.readline().strip().split()))  # 배열 요소를 읽음
    
    # Naive quick sort 적용
    quick_sorted = arr[:]
    quicksort(quick_sorted, 0, len(quick_sorted) - 1)
    print("quick sorting done")
    
    # Randomized quick sort 적용
    randomized_quicksorted = arr[:]
    randomized_quicksort(randomized_quicksorted, 0, len(randomized_quicksorted) - 1)
    print("randomized sorting done")
    
    # Median-of-3 quick sort 적용
    median_of_three_quicksorted = arr[:]
    median_of_three_quicksort(median_of_three_quicksorted, 0, len(median_of_three_quicksorted) - 1)
    print("median_of_three quick sorting done")
    
    # 결과를 'output.txt'에 씀
    with open('output.txt', 'w') as f:
        f.write(" ".join(map(str, quick_sorted)) + "\n")
        f.write(" ".join(map(str, randomized_quicksorted)) + "\n")
        f.write(" ".join(map(str, median_of_three_quicksorted)) + "\n")
    
# main 함수 호출
if __name__ == "__main__":
    main()