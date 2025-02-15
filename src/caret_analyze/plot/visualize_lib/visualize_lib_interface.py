# Copyright 2021 Research Institute of Systems Planning, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABCMeta, abstractmethod
from typing import Sequence, Union

from bokeh.plotting import Figure

from ..metrics_base import MetricsBase
from ...runtime import CallbackBase, CallbackGroup, Communication, Publisher, Subscription

TimeSeriesTypes = Union[CallbackBase, Communication, Union[Publisher, Subscription]]


class VisualizeLibInterface(metaclass=ABCMeta):
    """Interface class for VisualizeLib."""

    @abstractmethod
    def callback_scheduling(
        self,
        callback_groups: Sequence[CallbackGroup],
        xaxis_type: str,
        ywheel_zoom: bool,
        full_legends: bool,
        coloring_rule: str,
        lstrip_s: float,
        rstrip_s: float
    ) -> Figure:
        raise NotImplementedError()

    @abstractmethod
    def timeseries(
        self,
        metrics: MetricsBase,
        xaxis_type: str,
        ywheel_zoom: bool,
        full_legends: bool
    ) -> Figure:
        raise NotImplementedError()
