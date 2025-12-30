my_int: int = 123  # inference

my_list: list[str] = ["abc", "def"]

# mutable<생성 후에 변할 수 있다>, immutable<생성후에 변할수 없다>
my_tuple: tuple[str, str] = ("str", "str")

# 길이를 모르는 경우에 이렇게
my_tuple2: tuple[str, ...] = ("str", "str", "str")

my_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3}

or_type_list: list[int] = [False, False, 123, False]

or_type_list2: list[str | bool] = ["abc", True]
