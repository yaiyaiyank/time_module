import time
import random


def randsleep(start: int | float, end: int | float):
    """sleep時間をランダムにする秒"""
    try:
        assert (isinstance(start, int) or isinstance(start, float)) and start >= 0
        assert (isinstance(end, int) or isinstance(end, float)) and end >= 0
    except AssertionError:
        raise ValueError("start, endは0以上の数でお願いします。")
    ru = random.uniform(start, end)
    time.sleep(ru)


def countdown(timer: int):
    """コンソールに表示する"""
    try:
        assert isinstance(timer, int) and timer >= 0
    except AssertionError:
        raise ValueError("timerは0以上の整数でおなしゃす。")

    for i in range(timer):
        time.sleep(1)
        print(f"あと{timer - i}秒", end="\r")
