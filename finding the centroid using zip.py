#Code Author: Pradeepa Harini B
def centroid_zip(*points):
    max_len = max(map(len, points))
    padded = [p + [0] * (max_len - len(p)) for p in points]
    return [sum(x) / len(points) for x in zip(*padded)]

centroid_zip([1], [2, 3], [4, 5, 6])
