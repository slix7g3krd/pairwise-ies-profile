import pytest
import math
from render import ies_profile as mod

CASES = [
    ("lum", 'm.candela_to_luminance(10, 2) == approx(5.0)'),
    ("nadir", 'm.angle_from_nadir(30) == 150'),
    ("wrap", 'm.wrap_angle(-30) == 330'),
    ("mirror", 'm.mirror_sign(-1) == -1'),
    ("rotate", 'm.rotate_angle(10, 20) == 30'),
    ("unit", 'm.unit_scale(2, 1000) == 2000'),
    ("flux", 'm.flux_norm(100, 50) == approx(2.0)'),
    ("decay", 'm.distance_decay(2) == approx(0.25)'),
    ("atlas", 'm.atlas_v(0.5, 0.25) == approx(0.75)'),
    ("cutoff", 'm.cutoff_angle(0) == 90'),
    ("intensity", 'm.intensity(10, 2) == approx(2.5)'),
    ("solid", 'm.solid_angle(90) == approx(6.2832, abs=1e-3)'),
    ("key", 'm.ies_key(3, 2) == "3:2"'),
    ("clamp", 'm.clamp_angle(-10) == 0'),
    ("ring", 'm.ring_diff(350, 10) == 20')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
