
"""Simplified fixed-rate bond pricing."""

from math import isfinite


def price_fixed_rate_bond(
    face_value: float,
    coupon_rate: float,
    annual_yield: float,
    frequency: int,
    periods: int,
) -> float:
    """
    Calculate the present value of a fixed-rate bond.

    Assumptions:
    - Equal coupon periods.
    - Nominal annual yield compounded at coupon frequency.
    - Valuation on a coupon-period boundary.
    - No accrued interest or settlement-date adjustment.
    """

    if not isfinite(face_value) or face_value <= 0:
        raise ValueError("Face value must be finite and positive.")

    if not isfinite(coupon_rate) or coupon_rate < 0:
        raise ValueError("Coupon rate must be finite and non-negative.")

    if not isfinite(annual_yield):
        raise ValueError("Annual yield must be finite.")

    if not isinstance(frequency, int) or isinstance(frequency, bool):
        raise ValueError("Frequency must be an integer.")

    if frequency <= 0:
        raise ValueError("Frequency must be positive.")

    if not isinstance(periods, int) or isinstance(periods, bool):
        raise ValueError("Periods must be an integer.")

    if periods <= 0:
        raise ValueError("Periods must be positive.")

    periodic_rate = annual_yield / frequency

    if periodic_rate <= -1:
        raise ValueError("Periodic yield must be greater than -100%.")

    coupon = face_value * coupon_rate / frequency

    price = 0.0

    for period in range(1, periods + 1):
        discount_factor = (1 + periodic_rate) ** period
        price += coupon / discount_factor

    redemption_value = face_value / (
        (1 + periodic_rate) ** periods
    )

    price += redemption_value

    return price
