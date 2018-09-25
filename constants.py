import numpy as np
ZERO = 0

R = np.s_[..., 0]
G = np.s_[:, :, 1]
B = np.s_[:, :, 2]

_COLORS = {"BLACK": "#000000", "WHITE": "FFFFFF",
           "RED": "#FF0000", "GREEN": "#00FF00", "BLUE": "#0000FF", }

COLORS = list(_COLORS)

locals().update(_COLORS)
