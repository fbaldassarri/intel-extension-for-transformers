#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The neural engine operator mapping file."""

from .op import Operator, operator_registry
from .tensor import Tensor


# tf.math.reduce_mean(input_tensor, axis=None, keepdims=False, name=None)
# If axis is None, all dimensions are reduced, and a tensor with a single element is returned.
@operator_registry(operator_type='Mean')
class Mean(Operator):
    """Parse the Mean operator to the neural engine."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

    def set_attr(self, framework, node):
        """Extract the node attr from tensorflow."""
        if framework == 'tensorflow':
            self._attr['axis'] = self._input_tensors[1].data[0]
            self._attr['keep_dims'] = node.attr['keep_dims'].b
