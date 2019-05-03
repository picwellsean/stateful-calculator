import pytest

from calculator import StatefulCalculator


@pytest.mark.parametrize('x', [
    -1,
    0,
    1,
    11,
    111
])
def test_add_returns_x_given_x_and_no_state(x):
    # arrange
    calculator = StatefulCalculator()

    # act
    result = calculator.add(x)

    # assert
    assert result == x


@pytest.mark.parametrize('x, state', [(1, 1)])
def test_add_returns_x_plus_state_given_x_and_state(x, state):
    # arrange
    calculator = StatefulCalculator()
    calculator.add(state)

    # act
    result = calculator.add(x)

    # assert
    assert result == x + state


@pytest.mark.parametrize('x, y', [(1, 1)])
def test_add_returns_x_plus_y_given_x_and_y_and_no_state(x, y):
    # arrange
    calculator = StatefulCalculator()

    # act
    result = calculator.add(x, y)

    # assert
    assert result == x + y


@pytest.mark.parametrize('x, y, state', [(1, 1, 1)])
def test_add_returns_x_plus_y_given_x_and_y_and_state(x, y, state):
    # arrange
    calculator = StatefulCalculator()
    calculator.add(state)

    # act
    result = calculator.add(x, y)

    # assert
    assert result == x + y
