circ = 24901
deg_const = circ / 360.0

def calc_dim(zoom):
    dim = circ
    for i in range(zoom):
        dim /= 2
    return dim

def calc_zoom(dim):
    zoom = -1
    while dim < circ:
        dim *= 2
        zoom += 1
    return zoom

def calc_all(dim, lat, lon):
    zoom = calc_zoom(dim)
    dim = calc_dim(zoom)
    lat = 90 - lat #NS
    y = (lat*deg_const) / dim
    lon += 180 #EW
    x = (lon*deg_const) / dim
    return (zoom, x, y)
