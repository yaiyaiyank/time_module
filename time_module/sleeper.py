from dataclasses import dataclass
import time
import random


def randsleep(start: int | float, end: int | float):
    """startからendの範囲のランダムな値でsleep"""
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


@dataclass
class WaitTry:
    """
    フラグが立つまで待機
    Args:
        sec (int | float): 待機中の更新間隔
        count (int): 更新回数
    Usage:
        wait_try = WaitTry()
        wait_try.decide_count(10) # 10秒待機

        for _ in range(wait_try.count) # ここyeildでrangeいらなそう
            # フラグが立ったら抜ける
            if is_flag():
                break
            wait_try.sleep() # ここyeildで更に省略できそう

    """

    # TODO yeildでrangeせずにfor文回せるかも。後でやってみる

    sec: int | float = 0.1
    count: int = None  #

    def __post_init__(self):
        if not isinstance(self.sec, int | float):
            raise TypeError
        if self.sec <= 0:
            raise ValueError
        if not self.count is None:
            raise TypeError

    def decide_count(self, wait_time: int | float):
        self.count = int(wait_time / self.sec)
        # 最低1回
        if self.count <= 0:
            self.count = 1

    def sleep(self):
        time.sleep(self.sec)
