# Copilot Instructions for CodeWars Repository

This repository contains coding exercises, organized by difficulty and topic. AI coding agents should follow these guidelines to be productive:

## Project Structure
- Exercises are grouped by difficulty (e.g., `7th_lvl_Kata/`) and topic (e.g., `Credit Card Masking/`).
- Each exercise folder typically contains a single Python file implementing the solution (e.g., `CCMask.py`).
- The root `README.md` provides a minimal description; most context is in the folder/file names and code itself.

## Coding Patterns
- Solutions are written in Python, using simple functions and direct input/output.
- Example: `CCMask.py` implements a `maskify` function to mask credit card numbers, with input taken via `input()`.
- Return values are used for function outputs; print statements may be used for user interaction.
- No external dependencies or frameworks are used; keep solutions self-contained.

## Developer Workflows
- There are no build or test scripts; run Python files directly for manual testing:
  - Example: `python "7th_lvl_Kata/Credit Card Masking/CCMask.py"`
- Debug by adding print statements or using Python's built-in debugging tools.
- No automated test suites or CI/CD integrations are present.

## Conventions
- File and folder names reflect the exercise topic and difficulty.
- Keep code readable and concise; avoid unnecessary complexity.
- Do not introduce external libraries unless explicitly required by the exercise.
- Each exercise should be independent; avoid cross-file dependencies.

## Examples
- To add a new exercise, create a folder under the appropriate difficulty, then add a Python file with the solution.
- Follow the pattern in `CCMask.py` for function definition and input handling.

## Key Files
- `7th_lvl_Kata/Credit Card Masking/CCMask.py`: Example of a typical exercise solution.
- `README.md`: High-level description of the repository purpose.

---
If any conventions or workflows are unclear, please request clarification or examples from the user.
