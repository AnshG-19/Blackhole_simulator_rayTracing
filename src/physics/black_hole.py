
"""Basic Schwarzschild black hole calculations."""

# Physical constants in SI units
G = 6.67430e-11
C = 299792458.0
SOLAR_MASS_KG = 1.98847e30


def _validate_mass(mass_kg):
    """Reject zero or negative black hole masses."""
    if mass_kg <= 0:
        raise ValueError("Black hole mass must be positive.")


def schwarzschild_radius(mass_kg):
    """Calculate the event horizon radius in metres."""
    _validate_mass(mass_kg)
    return 2 * G * mass_kg / C**2


def photon_sphere_radius(mass_kg):
    """Calculate the photon sphere radius in metres."""
    _validate_mass(mass_kg)
    return 3 * G * mass_kg / C**2


def critical_impact_parameter(mass_kg):
    """Calculate the critical impact parameter in metres."""
    _validate_mass(mass_kg)
    return 3 * (3**0.5) * G * mass_kg / C**2
