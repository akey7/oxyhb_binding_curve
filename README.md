# oxyhb_binding_curve
Calculates oxyHb binding curves as described in the supplement as found in Dash et al. (citation at bottom).

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

Dash, R.K., Korman, B. & Bassingthwaighte, J.B. Simple accurate mathematical models of blood HbO2 and HbCO2 dissociation curves at varied physiological conditions: evaluation and comparison with other models. Eur J Appl Physiol 116, 97–113 (2016). https://doi.org/10.1007/s00421-015-3228-3
