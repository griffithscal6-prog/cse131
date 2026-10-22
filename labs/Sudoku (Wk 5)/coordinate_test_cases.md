# Sudoku Coordinate-Parsing Test Cases

**Function under test:** `get_cell_coordinates(coordinate)`

**Expected behavior:** The function accepts a row and column in either order (for example, `A5` or `5A`) and returns `(column_index, row_index)`. Columns `A`–`I` map to `0`–`8`, and rows `1`–`9` map to `0`–`8`. Invalid coordinates return `None`.

| Test Case Name | Input | Expected Output | Test Type |
|---|---|---|---|
| First cell, letter then number | `A1` | `(0, 0)` | Boundary condition |
| Last cell, letter then number | `I9` | `(8, 8)` | Boundary condition |
| Typical coordinate, letter then number | `A5` | `(0, 4)` | Requirement |
| Typical coordinate, number then letter | `5A` | `(0, 4)` | Requirement |
| Middle coordinate, letter then number | `E3` | `(4, 2)` | Requirement |
| Middle coordinate, number then letter | `3E` | `(4, 2)` | Requirement |
| Lowercase coordinate | `a5` | `(0, 4)` | Requirement |
| Lowercase coordinate, number first | `5i` | `(8, 4)` | Requirement |
| Row number zero | `A0` | `None` | Error state |
| Row number zero, number first | `0A` | `None` | Error state |
| Column letter before A | `@5` | `None` | Error state |
| Column letter after I | `J5` | `None` | Error state |
| Two letters | `AA` | `None` | Error state |
| Two numbers | `55` | `None` | Error state |
| Coordinate too long | `A10` | `None` | Error state |
| Coordinate too short | `A` | `None` | Error state |
| Empty input | `""` | `None` | Error state |

## Notes

- The function returns `(column, row)`, not `(row, column)`. For example, `A5` returns `(0, 4)`.
- The function calls `.upper()`, so lowercase letters should work.
- The function does not remove spaces itself. The current `enter_number()` function uses `.strip()` before calling it, so a direct call such as `get_cell_coordinates(" A5")` returns `None`. If whitespace handling is meant to be part of the coordinate parser's requirements, add `coordinate = coordinate.strip().upper()` in the function and test that behavior separately.
- These are documented test cases. They can be used manually or turned into automated tests later.
