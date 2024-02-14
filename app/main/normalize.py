

def normalize_integer_sum(numbers, target_sum):
    total = sum(numbers)

    # 전체 합이 0이거나 음수인 경우 빈 리스트 반환
    if total <= 0:
        return [0] * len(numbers)

    # 각 요소를 전체 합으로 나누어 정규화한 후 목표 합으로 확대
    scaled = [x / total * target_sum for x in numbers]
    # 확대된 값을 정수로 반올림
    rounded = [round(x) for x in scaled]

    # 반올림 후의 합이 목표 합과 다를 경우 조정
    while sum(rounded) != target_sum:
        difference = target_sum - sum(rounded)
        indices = range(len(numbers))

        # 오차가 가장 큰 요소의 인덱스 찾기
        if difference > 0:
            index = max(indices, key=lambda i: abs(scaled[i] - rounded[i]))
        else:
            # 값을 감소시켜야 할 때는 0보다 큰 요소 중에서 선택
            indices = [i for i in indices if rounded[i] > 0]
            index = min(indices, key=lambda i: abs(scaled[i] - rounded[i]))

        # 해당 요소의 값을 조정
        rounded[index] += 1 if difference > 0 else -1
    
    return rounded

