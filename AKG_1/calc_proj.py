import math


class Pointf:
    X = 0.0
    Y = 0.0

    def __init__(self, x, y):
        self.X = x
        self.Y = y


class Morphing:
    start_count_figure = 6
    finish_count_figure = 3
    size = 80
    start_position = Pointf(130, 130)
    finish_position = Pointf(700, 450)

    def get_coordinates_figure(self, count_figure, start_pos):
        ang = (2 * math.pi / count_figure)
        f = []
        i = 1
        while i <= count_figure:
            x = (self.size * math.cos(i * ang) - self.size * math.sin(i * ang)) + start_pos.X
            y = (self.size * math.sin(i * ang) + self.size * math.cos(i * ang)) + start_pos.Y
            f.append(Pointf(x=x, y=y))
            i += 1
        return f

    def get_coord_start_figure(self):
        data = self.get_coordinates_figure(self.start_count_figure, self.start_position)
        data.reverse()
        return data

    def get_coord_finish_figure(self):
        data = self.get_coordinates_figure(self.finish_count_figure, self.finish_position)
        #data.reverse()
        return data

    def get_current_coord(self, points_start, points_finish, current_step, steps):
        if len(points_start) > len(points_finish):
            count_max = len(points_start)
            count_min = len(points_finish)
            back = True
        else:
            count_max = len(points_finish)
            count_min = len(points_start)
            back = False
        max_count = count_max % count_min
        min_count = count_min - max_count
        min = count_max // count_min
        max = min + 1
        f = []
        counter = 0
        counter2 = 0
        for i in range(max_count):
            for j in range(max):
                if back:
                    m = counter2
                    n = counter
                else:
                    m = counter
                    n = counter2
                x = ((points_finish[m].X - points_start[n].X) / steps * current_step) + points_start[n].X
                y = ((points_finish[m].Y - points_start[n].Y) / steps * current_step) + points_start[n].Y
                f.append(Pointf(x, y))
                counter += 1
            counter2 += 1
        for i in range(min_count):
            for j in range(min):
                if back:
                    m = counter2
                    n = counter
                else:
                    m = counter
                    n = counter2
                x = ((points_finish[m].X - points_start[n].X) / steps * current_step) + points_start[n].X
                y = ((points_finish[m].Y - points_start[n].Y) / steps * current_step) + points_start[n].Y
                f.append(Pointf(x, y))
                counter += 1
            counter2 += 1
        return f
