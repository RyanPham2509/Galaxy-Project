def transform(self, x, y):
    # transform into different perspective
    # return self.transform_2D(x, y)
    return self.transform_perspective(x, y)


def transform_2D(self, x, y):
    # transform the grid back to 2D for debugging
    return int(x), int(y)


def transform_perspective(self, x, y):
    # turn a 2D grid into a different perspective for the game
    ln_y = self.perspective_point_y*y / self.height
    if ln_y > self.perspective_point_y:
        ln_y = self.perspective_point_y
    diff_x = x - self.perspective_point_x
    diff_y = self.perspective_point_y - ln_y
    factor_y = diff_y / self.perspective_point_y
    factor_y = factor_y**4
    tr_x = self.perspective_point_x + diff_x*factor_y
    tr_y = self.perspective_point_y - factor_y * self.perspective_point_y
    return int(tr_x), int(tr_y)
