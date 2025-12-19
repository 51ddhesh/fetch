# Fetch 

- Fetch sample tests for problems from Codeforces.

## Setup

1. Create a `venv` in the `competitive programming home` directory. The name of the `venv` is hardcoded as `.venv` in `fetch.py`.
```sh
python3 -m venv .venv

# or with uv
uv venv
```
2. Activate the `venv`
```sh
source .venv/bin/activate
```

3. Install the required Python packages
```sh
pip install -r requirements.txt
# or with uv
uv pip install -r requirements.txt
```

4. Set alias in `~/.bashrc`
```sh
alias cfetch="<address of fetch_tests.sh>"
```

## Usage
- Fetch test cases to in.txt and expected.txt
```sh
cfetch -cf -[c|p] <contest_id> <problem>
```

Example: Fetch the sample tests from the problem A of contest 1000. [https://codeforces.com/problemset/problem/1000/A]
```sh
cfetch -cf -c 1000 A
```

