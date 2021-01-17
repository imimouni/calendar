from datetime import datetime


class Event:
    def _minutes_position(self, minutes: int) -> int:
        min = 0
        max = 15
        for i in range(1, 5):
            if min <= minutes < max:
                return i
            min = max
            max += 15

    def _get_position(self, time: datetime) -> int:
        return time.hour * 4 + self._minutes_position(time.minute) + 5

    def _set_grid_position(self) -> None:
        start = self._get_position(self.start_time)
        end = self._get_position(self.end_time)
        self.grid_position = f'{start} / {end}'

    def _set_total_time(self):
        self.total_time = self.start_time.strftime("%H:%M") + ' - ' + self.end_time.strftime("%H:%M")

    def __init__(self, id: int, color: str, content: str, start_datetime: str, end_datetime: str) -> None:
        self.id = id
        self.color = color
        self.content = content
        self.start_time = datetime.strptime(start_datetime, "%d/%m/%Y %H:%M")
        self.end_time = datetime.strptime(end_datetime, "%d/%m/%Y %H:%M")
        self._set_total_time()
        self._set_grid_position()


