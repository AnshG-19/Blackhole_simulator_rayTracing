import unittest
import numpy as np

from src.physics.ray_tracing import (
    closest_approach_radius,
    calculate_light_ray,
)


class TestRayTracing(unittest.TestCase):

    def test_closest_approach_is_outside_photon_sphere(self):
        radius = closest_approach_radius(1.0, 8.0)
        self.assertGreater(radius, 3.0)
        self.assertAlmostEqual(radius, 6.701, places=2)

    def test_critical_impact_parameter(self):
        ray = calculate_light_ray(
            mass_parameter=1.0,
            impact_parameter=8.0,
            points=150,
        )
        self.assertAlmostEqual(
            ray["critical_impact_parameter"],
            3 * np.sqrt(3),
            places=6,
        )

    def test_trajectory_values_are_finite(self):
        ray = calculate_light_ray(
            mass_parameter=1.0,
            impact_parameter=8.0,
            points=150,
        )
        self.assertTrue(np.all(np.isfinite(ray["x"])))
        self.assertTrue(np.all(np.isfinite(ray["y"])))
        self.assertGreater(len(ray["x"]), 2)

    def test_subcritical_impact_parameter_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_light_ray(
                mass_parameter=1.0,
                impact_parameter=5.0,
            )


if __name__ == "__main__":
    unittest.main()
