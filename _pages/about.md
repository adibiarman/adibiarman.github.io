---
permalink: /
title: "Bio"
excerpt: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am an [Assistant Professor](https://www.augusta.edu/faculty/directory/view.php?id=AADIBI) in the School of Computer and Cyber Sciences at Augusta University. Previously, I was a postdoctoral researcher in Electrical and Computer Engineering at Princeton University, working with [Prof. H. Vincent Poor](https://ece.princeton.edu/people/h-vincent-poor) and [Prof. Sanjeev Kulkarni](https://ece.princeton.edu/people/sanjeev-r-kulkarni). I earned my Ph.D. in Electrical and Systems Engineering from the University of Pennsylvania under [Prof. Hamed Hassani](https://www.engineering.upenn.edu/~hassani/).

## Research

My research combines machine learning, optimization, and statistical inference to study learning and decision-making under uncertainty. I develop algorithms and analyze their sample complexity, convergence rates, and computational costs, with particular emphasis on dependent data, delayed information, distribution changes, and adversarial agents.

- **Reinforcement learning and distributed learning.** I study [stochastic approximation](https://proceedings.mlr.press/v238/adibi24a.html), multi-agent and federated reinforcement learning, and meta-learning. I analyze how Markovian data, delayed updates, communication constraints, and adversarial agents affect convergence and statistical efficiency.

- **Minimax and submodular optimization.** I develop algorithms for problems that combine continuous optimization, discrete decisions, and competing objectives. I study convergence and approximation guarantees for [minimax and submodular optimization](https://proceedings.mlr.press/v151/adibi22a.html), including settings with delays or adversarial data.

- **Sequential inference and quickest change detection.** I design sequential detectors for distribution changes when likelihoods or normalizing constants are unavailable. Recent work uses [diffusion-integrated scores](https://arxiv.org/abs/2610.12200) and [mixtures of detectors](https://arxiv.org/abs/2610.20876) to monitor high-dimensional data and combine evidence across data streams.

- **Generative models and language-model inference.** I study the computational and statistical foundations of generation, including [transformers as in-context samplers](https://arxiv.org/abs/2609.08981) and [game-theoretic decoding](https://arxiv.org/abs/2610.05817) for language models. I examine how sampling and inference procedures use computation at test time.

- **Certified robustness.** I develop optimization-based methods to certify neural-network robustness. Current work uses [sparse second-order cone relaxations](https://arxiv.org/abs/2610.16016) and [cascades of verifiers](https://arxiv.org/abs/2602.04236) to study the trade-off between certificate tightness and verification cost.

- **Information theory and entropy estimation.** I study minimax sample complexity for [Rényi entropy and min-entropy estimation](https://arxiv.org/abs/2607.16966). I examine how the entropy order and dependence between observations affect the amount of data needed for accurate estimation.

See my [publications]({{ '/publications/' | relative_url }}) for papers and preprints.

## Prospective Students

For questions about research opportunities and PhD supervision, please email [aadibi@augusta.edu](mailto:aadibi@augusta.edu) with your CV, transcript, and a brief description of your research interests. Further information about our research is available on the [Research Group]({{ '/research-group/' | relative_url }}) page.
