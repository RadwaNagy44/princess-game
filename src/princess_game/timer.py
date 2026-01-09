import time
class Timer(object):
    def __init__(self, duration=90):
        self.duration = duration
        self.start_time = None

    def start(self):
        self.start_time = time.monotonic()

    def time_left(self):
        if self.start_time is None:
            return self.duration
        elapsed = time.monotonic() - self.start_time
        remaining = self.duration - elapsed
        return max(0, remaining)
    
    def is_time_over(self):
        return self.time_left() <= 0
        
   