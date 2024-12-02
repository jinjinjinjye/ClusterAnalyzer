# Cluster_Analyzer [📄**arXiv**](https://arxiv.org/abs/2411.07189)

`cluster_analyzer` is a Python library designed to analyze critical behavior, self-similarity, and fractal dimensions of clusters in cellular automata. It provides tools for simulating cluster formation, performing statistical analyses, and visualizing results.

<p align="center">
    <img src="https://raw.githubusercontent.com/HakanAkgn/ClusterAnalyzer/main/assets/fractal_latest.png" width="800" />
</p>

## Features
- Optimized cluster detection
- Simulate Logistic Game of Life (LGOL) and find polynomial solutions.
- Analyze cluster sizes and their distributions.
- Perform power-law fitting and goodness-of-fit tests and visualizations based on [powerlaw package](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0085777) developed in on the statistical methods developed in [Clauset et al. 2007](https://arxiv.org/abs/0706.1062) and [Klaus et al. 2011](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0019779).
- Generate Probability Density Function (PDF) and Complementary Cumulative Distribution Function (CCDF) plots.

## Installation

You can install ClusterAnalyzer via pip:

```bash
pip install cluster-analyzer
```

or clone the repository and install it manually:

```bash
git clone https://github.com/HakanAkgn/ClusterAnalyzer.git

cd ClusterAnalyzer

pip install -e . # or turn off the editable mode with `pip install .`
```

Check the installation:

```python
import cluster_analyzer as ca
print(ca.__version__)
```

## Usage

Resort to the [Demo Notebook](https://github.com/HakanAkgn/ClusterAnalyzer/blob/main/Cluster_Analyzer_Demo.ipynb) for examples of each function.

## Citation
If you find this work useful, please cite our paper:

```bibtex
@misc{akgün2024deterministiccriticalitycluster,
      title={Deterministic criticality & cluster dynamics hidden in the Game of Life}, 
      author={Hakan Akgün and Xianquan Yan and Tamer Taşkıran and Muhamet Ibrahimi and Arash Mobaraki and Ching Hua Lee and Seymur Jahangirov},
      year={2024},
      eprint={2411.07189},
      archivePrefix={arXiv},
      primaryClass={cond-mat.stat-mech},
      url={https://arxiv.org/abs/2411.07189}, 
}
```