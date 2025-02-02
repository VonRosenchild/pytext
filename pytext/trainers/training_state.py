#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved


from typing import Any, Dict

from pytext.common.constants import Stage
from pytext.data.tensorizers import Tensorizer
from pytext.models.model import Model
from pytext.optimizer import Optimizer
from pytext.optimizer.scheduler import Scheduler


class TrainingState:
    model: Model
    optimizer: Optimizer
    scheduler: Scheduler
    start_time: float
    epoch: int = 0
    rank: int = 0
    stage: Stage = Stage.TRAIN
    epochs_since_last_improvement: int = 0
    best_model_state: Any = None
    best_model_metric: Any = None
    tensorizers: Dict[str, Tensorizer] = None

    def __init__(self, **kwargs):
        unknown_keys = kwargs.keys() - TrainingState.__annotations__.keys()
        if unknown_keys:
            raise TypeError(f"TrainingState unexpected attributes {unknown_keys}")
        vars(self).update(kwargs)
