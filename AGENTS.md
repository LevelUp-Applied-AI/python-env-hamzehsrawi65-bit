# AGENTS.md

## Testing Requirements
All changes must pass `python test_environment.py` before committing.

Any Python code added to `src/` must be tested locally.
If tests are added under `tests/`, they must pass before pushing.

## Secrets Policy
Do not include API keys, passwords, personal data, or raw dataset contents in prompts.

Never commit `.env`, `*.key`, `*.pem`, or raw data files such as `.csv`, `.parquet`, or `.xlsx`.

## Scope Boundaries
Agents may edit files in `src/`, `notebooks/`, `docs/`, and project documentation files.

Do not modify `requirements.txt` without confirming dependency changes are necessary.
Do not modify `setup.sh` without running it locally afterward.
Do not change `.gitignore` without checking that source files are still tracked correctly.

## Reproducibility Standard
All AI-assisted changes must be verified locally before commit or push.

A change is only considered done when a teammate can clone the repository, install dependencies, run `python test_environment.py`, and continue work without extra clarification.