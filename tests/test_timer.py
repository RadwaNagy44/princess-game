import time
from src.princess_game.timer import Timer

def test_timer_initialization():
    timer = Timer(10)
    assert timer.duration == 10
    assert timer.start_time is None

def test_timer_start():
    timer = Timer(10)
    timer.start()
    assert timer.start_time is not None

def test_time_left():
    timer = Timer(5)
    timer.start()
    time.sleep(1)
    remaining = timer.time_left()
    assert 1 <= remaining <= 5

def test_is_time_over():
    timer = Timer(2)
    timer.start()
    time.sleep(3)
    assert timer.is_time_over()
