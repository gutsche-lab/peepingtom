from seaborn import color_palette

from ...io_ import star_to_crates
from ...analysis.particles import classify_radial_distance
from .base import Peeper
from ...core import ParticleBlock, stack
from ..depictors import ParticleDepictor


class ParticlePeeper(Peeper):
    """
    Peeper class for Particles objects
    """
    def __init__(self, star_paths, **kwargs):
        crates = star_to_crates(star_paths)
        super().__init__(crates, **kwargs)
        self.stack = None

    @property
    def particles(self):
        return self._get_datablocks(ParticleBlock)

    def peep(self, viewer=None, as_stack=True, **kwargs):
        self._init_viewer(viewer)
        if as_stack:
            self.stack = stack(self.particles)
            ParticleDepictor(self.stack, peeper=self)
            self.stack.depictor.draw()
        else:
            self.depictors.draw()

    def classify_radial_distance(self, **kwargs):
        n_classes = kwargs.pop('n_classes', 5)
        class_tag = kwargs.pop('class_tag', 'class_radial')
        colors = [list(x) for x in color_palette('colorblind', n_colors=n_classes)]
        classify_radial_distance(self.particles, n_classes=n_classes, class_tag=class_tag, **kwargs)
        for d in self.depictors:
            d.point_layer.face_color = class_tag
            d.point_layer.face_color_cycle = colors