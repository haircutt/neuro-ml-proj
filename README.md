# neuro-clustering

Identifying limitations within clustering (HDBScan) of Electroencephalography (EEG) reads.

## Overview


Two clustering approaches are compared:

- **Polarity-sensitive** — standard Euclidean-distance HDBSCAN, where a topography and its
  polarity-inverted counterpart (+A / -A) are treated as different states.
- **Polarity-invariant** — HDBSCAN with a custom distance metric that treats +A and -A as the
  same microstate (based on squared correlation), which is the standard assumption in EEG
  microstate literature.

For both approaches, `min_cluster_size` is swept over `[3, 5, 7, 8, 10, 20, 30, 50, 100, 150, 200]`
to examine how the number of detected clusters and the amount of noise (unassigned points) changes
as the clustering becomes coarser.


- `main.py` — quick script for loading and plotting a single raw EEG recording. First attempt at reading an EEG
- `microstate-clustering-eeg.ipynb` — main notebook: data loading, GFP peak extraction, HDBSCAN
  sweeps (polarity-sensitive and polarity-invariant), PCA projections, cluster centroid
  topographies, raincloud/density plots, and summary tables of results.
- `gfp_peaks/` — cached GFP peak indices/topographies per recording.
- `clustering-results/` — CSV checkpoints of HDBSCAN sweep results:
  - `polarity-inclusive-no-min-size.csv` — polarity-sensitive sweep results.
  - `polarity-invariant-min-cluster.csv` — polarity-invariant sweep results.

## Key findings

- With the standard (polarity-sensitive) distance metric, larger `min_cluster_size` values tend to
  push most fits toward 0 clusters
- With the polarity-invariant metric, most fits converge to a single cluster (1) across
  `min_cluster_size` values, which matches the expectation that polarity-inverted topographies
  represent the same microstate.
