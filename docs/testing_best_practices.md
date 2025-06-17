# Best Practices for Writing Unit Tests

## 1. Test Behavior, Not Implementation

- Focus on what the code should do, not how it does it.
- Avoid testing internal details (e.g., exact function calls) unless necessary.

## 2. Mock External Dependencies

- Mock external services, APIs, or complex logic to isolate the unit under test.
- Mock at the right level (where the dependency is imported, not where it's defined).

## 3. Use Clear, Descriptive Test Names

- Name tests to describe the behavior being tested (e.g., `test_should_handle_empty_csv`).
- Follow a consistent naming convention (e.g., `test_<scenario>_<expected_outcome>`).

## 4. Follow the Arrange-Act-Assert Pattern

- **Arrange**: Set up the test data and mocks.
- **Act**: Call the function under test.
- **Assert**: Verify the expected outcomes.

## 5. Test Both Success and Error Cases

- Test happy paths (expected inputs and outputs).
- Test error cases (e.g., missing data, exceptions) to ensure robustness.

## 6. Preserve State Integrity

- Ensure the function under test preserves unrelated state fields.
- Use `state.update({...})` instead of returning a new dictionary if state preservation is required.

## 7. Validate Output Format and Content

- Assert that the output matches the expected format (e.g., type, structure, content).
- Use specific assertions (e.g., `assert result["key"] == expected_value`).

## 8. Test Edge Cases

- Test boundary conditions (e.g., empty inputs, maximum values).
- Test scenarios that might cause unexpected behavior.

## 9. Keep Tests Independent and Isolated

- Each test should be self-contained and not depend on the state or output of other tests.
- Use fixtures or `setUp`/`tearDown` methods to manage test data.

## 10. Use Integration Tests for Real-World Scenarios

- Supplement unit tests with integration tests that use real dependencies.
- Test the full flow of data through multiple components.
