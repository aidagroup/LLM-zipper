<p align="center">
  <img src="https://raw.githubusercontent.com/aidagroup/LLM-zipper/main/docs/assets/hero.svg"
       alt="LLM-zipper: know before you compress" width="100%">
</p>

<p align="center">
  <a href="https://pypi.org/project/llm-zipper/"><img src="https://img.shields.io/pypi/v/llm-zipper" alt="PyPI"></a>
  <a href="https://pypi.org/project/llm-zipper/"><img src="https://img.shields.io/pypi/pyversions/llm-zipper" alt="Python"></a>
  <a href="https://github.com/aidagroup/LLM-zipper/actions/workflows/ci.yml"><img src="https://github.com/aidagroup/LLM-zipper/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/aidagroup/LLM-zipper/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue" alt="License"></a>
</p>

**Know before you compress.** LLM-zipper is an open-source framework for cheaper, faster,
energy-efficient LLMs. It predicts how much a model shrinks, and at what quality cost, before
you spend the compute.

We are [AIDA](https://github.com/aidagroup) (AI in Dynamic Action), a research group led by
Dr. habil. Pavel Osinenko. We work on making large models cheaper and faster to run:

- KV-cache compression
- LLM acceleration
- memory-efficient RAG
- RL for adaptive inference
- fine-tuning, tensorization and more

New LLM-zipper modules arrive together with our papers, so each one brings both the theory and
working code.

<p align="center">
  <img src="https://raw.githubusercontent.com/aidagroup/LLM-zipper/main/docs/assets/infra.svg"
       alt="A data center with its own nuclear plant, zipped down to a laptop and one GPU at home"
       width="100%">
  <br>
  <sub>Our goal: take LLMs from data-center scale down to a rig you can run at home.</sub>
</p>

## Install

```bash
pip install llm-zipper
llm-zipper --version
```

## Roadmap

LLM-zipper grows one module at a time. Every module follows the same contract: **scan**
predicts how compressible a part of the model is, **compress** applies a method, and
**evaluate** measures what it cost.

| Module                                                        | Status         |
| ------------------------------------------------------------- | -------------- |
| KV-cache compression across layers, heads and context lengths | in development |
| Theory of LLM tensorizability                                 | in development |
| Efficient fine-tuning                                         | in development |
| Memory-efficient RAG                                          | in development |
| RL for adaptive inference                                     | in development |

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
