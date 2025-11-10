# Create Python Unit Test

Create comprehensive unit tests for Python code following these guidelines.

**Note**: All Python code should follow the general Python coding standards
defined in `@.cursor/rules/python.mdc`, including type hints, Pydantic models,
and abstract protocols.

## Framework

- Use `pytest` as the testing framework
- Use `pytest` fixtures for setup and teardown
- Use `pytest.mark` for test categorization when appropriate

## File Structure

- Test files MUST mirror the exact folder structure of source files
- Place tests in a `tests/` directory with identical subdirectory structure
- Name test files as `test_<module_name>.py`
- Examples:
  - `src/utils/parser.py` → `tests/utils/test_parser.py`
  - `src/api/handlers/user.py` → `tests/api/handlers/test_user.py`
- Create a `conftest.py` file per directory containing fixtures for that
  directory's tests
- Fixtures can be shared across subdirectories via parent `conftest.py` files

## Test Structure

1. **Imports**: Include all necessary imports at the top

   - Import the functions being tested
   - Import pytest and any necessary fixtures

1. **Fixtures**: ALL test data and setup goes in fixtures in `conftest.py`

1. **Test Functions**: Name tests descriptively using pattern
   `test_<function>_<scenario>_<expected_result>`

1. **Arrange-Act-Assert**: Structure each test with clear sections:

   - **Arrange**: ALL setup happens in fixtures - test receives ready data
   - **Act**: Execute the function being tested
   - **Assert**: Verify the expected outcomes

## Coverage Guidelines

Create tests covering:

- **Happy path**: Normal, expected inputs and behavior
- **Edge cases**: Boundary values, empty inputs, maximum values
- **Error cases**: Invalid inputs, exceptions, error handling with specific
  messages

## Best Practices & Additional Considerations

- Write standalone test functions - avoid classes for tests
- Each test should test one specific behavior
- Do NOT test third-party code - only test YOUR logic and business rules
- Avoid testing that third-party libraries work (e.g., don't test that
  `BaseModel` can be instantiated or that Pydantic validation works)
- Only write tests that execute your code's logic and can assert against
  expected results
- Keep tests independent - no shared state between tests
- Do NOT use mocks or patches - create functional Fakes/Stubs instead
- Prefer `pytest.fixture(params=...)` over `@pytest.mark.parametrize`
- ALL fixtures must be in `conftest.py` files, not in test files
- Fixtures can nest other fixtures for complex initialization
- Side-effect-only fixtures should start with `_` and use
  `@pytest.mark.usefixtures`
- Use `pytest.raises` with `match` parameter for error message validation
- Always use `match` parameter in `pytest.raises` to verify error messages
- Assertions should ALWAYS be against fixtures or use snapshot testing with
  `syrupy`
- NEVER hardcode expected values in assertions - use fixtures instead
- For async tests, ALWAYS use `anyio` instead of `pytest-asyncio`
- Use `pytest.approx()` for floating-point comparisons
- Use `syrupy` for snapshot testing complex data structures or serialization
- Consider property-based testing with `hypothesis` for complex scenarios
- Ensure tests can run in isolation and in any order
- Use fixture scopes (function, module, session) appropriately for performance
- Organize `conftest.py` files hierarchically - more specific near tests,
  general at root

## When Creating Tests

1. Analyze the source code to understand its behavior
1. Identify all public functions that need testing
1. Determine the test scenarios for each function
1. Create the correct directory structure mirroring source files
1. Create all necessary fixtures in appropriate `conftest.py` files
1. Create Fake/Stub classes for external dependencies
1. Create appropriately named test file(s)
1. Generate comprehensive functional test cases
1. Use `pytest.fixture(params=...)` for testing multiple scenarios

## Examples

### Example Directory Structure

```
src/
  api/
    handlers/
      user.py

tests/
  conftest.py              # Root fixtures shared across all tests
  api/
    conftest.py            # Fixtures for api tests
    handlers/
      conftest.py          # Fixtures for handler tests
      test_user.py
```

### Example Pydantic Models (in conftest.py or separate models file)

@examples/01_pydantic_models_user_input.py

### Example conftest.py with Parameterized Fixtures

@examples/02_conftest_parameterized_fixtures.py

### Example Pydantic Models for Testing

@examples/03_pydantic_models_testing.py

### Example Fake/Stub Classes in conftest.py

@examples/04_conftest_fake_stubs.py

### Example Nested Fixtures in conftest.py

@examples/05_conftest_nested_fixtures.py

### Example Side-Effect Fixtures in conftest.py

@examples/06_conftest_side_effect_fixtures.py

### Example Test Structure

@examples/07_test_basic_structure.py

### Example Using Side-Effect Fixtures

@examples/08_test_side_effect_fixtures.py

### Example Using Fake Services

@examples/09_test_fake_services.py

### Example Using Snapshot Testing with Syrupy

@examples/10_test_snapshot_syrupy.py

### Example Async Testing with Anyio

Pydantic models for async testing (in `conftest.py` or models file):

@examples/11_pydantic_models_async.py

Expected value fixtures would be in `conftest.py`:

@examples/12_conftest_async_fixtures.py

Test file using `anyio`:

@examples/13_test_async_anyio.py

### Example Using TypedDict (when Pydantic is not suitable)

@examples/14_typeddict_example.py
