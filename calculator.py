class StatefulCalculator:
    def __init__(self):
        self.state = 0

    def add(self, x, y=None):
        if y:
            self.state = x + y
        else:
            self.state += x

        return self.state
