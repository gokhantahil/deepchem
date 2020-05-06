"""This module adds utilities for coordinate boxes"""


def merge_boxes(box1, box2):
  """Merges two boxes.

  Parameters
  ----------
  box1: CoordinateBox
    First box to merge
  box2: CoordinateBox
    Second box to merge

  Returns
  -------
  Smallest `CoordinateBox` that contains both `box1` and `box2`
  """
  x_min = min(box1.x_range[0], box2.x_range[0])
  y_min = min(box1.y_range[0], box2.y_range[0])
  z_min = min(box1.z_range[0], box2.z_range[0])
  x_max = max(box1.x_range[1], box2.x_range[1])
  y_max = max(box1.y_range[1], box2.y_range[1])
  z_max = max(box1.z_range[1], box2.z_range[1])
  return CoordinateBox((x_min, x_max), (y_min, y_max), (z_min, z_max))

class CoordinateBox(object):
  """A coordinate box that represents a block in space.

  Molecular complexes are typically represented with atoms as
  coordinate points. Each complex is naturally associated with a
  number of different box regions. For example, the bounding box is a
  box that contains all atoms in the molecular complex. A binding
  pocket box is a box that focuses in on a binding region of a protein
  to a ligand. A interface box is the region in which two proteins
  have a bulk interaction.

  The `CoordinateBox` class is designed to represent such regions of
  space. It consists of the coordinates of the box, and the collection
  of atoms that live in this box alongside their coordinates.
  """

  def __init__(self, x_range, y_range, z_range):
    """Initialize this box.

    Parameters
    ----------
    x_range: tuple
      A tuple of `(x_min, x_max)` with max and min x-coordinates.
    y_range: tuple
      A tuple of `(y_min, y_max)` with max and min y-coordinates.
    z_range: tuple
      A tuple of `(z_min, z_max)` with max and min z-coordinates.
    """
    self.x_range = x_range
    self.y_range = y_range
    self.z_range = z_range

