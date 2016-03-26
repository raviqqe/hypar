# Hypar

## About

Hypar is a library to manage hyper parameters of machine learning models.


## Installation

```
$ pip install hypar
```


## Usage

```
import hypar

hp_class = hypar.hyper_params("foo", "bar")
hp = hp_class(foo=123, bar=456)

assert hp.foo == 123
assert hp.bar == 456
assert isinstance(hp, hp_class)

# Assume that our model, "model1" has a sub model, "model2".

model2_hp_class = hypar.hyper_params("bar")
model1_hp_class = hypar.hyper_params("foo", embed=model2_hp_class)
hp = model1_hp_class(foo=123, bar=456)

assert hp.foo == 123
assert hp.bar == 456
assert isinstance(hp, model1_hp_class)
assert isinstance(hp, model2_hp_class)
assert not isinstance(hp, hp_class)
```


## License

All the contents are released into the public domain.
For more information, see [the unlicense](http://unlicense.org/UNLICENSE).
