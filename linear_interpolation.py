import functools


class LinearInterpolator:

    def __init__(self, val_list):
        self.val_list = val_list
        self.first = val_list[0]
        self.last = val_list[-1]
        self.num_vals = len(val_list)

    @classmethod
    def from_tuple_list(cls, val_list):
        return cls(val_list)

    @classmethod
    def from_list(cls, val_list, min_val, max_val):
        if len(val_list) == 1:
            return cls([(0, val_list[0])])
        step = (max_val - min_val)/(len(val_list)-1)
        val_list = [(i*step, val_list[i]) for i in range(len(val_list))]
        return cls(val_list)

    @functools.lru_cache(maxsize=None)
    def _segments(self, pieces):
        segment = []
        if pieces == 1:
            return [((self.first[0]+self.last[0]) * 0.5, (self.first[1]+self.last[1]) * 0.5)]
        elif pieces == 2:
            return [(self.first[0], self.first[1]), (self.last[0]/2, self.last[1])]
        else:
            interpolation_step = (self.last[0] - self.first[0]) / (pieces - 1)
            range_step = (self.last[0] - self.first[0])/pieces
            # for i in range(pieces):
            #     val = self.first[0] + interpolation_step * i
            #     segment.append((range_step*i, self.get(val)))
            # UNTESTED
            # return segment
            return [(range_step*i, self.get(self.first[0] + interpolation_step * i))
                    for i in range(pieces)]

    def get(self, val):
        if val <= self.first[0]:
            return self.first[1]

        if val >= self.last[0]:
            return self.last[1]

        for i in range(len(self.val_list)-1):
            # Tree or something like that
            if self.val_list[i][0] <= val < self.val_list[i+1][0]:
                # ratio = (val - self.val_list[i][0]) / \
                #     (self.val_list[i+1][0] -
                #      self.val_list[i][0])
                _ratio = ratio(self.val_list[i][0], self.val_list[i+1][0], val)
                return interpolate(self.val_list[i][1], self.val_list[i+1][1], _ratio)

    def get_segmented(self, val, segments=None):
        if segments is None:
            segments = self.num_vals
        segments = self._segments(segments)

        if val <= segments[0][0]:
            return segments[0][1]

        if val >= segments[-1][0]:
            return segments[-1][1]

        for i in range(len(segments)-1):
            if segments[i][0] <= val < segments[i+1][0]:
                return segments[i][1]

    def __getitem__(self, key):
        return self.get(key)


def interpolate(a, b, ratio):
    # return (1-ratio) * a + ratio * b
    return a + ratio * (b - a)


def ratio(a, b, value):
    return (value - a) / (b-a)
# if __name__ == '__main__':
#     linear_interpolator1 = LinearInterpolation.from_list([0, 4, 10], -10, 10)
#     linear_interpolator2 = LinearInterpolation.from_tuple_list(
#         [(0, -10), (4, -2), (10, 10)])

#     a1 = linear_interpolator1.get(10)
#     a2 = linear_interpolator1[10]
