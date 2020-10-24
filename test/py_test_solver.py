import pytest


@pytest.fixture(params=[
    pytest.param(
        (1, 10, -24), (2, -12),
        id='function_solved_another_equation_right_and_return_max_first',
    ),
    pytest.param(
        (1, 3, 2), (-1, -2),
        id='another_equation',
    ),
    pytest.param(
        (3, -18, 27), (3, None),
        id='d_equals_zero',
    ),
    pytest.param(
        (5, 0, 0), (0, None),
        id='simple_square_equation',
    ),
    pytest.param(
        (0, 10, 20), (-2, None),
        id='a_is_zero',
    ),
])
def solver_test_cases(request):
    return request.params


@pytest.mark.parametrize('input_data, expected_data', [
    pytest.param(
        (1, 10, -24), (2, -12),
        id='function_solved_another_equation_right_and_return_max_first',
    ),
    pytest.param(
        (1, 3, 2), (-1, -2),
        id='another_equation',
    ),
    pytest.param(
        (3, -18, 27), (3, None),
        id='d_equals_zero',
    ),
    pytest.param(
        (5, 0, 0), (0, None),
        id='simple_square_equation',
    ),
    pytest.param(
        (0, 10, 20), (-2, None),
        id='a_is_zero',
    ),
]
)
def test_solver_with_some_data(input_data, expected_data):
    from solver import square_equation_solver
    result = square_equation_solver(*input_data)
    assert result == expected_data


@pytest.fixture(scope='module')
def solver_input_data():
    print('call solver_input_data...')
    return 1, -70, 600


@pytest.fixture
def solver_input_data_with_result(solver_input_data):
    print('call solver_input_data_with_result...')
    return solver_input_data, (60, 10)


def test_raises_on_invalid_arg_type():
    from solver import square_equation_solver
    with pytest.raises(TypeError):
        square_equation_solver('1', [-70], None)


def test_solver_module_exists():
    try:
        import solver
    except ModuleNotFoundError:
        pytest.fail('Module solver not found!')


def test_function_accepts_args(solver_input_data):
    from solver import square_equation_solver
    try:
        square_equation_solver(*solver_input_data)
    except TypeError:
        pytest.fail('Function must takes 3 args')


def test_solver_function_exists():
    import solver
    assert hasattr(solver, 'square_equation_solver')


def test_a_and_b_are_zero():
    from solver import square_equation_solver
    result = square_equation_solver(0, 0, 20)
    assert result == (None, None)


def test_function_return_tuple_with_two_elements(solver_input_data):
    from solver import square_equation_solver
    result = square_equation_solver(*solver_input_data)
    assert len(result) == 2


def test_func_solved_equation_right(solver_input_data_with_result):
    from solver import square_equation_solver
    result = square_equation_solver(*solver_input_data_with_result[0])
    assert result == solver_input_data_with_result[1]


def test_func_returns_tuple():
    from solver import square_equation_solver
    result = square_equation_solver(1, -70, 600)
    assert isinstance(result, tuple)


