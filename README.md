# LLM-zipper

[![PyPI](https://img.shields.io/pypi/v/llm-zipper)](https://pypi.org/project/llm-zipper/)
[![Python](https://img.shields.io/pypi/pyversions/llm-zipper)](https://pypi.org/project/llm-zipper/)
[![CI](https://github.com/aidagroup/LLM-zipper/actions/workflows/ci.yml/badge.svg)](https://github.com/aidagroup/LLM-zipper/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](https://github.com/aidagroup/LLM-zipper/blob/main/LICENSE)

**Know before you compress.** LLM-zipper is an open-source framework for cheaper, faster,
energy-efficient LLMs. It predicts how much a model shrinks, and at what quality cost, before
you spend the compute.

> [!NOTE]
> **Pre-alpha.** This release sets up the project. The first module, KV-cache compression,
> is in development, and the API is not public yet.

## Install

```bash
pip install llm-zipper
llm-zipper --version
```

## Roadmap

LLM-zipper grows one module at a time, and each module comes from a research paper by our
group. Every module follows the same contract: **scan** predicts how compressible a part of
the model is, **compress** applies a method, and **evaluate** measures what it cost.

| Module                                                        | Status         |
| ------------------------------------------------------------- | -------------- |
| KV-cache compression across layers, heads and context lengths | in development |
| Theory of LLM tensorizability                                 | planned        |
| Efficient fine-tuning                                         | planned        |
| RAG compression with tensors                                  | planned        |
| Tensorization of RL agents                                    | planned        |

## Development

```bash
git clone https://github.com/aidagroup/LLM-zipper.git && cd LLM-zipper
uv sync                     # package + dev tools
uv run pre-commit install   # lint and format on every commit
uv run pytest
```

To release, bump `__version__` in `src/llm_zipper/__init__.py`, merge to `main`, then push a
matching tag such as `v0.1.0`. GitHub Actions builds the package and publishes it to PyPI.

## Citation

If LLM-zipper helps your research, please cite it with the metadata in
[`CITATION.cff`](https://github.com/aidagroup/LLM-zipper/blob/main/CITATION.cff). On GitHub,
use **Cite this repository**.

## License

[Apache-2.0](https://github.com/aidagroup/LLM-zipper/blob/main/LICENSE)
