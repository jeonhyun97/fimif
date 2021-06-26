![](https://user-images.githubusercontent.com/38465539/123514952-6b7fa080-d6d0-11eb-8f1b-da2bb5b8a0e4.png)
---
<p align="center">
  <i>Quality Metrics for evaluating the inter-cluster reliability of Mutldimensional Projections</i>
  <br />
    <a href="">Docs</a>
    ·
<!--     <a href=""> -->
      Paper
<!--   </a> -->
    ·
    <a href="mailto:hj@hcil.snu.ac.kr">Contact</a>

    
  </p>
</p>


## Why Steadiness & Cohesiveness??

For sure, we cannot trust the result seen in multidimensional projections (MDP), such as [*t*-SNE](https://lvdmaaten.github.io/tsne/), [UMAP](https://github.com/lmcinnes/umap), or [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html), which are also known as the embeddings generated by Dimensionality Reduction. As distortions inherently occur when reducing dimensionality, meaningful patterns in projections can be less trustworthy and thus disturb users’ accurate comprehension of the original data, leading to interpretation bias. Therefore, it is vital to measure the overall distortions using quantitative metrics or visualize where and how the distortions occurred in the projection. 

So- which aspects of MDP should be evaluated? There exist numerous criteria to check whether MDP well preserved the characteristics of the original high-dimensional data. Here, we focus on **inter-cluster reliability**, representing how well the projection depicts the **inter-cluster structure** (e.g., number of clusters, outliers, the distance between clusters...). It is important for MDP to have high inter-cluster reliability, as cluster analysis is one of the most critical tasks in MDP. 

However, previous local metrics to evaluate MDP (e.g., Trustworthiness & Continuity, Mean Relative Rank Error) focused on measuring the preservation of nearest neighbors or naively checked the maintenance of predefined clustering result or classes. These approaches cannot properly measure the reliability of the complex inter-cluster structure.

Steadiness & Cohesiveness were designed and implemented to bridge such a gap. By repeatedly extracting a random cluster from one space and measuring how well the cluster stays still in the opposite space, the metrics measure inter-cluster reliability. Note that Steadiness measures the extent to which clusters in the projected space form clusters in the original space, and Cohesiveness measures the opposite.

For more details, please refer our paper (TBA).

*(documentation still in progress)*

## Basic Usage 

If you have trouble using Steadiness & Cohesiveness in your project or research, feel free to contact us ([hj@hcil.snu.ac.kr](mailto:hj@hcil.snu.ac.kr)).
We appreciate all requests about utilizing our metrics!!

### Installation
Steadiness and Cohesiveness are served with conda environment

```sh
## Download file in your project directory
conda activate ...
pip3 install requirements.txt
```

### How to use Stediness & Cohesiveness

```python
import sys

sys.path.append("/absolute/path/to/steadiness-cohesiveness")
import snc as sc

...

# k value for computing Shared Nearest Neighbor-based dissimilarity 
parameter = { "k": 10, "alpha": 0.1 }

metrics = SNC(
  raw=raw_data, 
  emb=emb_data, 
  iteration=300, 
  dist_parameter = parameter
)
metrics.fit()
print(metrics.steadiness(), metrics.cohesiveness())
```

There exists number of parameters for Steadiness & Cohesiveness, but can use default setting (which is described in our paper) by only injecting original data `raw` and projection data `emb` as arguments. Detailed explanation for these parameters is like this:
- **`raw`**: the original (raw) high-dimensional data which used to generate multidimensional projections. Should be a 2D array (or a 2D np array) with shape `(n_samples, n_dim)` where `n_samples` denotes the number of data points in dataset and `n_dim` is the original size of dimensionality (number of features).
- **`emb`**: the projected (embedded) data of **`raw`** (i.e., MDP result). Should be a 2D array (or a 2D np array) with shape `(n_samples, n_reduced_dim)` where `n_reduced_dim` denotes the dimensionality of projection. 

 Refer [API description](#api) for more details about hyperparameter setting.  

## API


### Initialization

```python
class SNC(
    raw, 
    emb, 
    iteration=200, 
    walk_num_ratio=0.4, 
    dist_strategy="snn", 
    dist_paramter={}, 
    dist_function=None,
    cluster_strategy="dbscan"
)
```

***`raw`*** : *`Array, shape=(n_samples, n_dim), dtype=float or int`*

- The original (raw) high-dimensional data which used to generate MDP
- Note that `n_samples` denotes the number of data points in dataset and `n_dim` is the original size of dimensionality


***`emb`*** : *`Array, shape=(n_samples, n_reduced_dim), dtype=float or int`*

***`iteration`*** : *`int, (optional, default: 200)`*

***`walk_num_ratio`*** : *`float, (optional, default: 0.4)`*

***`dist_strategy`*** : *`string, (optional, default: "snn")`*

***`dist_parameter`*** : *`dict, (optional, default: {})`*

***`dist_function`*** : *`function, (optional, default: None)`*

***`cluster_strategy`*** : *`string, (optional, default: "dbscan")`*


### Methods

```python3
SNC.fit(record_vis_info=False)
```
***`record_vis_info`*** : *`bool, (optional, default: False)`*


```python3
SNC.steadiness()
SNC.cohesiveness()
```

```python3
SNC.vis_info(file_path=None)
```

***`file_path`*** : *`bool, (optional, default: None)`*



## Examples



## Visualizing Steadiness & Cohesiveness


![vis](https://user-images.githubusercontent.com/38465539/123515745-b0590680-d6d3-11eb-816d-e725fd5841ee.png)

By visualizing the result of Steadiness and Cohesiveness through the reliability map, it is able to get more insight about how inter-cluster structure is distorted in MDP. Please check [relability map repository](https://github.com/hj-n/snc-reliability-map) and follow the instructions to visualize Steadiness and Cohesiveness in your web browser.

*The reliability map also supports interactions to show Missing Groups — please enjoy it!!*

<p align="center">
<img src="https://user-images.githubusercontent.com/38465539/123516175-c49e0300-d6d5-11eb-9a1c-2215b924ef79.gif" alt="" data-canonical-src="https://user-images.githubusercontent.com/38465539/123516175-c49e0300-d6d5-11eb-9a1c-2215b924ef79.gif" width="45%"/>
</p>
 

## References / Citation

TBA

## Contributors

TBA

