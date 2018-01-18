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


class RunbookDraft(Model):
    """Definition of the runbook type.

    :param in_edit: Gets or sets whether runbook is in edit mode.
    :type in_edit: bool
    :param draft_content_link: Gets or sets the draft runbook content link.
    :type draft_content_link: ~azure.mgmt.automation.models.ContentLink
    :param creation_time: Gets or sets the creation time of the runbook draft.
    :type creation_time: datetime
    :param last_modified_time: Gets or sets the last modified time of the
     runbook draft.
    :type last_modified_time: datetime
    :param parameters: Gets or sets the runbook draft parameters.
    :type parameters: dict[str,
     ~azure.mgmt.automation.models.RunbookParameter]
    :param output_types: Gets or sets the runbook output types.
    :type output_types: list[str]
    """

    _attribute_map = {
        'in_edit': {'key': 'inEdit', 'type': 'bool'},
        'draft_content_link': {'key': 'draftContentLink', 'type': 'ContentLink'},
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'lastModifiedTime', 'type': 'iso-8601'},
        'parameters': {'key': 'parameters', 'type': '{RunbookParameter}'},
        'output_types': {'key': 'outputTypes', 'type': '[str]'},
    }

    def __init__(self, in_edit=None, draft_content_link=None, creation_time=None, last_modified_time=None, parameters=None, output_types=None):
        super(RunbookDraft, self).__init__()
        self.in_edit = in_edit
        self.draft_content_link = draft_content_link
        self.creation_time = creation_time
        self.last_modified_time = last_modified_time
        self.parameters = parameters
        self.output_types = output_types
