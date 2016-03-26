import collections



# constants

__version__ = "0.0.1"
HYPER_PARAMS = "HyperParams"



# classes

def hyper_params(*param_names, embed=[]):
  if hasattr(embed, "__len__"):
    assert all(__is_hyper_params_class(cls) for cls in embed)
    embedded_hp_classes = embed
  else:
    assert __is_hyper_params_class(embed)
    embedded_hp_classes = [embed]

  all_param_names = set(param_names)
  for embedded_hp_class in embedded_hp_classes:
    all_param_names |= embedded_hp_class.param_names

  class HyperParams(*embedded_hp_classes):
    param_names = all_param_names

    def __init__(self, **params):
      self.__params = self.__struct(*all_param_names)(**params)

    def __getattr__(self, param_name):
      if hasattr(self.__params, param_name):
        return getattr(self.__params, param_name)
      raise AttributeError("No such attribute in any parts of hyper "
                           "parameters. (attribute name: {})"
                           .format(param_name))

    @staticmethod
    def __struct(*members):
      return collections.namedtuple(HYPER_PARAMS, members)

  return HyperParams



# functions

def __is_hyper_params_class(cls):
  return cls.__name__ == HYPER_PARAMS
