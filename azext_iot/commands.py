# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
Load CLI commands
"""

from azext_iot import iothub_ops, iotdps_ops


def load_command_table(self, _):
    """
    Load CLI commands
    """
    with self.command_group('iot hub', command_type=iothub_ops) as cmd_group:
        cmd_group.command('query', 'iot_query')
        cmd_group.command('invoke-device-method', 'iot_device_method')
        cmd_group.command('invoke-module-method', 'iot_device_module_method')
        cmd_group.command('generate-sas-token', 'iot_get_sas_token')
        cmd_group.command('apply-configuration', 'iot_device_configuration_apply')

        cmd_group.command('show-connection-string', 'iot_get_hub_connection_string')

    with self.command_group('iot hub device-identity', command_type=iothub_ops) as cmd_group:
        cmd_group.command('create', 'iot_device_create')
        cmd_group.command('show', 'iot_device_show')
        cmd_group.command('list', 'iot_device_list')
        cmd_group.command('delete', 'iot_device_delete')
        cmd_group.generic_update_command('update', getter_name='iot_device_show',
                                         setter_name='iot_device_update')

        cmd_group.command('show-connection-string', 'iot_get_device_connection_string')
        cmd_group.command('import', 'iot_device_import')
        cmd_group.command('export', 'iot_device_export')

    with self.command_group('iot hub module-identity', command_type=iothub_ops) as cmd_group:
        cmd_group.command('create', 'iot_device_module_create')
        cmd_group.command('show', 'iot_device_module_show')
        cmd_group.command('list', 'iot_device_module_list')
        cmd_group.command('delete', 'iot_device_module_delete')
        cmd_group.generic_update_command('update', getter_name='iot_device_module_show',
                                         setter_name='iot_device_module_update')

        cmd_group.command('show-connection-string', 'iot_get_module_connection_string')

    with self.command_group('iot hub module-twin', command_type=iothub_ops) as cmd_group:
        cmd_group.command('show', 'iot_device_module_twin_show')
        cmd_group.command('replace', 'iot_device_module_twin_replace')
        cmd_group.generic_update_command('update', getter_name='iot_device_module_twin_show',
                                         setter_name='iot_device_module_twin_update')

    with self.command_group('iot hub device-twin', command_type=iothub_ops) as cmd_group:
        cmd_group.command('show', 'iot_device_twin_show')
        cmd_group.command('replace', 'iot_device_twin_replace')
        cmd_group.generic_update_command('update', getter_name='iot_device_twin_show',
                                         setter_name='iot_device_twin_update')

    with self.command_group('iot edge deployment', command_type=iothub_ops) as cmd_group:
        cmd_group.command('create', 'iot_device_configuration_create')
        cmd_group.command('show', 'iot_device_configuration_show')
        cmd_group.command('list', 'iot_device_configuration_list')
        cmd_group.command('delete', 'iot_device_configuration_delete')
        cmd_group.generic_update_command('update', getter_name='iot_device_configuration_show',
                                         setter_name='iot_device_configuration_update')

    with self.command_group('iot device', command_type=iothub_ops) as cmd_group:
        cmd_group.command('send-d2c-message', 'iot_device_send_message')
        cmd_group.command('simulate', 'iot_simulate_device')
        cmd_group.command('upload-file', 'iot_device_upload_file')

    with self.command_group('iot device c2d-message', command_type=iothub_ops) as cmd_group:
        cmd_group.command('complete', 'iot_c2d_message_complete')
        cmd_group.command('abandon', 'iot_c2d_message_abandon')
        cmd_group.command('reject', 'iot_c2d_message_reject')
        cmd_group.command('receive', 'iot_c2d_message_receive')

    with self.command_group('iot dps enrollment', command_type=iotdps_ops) as cmd_group:
        cmd_group.command('create', 'iot_dps_device_enrollment_create')
        cmd_group.command('list', 'iot_dps_device_enrollment_list')
        cmd_group.command('show', 'iot_dps_device_enrollment_get')
        cmd_group.command('update', 'iot_dps_device_enrollment_update')
        cmd_group.command('delete', 'iot_dps_device_enrollment_delete')

    with self.command_group('iot dps enrollment-group', command_type=iotdps_ops) as cmd_group:
        cmd_group.command('create', 'iot_dps_device_enrollment_group_create')
        cmd_group.command('list', 'iot_dps_device_enrollment_group_list')
        cmd_group.command('show', 'iot_dps_device_enrollment_group_get')
        cmd_group.command('update', 'iot_dps_device_enrollment_group_update')
        cmd_group.command('delete', 'iot_dps_device_enrollment_group_delete')

    with self.command_group('iot dps registration', command_type=iotdps_ops) as cmd_group:
        cmd_group.command('list', 'iot_dps_registration_list')
        cmd_group.command('show', 'iot_dps_registration_get')
        cmd_group.command('delete', 'iot_dps_registration_delete')
