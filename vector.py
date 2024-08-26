import math

class vector:
    @staticmethod
    def calc_ang(x1, y1, x2, y2):
        dot = x1 * x2 + y1 * y2
        det1 = math.sqrt((x1 ** 2) + (y1 ** 2))
        det2 = math.sqrt((x2 ** 2) + (y2 ** 2))
        dett = det1*det2
        res = dot/dett
        res = math.degrees(math.acos(res))
        return res


print(vector.calc_ang(2,2,0,2))