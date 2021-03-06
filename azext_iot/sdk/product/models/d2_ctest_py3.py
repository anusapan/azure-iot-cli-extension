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


class D2CTest(Model):
    """D2CTest.

    :param expected_message:
    :type expected_message: str
    :param expected_message_count:
    :type expected_message_count: int
    :param validation_timeout:
    :type validation_timeout: int
    :param is_mandatory:
    :type is_mandatory: bool
    :param should_validate:
    :type should_validate: bool
    """

    _attribute_map = {
        'expected_message': {'key': 'expectedMessage', 'type': 'str'},
        'expected_message_count': {'key': 'expectedMessageCount', 'type': 'int'},
        'validation_timeout': {'key': 'validationTimeout', 'type': 'int'},
        'is_mandatory': {'key': 'isMandatory', 'type': 'bool'},
        'should_validate': {'key': 'shouldValidate', 'type': 'bool'},
    }

    def __init__(self, *, expected_message: str=None, expected_message_count: int=None, validation_timeout: int=None, is_mandatory: bool=None, should_validate: bool=None, **kwargs) -> None:
        super(D2CTest, self).__init__(**kwargs)
        self.expected_message = expected_message
        self.expected_message_count = expected_message_count
        self.validation_timeout = validation_timeout
        self.is_mandatory = is_mandatory
        self.should_validate = should_validate
