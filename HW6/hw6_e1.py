from time import sleep


class Colors:
    RED = '\033[31m'
    YELLOW = '\033[33m'
    GREEN = '\033[32m'
    NORMAL = '\033[m'


class TrafficLight:
    _color = 'Red'

    def running(self):
        if self._color == 'Red':
            print(f"{Colors.RED}{self._color}{Colors.NORMAL}")
            sleep(7)
            self._color = 'Yellow'
        elif self._color == 'Yellow':
            print(f"{Colors.YELLOW}{self._color}{Colors.NORMAL}")
            sleep(2)
            self._color = 'Green'
        else:
            print(f"{Colors.GREEN}{self._color}{Colors.NORMAL}")
            sleep(9)
            self._color = 'Red'


lights = TrafficLight()
for i in range(12):
    lights.running()
