```
 _ _                                                    _ _
| | | __ _ _ __ ___   __ _    ___ ___  _ __ ___  _ __ ___ (_) |_
| | |/ _` | '_ ` _ \ / _` |  / __/ _ \| '_ ` _ \| '_ ` _ \| | __|
| | | (_| | | | | | | (_| | | (_| (_) | | | | | | | | | | | | |_
|_|_|\__,_|_| |_| |_|\__,_|  \___\___/|_| |_| |_|_| |_| |_|_|\__|
```

<p align="center">
  <strong>Generate git commit messages from your diffs with a local Ollama LLM — fully offline, no API keys.</strong>
</p>

<p align="center">
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/github/license/cajias/llama-commit-msg"></a>
  <img alt="Top language" src="https://img.shields.io/github/languages/top/cajias/llama-commit-msg">
  <img alt="Last commit" src="https://img.shields.io/github/last-commit/cajias/llama-commit-msg">
  <img alt="Python" src="https://img.shields.io/badge/python-3.11-3776AB?logo=python&logoColor=white">
  <img alt="Ollama" src="https://img.shields.io/badge/Ollama-codellama%3A13b-000000?logo=ollama&logoColor=white">
  <img alt="LangChain" src="https://img.shields.io/badge/LangChain-1C3C3C?logo=langchain&logoColor=white">
</p>

---

## Overview

**llama-commit-msg** reads the changes in a local git repository, feeds each
modified file's content to a [Code Llama](https://ollama.com/library/codellama)
model running locally through [Ollama](https://ollama.com/), and prints a
generated commit message for each file. Everything runs on your machine through
[LangChain](https://www.langchain.com/) — there are no external API calls and no
keys to manage. It is a small, hackable proof of concept for LLM-assisted commit
authoring.

## ✨ Features

- **Local-first** — talks to an Ollama server on `localhost:11434`; nothing
  leaves your machine.
- **Code Llama backed** — uses the `codellama:13b` model out of the box.
- **Diff-aware prompting** — a tightly constrained system prompt asks the model
  to describe only what changed, nothing else.
- **GitPython powered** — discovers changed files directly from your working
  tree via [GitPython](https://gitpython.readthedocs.io/).
- **Conda + Makefile workflow** — reproducible environment and one-line run
  targets.

## 📦 Requirements

This project depends on services and tooling that must be present **before** you
run it:

1. **[Ollama](https://ollama.com/)** running locally and serving the model at
   `http://localhost:11434` (the URL is hard-coded in `src/gen.py`):
   ```bash
   ollama pull codellama:13b
   ollama serve
   ```
2. **[Conda](https://docs.conda.io/)** for environment management.
3. A **git repository** with uncommitted changes to describe.

## 🚀 Installation

Clone the repository and create the conda environment from `environment.yml`:

```bash
git clone https://github.com/cajias/llama-commit-msg.git
cd llama-commit-msg
make install-deps   # conda env update -f environment.yml --prune
```

## 🛠 Usage

Run the generator through the Makefile target, which executes
`src/main.py` inside the conda environment:

```bash
make run
```

Or invoke the script directly (the `-p/--path` argument is required by the
parser):

```bash
python src/main.py -p .
```

For each changed file in the repository it walks, the tool prints the file path
followed by the model's suggested commit message:

```
src/gen.py
Refactor explain_diff to constrain the system prompt to the supplied diff.
```

> [!NOTE]
> This is an early proof of concept. The walked repository is currently the
> parent directory (`repo_path = "../"` in `src/main.py`), and changes are read
> from the working tree (modified files), not the git staging area. Adjust the
> source if you need different behavior.

## 🗂 Project Structure

```
llama-commit-msg/
├── src/
│   ├── __init__.py     # Package metadata (name, version, author, license)
│   ├── main.py         # Entry point: parses args, walks diffs, prints messages
│   ├── gen.py          # LangChain + Ollama wrapper that turns a diff into prose
│   └── git_diff.py     # GitPython helper that collects modified files
├── environment.yml     # Conda environment specification
├── Makefile            # install-deps / run / build / test / clean targets
├── LICENSE             # MIT
└── README.md
```

## 🧪 Development

Common Makefile targets:

| Target              | What it does                                              |
| ------------------- | -------------------------------------------------------- |
| `make install-deps` | Update the conda env from `environment.yml`.             |
| `make run`          | Run `src/main.py` inside the conda env.                  |
| `make test`         | Discover and run unit tests via `python -m unittest`.    |
| `make build`        | Bundle a standalone binary with PyInstaller.             |
| `make clean`        | Remove `__pycache__` and built docs.                     |

## 🤝 Contributing

Contributions are welcome. Fork the repository, create a feature branch, make
your changes, and open a pull request. Please keep changes focused and describe
the motivation in the PR.

## 📄 License

Released under the [MIT License](LICENSE). Copyright © 2026 Raul Cajias.
