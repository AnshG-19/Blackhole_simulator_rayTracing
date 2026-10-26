"""Light-ray trajectory calculations in Schwarzschild spacetime."""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def closest_approach_radius(mass_parameter, impact_parameter):
    """Find the closest approach radius for an escaping ray."""

    M = float(mass_parameter)
    b = float(impact_parameter)

    if M <= 0 or b <= 0:
        raise ValueError("Mass and impact parameter must be positive.")

    b_critical = 3 * np.sqrt(3) * M

    if b <= b_critical:
        raise ValueError("Impact parameter must exceed the critical value.")

    def equation(radius):
        return radius**3 - b**2 * radius + 2 * M * b**2

    return brentq(equation, 3 * M, b)


def calculate_light_ray(
    mass_parameter=1.0,
    impact_parameter=8.0,
    max_angle=4.0,
    points=1500,
):
    """Calculate an escaping light ray in geometric units."""

    M = float(mass_parameter)
    b = float(impact_parameter)

    if M <= 0:
        raise ValueError("Mass parameter must be positive.")

    if max_angle <= 0:
        raise ValueError("Maximum angle must be positive.")

    if points < 2:
        raise ValueError("Points must be at least 2.")

    b_critical = 3 * np.sqrt(3) * M
    r_min = closest_approach_radius(M, b)
    u_initial = 1.0 / r_min

    def orbit_equation(phi, state):
        u, du_dphi = state
        return [du_dphi, 3 * M * u**2 - u]

    phi_half = np.linspace(0.0, max_angle / 2.0, points // 2 + 1)

    solution = solve_ivp(
        orbit_equation,
        (0.0, max_angle / 2.0),
        [u_initial, 0.0],
        t_eval=phi_half,
        rtol=1e-9,
        atol=1e-11,
    )

    if not solution.success:
        raise RuntimeError(solution.message)

    u_half = solution.y[0]

    if np.any(u_half <= 0):
        raise RuntimeError("Invalid inverse radius encountered.")

    radius_half = 1.0 / u_half

    phi = np.concatenate((-phi_half[:0:-1], phi_half))
    radius = np.concatenate((radius_half[:0:-1], radius_half))

    x = radius * np.cos(phi)
    y = radius * np.sin(phi)

    return {
        "phi": phi,
        "radius": radius,
        "x": x,
        "y": y,
        "closest_approach": r_min,
        "critical_impact_parameter": b_critical,
    }
