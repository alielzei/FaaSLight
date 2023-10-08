# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""VGG19 model for Keras.

Reference:
  - [Very Deep Convolutional Networks for Large-Scale Image Recognition](
      https://arxiv.org/abs/1409.1556) (ICLR 2015)

"""

from __future__ import print_function as _print_function

import sys as _sys

from tensorflow.python.keras.applications.vgg19 import VGG19
from tensorflow.python.keras.applications.vgg19 import decode_predictions
from tensorflow.python.keras.applications.vgg19 import preprocess_input

del _print_function

from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "keras.applications.vgg19", public_apis=None, deprecation=True,
      has_lite=False)
