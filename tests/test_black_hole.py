
import unittest

from src.physics.black_hole import (
    SOLAR_MASS_KG,
    schwarzschild_radius,
    photon_sphere_radius,
    critical_impact_parameter,
)


class TestBlackHolePhysics(unittest.TestCase):

    def test_schwarzschild_radius_is_positive(self):
        mass = 10 * SOLAR_MASS_KG
        self.assertGreater(schwarzschild_radius(mass), 0)

    def test_photon_sphere_ratio(self):
        mass = 10 * SOLAR_MASS_KG
        rs = schwarzschild_radius(mass)
        rph = photon_sphere_radius(mass)

        self.assertAlmostEqual(rph / rs, 1.5)

    def test_critical_impact_parameter_ratio(self):
        mass = 10 * SOLAR_MASS_KG
        rs = schwarzschild_radius(mass)
        bcrit = critical_impact_parameter(mass)

        self.assertAlmostEqual(bcrit / rs, 3 * (3**0.5) / 2)

    def test_zero_mass_is_rejected(self):
        with self.assertRaises(ValueError):
            schwarzschild_radius(0)


if __name__ == "__main__":
    unittest.main()
