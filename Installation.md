# Installation

In this chapter, you'll learn how to install the package

## Clone from Github

you can install <font color=deeppink>Compbrain</font> from [GitHub](https://github.com/boyuan99/comp-brain)

```
git clone https://github.com/boyuan99/comp-brain.git
```



## Installation with setup.py

Recommended installation method for <font color=deeppink>Compbrain</font> is:

```shell
python setup.py develop
```

it will be installed in your current folder.

Or alternatively, you can do:

```
python setup.py install
```

## Dependency 1: NumPy & tqdm

<font color=deeppink>Compbrain</font> requires several dependent Python packages.

The basic function of <font color=deeppink>Compbrain</font> relies on [numPy](https://numpy.org/) and [tqdm](https://github.com/tqdm/tqdm), which are very easy to install through `pip` :

```
pip install numpy
pip install tqdm
```

or `conda`:

```
conda install numpy
conda install tqdm
```



## Other Dependency

### PyYAML

In order to define a complicated brain circuit, the configuration file for the circuit is essential, which requires [PyYAML](https://pyyaml.org/)

Install `PyYAML` with `pip`:

```
pip install pyyaml
```

or with `conda`:

``` 
conda install pyyaml
```



### Matplotlib

It is recommended that users explicitly import [matplotlib](https://matplotlib.org/) for visualization

```
pip install matplotlib

# or 

conda install matplotlib
```

