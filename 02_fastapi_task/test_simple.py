# 제품 코드
def add(a: int, b: int) -> int:
    return a + b


# 테스트 코드
def test_add() -> None:
    # Given: 무엇인가 주어졌을때
    a, b = 1, 1
    # 버그는 "경계"를 좋아합니다
    # int 의 경우에는 -1, 0, 1 로 작동하는지 확인
    # When: 테스트 대상이 되는 함수를 호출합니다.
    result = add(a, b)  # result의 타입은 int
    # Then:
    assert result == 2
    if not result == 2:
        raise AssertionError
