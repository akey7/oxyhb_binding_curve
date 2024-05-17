# oxyhb_binding_curve
Calculates oxyHb binding curves as described in the supplement as found in Kinoshita et al. (citation at bottom).

## Conda virtual environment

You can manage the dependencies with conda.

```
conda create -n oxyhb_binding_curve python=3.11
conda install numpy matplotlib jupyterlab
```

If you wish, you can use `pip` as well.

## Usage

The main source file is `oxyhb_binding_curve.py`. It contains a class called `OxyHbBindingCurve` that calculates binding curves based on the equations on page 8 of the supplement of the cited paper. The notebook `plot_binding_curves.ipynb` uses that class to plot binding curves.

## Citation

[doi: 10.1074/jbc.M610717200](https://doi.org/10.1074/jbc.M610717200)

Kinoshita, A. et al. Roles of Hemoglobin Allostery in Hypoxia-induced Metabolic Alterations in Erythrocytes. Journal of Biological Chemistry 282, 10731–10741 (2007).
