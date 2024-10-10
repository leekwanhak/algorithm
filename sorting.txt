# insertion sort
def insertion_sort(arr):
    # 1~len(arr)까지 반복
    for i in range(1, len(arr)):
        key = arr[i] # 현재 원소를 key에 저장

        # 정렬되어있는 배열에서 key값과 비교 후 보다 큰 원소들을 한 칸씩 오른쪽으로 이동
        j = i-1
        while j >=0 and arr[j] > key:
                arr[j + 1] = arr[j] # key값보다 큰 원소를 오른쪽으로 이동
                j -= 1
        # key값을 정렬된 위치에 삽입
        arr[j + 1] = key
    return arr

# merge sort 2
def merge_sort2(arr):
    # 배열의 길이가 1보다 작거나 같으면 그대로 반환
    if len(arr) <= 1:
        return arr

    # 배열을 반으로 나누기
    mid = len(arr) // 2
    # 나눈 배열을 다시 merge_sort 함수에 넣어 정렬(재귀)
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    # 정렬된 배열을 merge 함수에 넣어 합치기
    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:] #
    merged_arr += high_arr[h:]
    return merged_arr

# merge sort 1
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
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    
    # Copy data to temporary arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[p + i]
    for j in range(n2):
        R[j] = arr[q + 1 + j]

    # Sentinel values to mark the end of each array
    L[n1] = float('inf')
    R[n2] = float('inf')
    
    i = 0
    j = 0
    
    # Merge the temporary arrays back into A[p..r]
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1


# Combining insertion sort and merge sort
def sort(arr):
    # 배열의 길이가 5 이하일 때 insertion sort 사용
    if len(arr) <= 5:
        return insertion_sort(arr)
    # 그 외에는 merge sort 사용
    else:
        return merge_sort(arr)
    
# Test
def read_input(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

def write_output(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'
    
    arr = read_input(input_file)
    sorted_arr = sort(arr)
    write_output(output_file, sorted_arr)

if __name__ == "__main__":
    main()

    
