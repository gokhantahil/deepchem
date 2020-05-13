"""
Test Coordinate Boxes.
"""
import unittest
from deepchem.utils import coordinate_box_utils as box_utils

class TestCoordinateBoxUtils(unittest.TestCase):

  def test_make_box(self):
    x_range = (-10, 10)
    y_range = (-20, 20)
    z_range = (-30, 30)
    box = box_utils.CoordinateBox(x_range, y_range, z_range)
    assert box.x_range == x_range
    assert box.y_range == y_range
    assert box.z_range == z_range

  def test_merge_box(self):
    x_range = (-10, 10)
    y_range = (-20, 20)
    z_range = (-30, 30)
    box = box_utils.CoordinateBox(x_range, y_range, z_range)

    x_range = (-1, 1)
    y_range = (-2, 2)
    z_range = (-3, 3)
    interior_box = box_utils.CoordinateBox(x_range, y_range, z_range)

    merged_box = box_utils.merge_boxes(box, interior_box)
    assert merged_box.x_range == box.x_range
    assert merged_box.y_range == box.y_range
    assert merged_box.z_range == box.z_range

    x_range = (-10, 10)
    y_range = (-20, 20)
    z_range = (-30, 30)
    box1 = box_utils.CoordinateBox(x_range, y_range, z_range)

    x_range = (-11, 9)
    y_range = (-20, 20)
    z_range = (-30, 30)
    box2 = box_utils.CoordinateBox(x_range, y_range, z_range)

    merged_box = box_utils.merge_boxes(box1, box2)
    assert merged_box.x_range == (-11, 10)
    assert merged_box.y_range == (-20, 20)
    assert merged_box.z_range == (-30, 30)

