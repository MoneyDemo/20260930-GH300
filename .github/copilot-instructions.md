# Repository guidance

## Environment and commands

- Python requires 3.10 or newer. Dependencies and the virtual environment are managed with `uv`; keep `pyproject.toml` and `uv.lock` in sync.
- Install/sync development dependencies:

  ```powershell
  uv sync --dev
  ```

- Run the interactive BMI console:

  ```powershell
  uv run python app.py
  ```

- Run the full test suite:

  ```powershell
  uv run pytest
  ```

- Run one test file or one test by node ID:

  ```powershell
  uv run pytest -vv tests/test_calBMI.py
  uv run pytest -vv tests/test_calBMI.py::test_calBMI_returns_healthy_weight_at_18_5
  ```

- Use `uv run pytest -vv -ra --tb=long --showlocals` when detailed failure output is needed.

## Architecture

- `app.py` is the Python application and the source of truth. `calculate_bmi()` owns console input/output and delegates all domain work.
- `calculate_bmi_value(weight, height)` is the calculation boundary. It converts height from inches to meters (`height * 0.0254`) and returns `weight / height_in_meters**2`.
- `calBMI(bmi)` is the classification boundary. It accepts an already calculated BMI and returns one of the exact English category strings.
- Tests mirror these two domain boundaries: `tests/test_calculate_bmi_value.py` covers conversion/calculation, while `tests/test_calBMI.py` covers category thresholds and adjacent floating-point values.
- `console.cs` is a standalone earlier/reference implementation. There is no .NET project file; do not treat it as the tested application or duplicate Python changes there unless the task explicitly asks for it.

## Repository-specific conventions

- Preserve the existing public function name `calBMI` despite its mixed-case spelling; tests and callers import it directly.
- Inputs are kilograms for weight and inches for height. Do not silently reinterpret height as meters or centimeters.
- Preserve the classification intervals and exact return strings unless requirements explicitly change:
  - `bmi < 18.5`: `"Underweight"`
  - `18.5 <= bmi < 24`: `"Healthy weight"`
  - `24 <= bmi < 27`: `"Overweight"`
  - `bmi >= 27`: `"Obesity"`
- Current edge behavior is part of the tested contract: zero weight returns a zero BMI, while zero height raises `ZeroDivisionError`. Do not add validation or convert exceptions without updating the requirements and tests.
- Tests use `pytest` with AssertPy fluent assertions. Use `is_close_to(expected, 0.01)` for rounded BMI expectations, exact assertions for category strings, and `raises(...).when_called_with(...)` for exceptions.
- Boundary tests use `math.nextafter` to exercise the nearest representable values around 18.5, 24, and 27. When changing thresholds, update exact-boundary and adjacent-value cases together.
- Existing Python docstrings and Arrange/Act/Assert comments are written in Traditional Chinese, while identifiers, prompts, and category values remain English. Follow that split in related code and tests.
