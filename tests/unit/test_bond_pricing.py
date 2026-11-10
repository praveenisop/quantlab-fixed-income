
import pytest

from quantlab.pricing.bond import price_fixed_rate_bond


def test_example_bond_price():
    price = price_fixed_rate_bond(
        face_value=1000,
        coupon_rate=0.05,
        annual_yield=0.04,
        frequency=2,
        periods=10,
    )

    assert price == pytest.approx(1044.91, abs=0.01)


def test_bond_prices_at_par_when_coupon_equals_yield():
    price = price_fixed_rate_bond(
        face_value=1000,
        coupon_rate=0.05,
        annual_yield=0.05,
        frequency=2,
        periods=10,
    )

    assert price == pytest.approx(1000.0)


def test_bond_price_decreases_when_yield_increases():
    low_yield_price = price_fixed_rate_bond(
        1000, 0.05, 0.03, 2, 10
    )

    high_yield_price = price_fixed_rate_bond(
        1000, 0.05, 0.06, 2, 10
    )

    assert low_yield_price > high_yield_price


def test_bond_price_increases_when_yield_decreases():
    low_yield_price = price_fixed_rate_bond(
        1000, 0.05, 0.03, 2, 10
    )

    high_yield_price = price_fixed_rate_bond(
        1000, 0.05, 0.06, 2, 10
    )

    assert low_yield_price > high_yield_price


def test_zero_coupon_bond():
    price = price_fixed_rate_bond(
        1000, 0.0, 0.04, 2, 10
    )

    expected = 1000 / (1.02 ** 10)

    assert price == pytest.approx(expected)


@pytest.mark.parametrize(
    "arguments",
    [
        (0, 0.05, 0.04, 2, 10),
        (1000, -0.01, 0.04, 2, 10),
        (1000, 0.05, 0.04, 0, 10),
        (1000, 0.05, 0.04, 2, 0),
        (1000, 0.05, -2.0, 2, 10),
    ],
)
def test_invalid_inputs(arguments):
    with pytest.raises(ValueError):
        price_fixed_rate_bond(*arguments)
