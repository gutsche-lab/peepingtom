import numpy as np
from napari.layers import Points

from peepingtom.datablocks import PointBlock
from peepingtom.depictors import PointDepictor


def test_points_depictor():
    pointblock = PointBlock(np.ones((2, 3)))
    point_depictor = PointDepictor(pointblock)
    assert point_depictor.datablock is pointblock
    assert len(point_depictor.layers) == 1
    assert isinstance(point_depictor.layers[0], Points)
