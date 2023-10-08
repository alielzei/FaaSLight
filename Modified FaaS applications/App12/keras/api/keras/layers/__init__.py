# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Public API for tf.keras.layers namespace.
"""

from __future__ import print_function as _print_function

import sys as _sys

from keras.api.keras.layers import experimental
from keras.engine.base_layer import Layer
from keras.engine.base_layer_utils import disable_v2_dtype_behavior
from keras.engine.base_layer_utils import enable_v2_dtype_behavior
from keras.engine.input_layer import Input
from keras.engine.input_layer import InputLayer
from keras.engine.input_spec import InputSpec
from keras.feature_column.dense_features import DenseFeatures
from keras.layers.advanced_activations import ELU
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.advanced_activations import PReLU
from keras.layers.advanced_activations import ReLU
from keras.layers.advanced_activations import Softmax
from keras.layers.advanced_activations import ThresholdedReLU
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import Conv1D as Convolution1D
from keras.layers.convolutional import Conv1DTranspose
from keras.layers.convolutional import Conv1DTranspose as Convolution1DTranspose
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import Conv2D as Convolution2D
from keras.layers.convolutional import Conv2DTranspose
from keras.layers.convolutional import Conv2DTranspose as Convolution2DTranspose
from keras.layers.convolutional import Conv3D
from keras.layers.convolutional import Conv3D as Convolution3D
from keras.layers.convolutional import Conv3DTranspose
from keras.layers.convolutional import Conv3DTranspose as Convolution3DTranspose
from keras.layers.convolutional import Cropping1D
from keras.layers.convolutional import Cropping2D
from keras.layers.convolutional import Cropping3D
from keras.layers.convolutional import DepthwiseConv2D
from keras.layers.convolutional import SeparableConv1D
from keras.layers.convolutional import SeparableConv1D as SeparableConvolution1D
from keras.layers.convolutional import SeparableConv2D
from keras.layers.convolutional import SeparableConv2D as SeparableConvolution2D
from keras.layers.convolutional import UpSampling1D
from keras.layers.convolutional import UpSampling2D
from keras.layers.convolutional import UpSampling3D
from keras.layers.convolutional import ZeroPadding1D
from keras.layers.convolutional import ZeroPadding2D
from keras.layers.convolutional import ZeroPadding3D
from keras.layers.convolutional_recurrent import ConvLSTM1D
from keras.layers.convolutional_recurrent import ConvLSTM2D
from keras.layers.convolutional_recurrent import ConvLSTM3D
from keras.layers.core import Activation
from keras.layers.core import ActivityRegularization
from keras.layers.core import Dense
from keras.layers.core import Dropout
from keras.layers.core import Flatten
from keras.layers.core import Lambda
from keras.layers.core import Masking
from keras.layers.core import Permute
from keras.layers.core import RepeatVector
from keras.layers.core import Reshape
from keras.layers.core import SpatialDropout1D
from keras.layers.core import SpatialDropout2D
from keras.layers.core import SpatialDropout3D
from keras.layers.cudnn_recurrent import CuDNNGRU
from keras.layers.cudnn_recurrent import CuDNNLSTM
from keras.layers.dense_attention import AdditiveAttention
from keras.layers.dense_attention import Attention
from keras.layers.embeddings import Embedding
from keras.layers.local import LocallyConnected1D
from keras.layers.local import LocallyConnected2D
from keras.layers.merge import Add
from keras.layers.merge import Average
from keras.layers.merge import Concatenate
from keras.layers.merge import Dot
from keras.layers.merge import Maximum
from keras.layers.merge import Minimum
from keras.layers.merge import Multiply
from keras.layers.merge import Subtract
from keras.layers.merge import add
from keras.layers.merge import average
from keras.layers.merge import concatenate
from keras.layers.merge import dot
from keras.layers.merge import maximum
from keras.layers.merge import minimum
from keras.layers.merge import multiply
from keras.layers.merge import subtract
from keras.layers.multi_head_attention import MultiHeadAttention
from keras.layers.noise import AlphaDropout
from keras.layers.noise import GaussianDropout
from keras.layers.noise import GaussianNoise
from keras.layers.normalization.batch_normalization_v1 import BatchNormalization
from keras.layers.normalization.layer_normalization import LayerNormalization
from keras.layers.pooling import AveragePooling1D
from keras.layers.pooling import AveragePooling1D as AvgPool1D
from keras.layers.pooling import AveragePooling2D
from keras.layers.pooling import AveragePooling2D as AvgPool2D
from keras.layers.pooling import AveragePooling3D
from keras.layers.pooling import AveragePooling3D as AvgPool3D
from keras.layers.pooling import GlobalAveragePooling1D
from keras.layers.pooling import GlobalAveragePooling1D as GlobalAvgPool1D
from keras.layers.pooling import GlobalAveragePooling2D
from keras.layers.pooling import GlobalAveragePooling2D as GlobalAvgPool2D
from keras.layers.pooling import GlobalAveragePooling3D
from keras.layers.pooling import GlobalAveragePooling3D as GlobalAvgPool3D
from keras.layers.pooling import GlobalMaxPooling1D
from keras.layers.pooling import GlobalMaxPooling1D as GlobalMaxPool1D
from keras.layers.pooling import GlobalMaxPooling2D
from keras.layers.pooling import GlobalMaxPooling2D as GlobalMaxPool2D
from keras.layers.pooling import GlobalMaxPooling3D
from keras.layers.pooling import GlobalMaxPooling3D as GlobalMaxPool3D
from keras.layers.pooling import MaxPooling1D
from keras.layers.pooling import MaxPooling1D as MaxPool1D
from keras.layers.pooling import MaxPooling2D
from keras.layers.pooling import MaxPooling2D as MaxPool2D
from keras.layers.pooling import MaxPooling3D
from keras.layers.pooling import MaxPooling3D as MaxPool3D
from keras.layers.preprocessing.category_encoding import CategoryEncoding
from keras.layers.preprocessing.discretization import Discretization
from keras.layers.preprocessing.hashing import Hashing
from keras.layers.preprocessing.image_preprocessing import CenterCrop
from keras.layers.preprocessing.image_preprocessing import RandomContrast
from keras.layers.preprocessing.image_preprocessing import RandomCrop
from keras.layers.preprocessing.image_preprocessing import RandomFlip
from keras.layers.preprocessing.image_preprocessing import RandomHeight
from keras.layers.preprocessing.image_preprocessing import RandomRotation
from keras.layers.preprocessing.image_preprocessing import RandomTranslation
from keras.layers.preprocessing.image_preprocessing import RandomWidth
from keras.layers.preprocessing.image_preprocessing import RandomZoom
from keras.layers.preprocessing.image_preprocessing import Rescaling
from keras.layers.preprocessing.image_preprocessing import Resizing
from keras.layers.preprocessing.normalization import Normalization
from keras.layers.recurrent import AbstractRNNCell
from keras.layers.recurrent import GRU
from keras.layers.recurrent import GRUCell
from keras.layers.recurrent import LSTM
from keras.layers.recurrent import LSTMCell
from keras.layers.recurrent import RNN
from keras.layers.recurrent import SimpleRNN
from keras.layers.recurrent import SimpleRNNCell
from keras.layers.recurrent import StackedRNNCells
from keras.layers.serialization import deserialize
from keras.layers.serialization import serialize
from keras.layers.wrappers import Bidirectional
from keras.layers.wrappers import TimeDistributed
from keras.layers.wrappers import Wrapper

del _print_function

from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "keras.layers", public_apis=None, deprecation=True,
      has_lite=False)
