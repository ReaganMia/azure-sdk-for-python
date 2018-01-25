# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Metric(Model):
    """Database metrics.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar start_time: The start time for the metric (ISO-8601 format).
    :vartype start_time: datetime
    :ivar end_time: The end time for the metric (ISO-8601 format).
    :vartype end_time: datetime
    :ivar time_grain: The time step to be used to summarize the metric values.
    :vartype time_grain: str
    :ivar unit: The unit of the metric. Possible values include: 'count',
     'bytes', 'seconds', 'percent', 'countPerSecond', 'bytesPerSecond'
    :vartype unit: str or ~azure.mgmt.sql.models.UnitType
    :ivar name: The name information for the metric.
    :vartype name: ~azure.mgmt.sql.models.MetricName
    :ivar metric_values: The metric values for the specified time window and
     timestep.
    :vartype metric_values: list[~azure.mgmt.sql.models.MetricValue]
    """

    _validation = {
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
        'time_grain': {'readonly': True},
        'unit': {'readonly': True},
        'name': {'readonly': True},
        'metric_values': {'readonly': True},
    }

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'time_grain': {'key': 'timeGrain', 'type': 'str'},
        'unit': {'key': 'unit', 'type': 'str'},
        'name': {'key': 'name', 'type': 'MetricName'},
        'metric_values': {'key': 'metricValues', 'type': '[MetricValue]'},
    }

    def __init__(self):
        super(Metric, self).__init__()
        self.start_time = None
        self.end_time = None
        self.time_grain = None
        self.unit = None
        self.name = None
        self.metric_values = None
