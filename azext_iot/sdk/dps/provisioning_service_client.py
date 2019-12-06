# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.device_enrollment_operations import DeviceEnrollmentOperations
from .operations.device_enrollment_group_operations import DeviceEnrollmentGroupOperations
from .operations.registration_state_operations import RegistrationStateOperations
from . import models
from azext_iot.constants import USER_AGENT


class ProvisioningServiceClientConfiguration(AzureConfiguration):
    """Configuration for ProvisioningServiceClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://localhost'

        super(ProvisioningServiceClientConfiguration, self).__init__(base_url)
        self.add_user_agent('provisioningserviceclient/{}'.format(VERSION))
        self.add_user_agent(USER_AGENT)

        self.credentials = credentials


class ProvisioningServiceClient(object):
    """API for service operations with the Azure IoT Hub Device Provisioning Service

    :ivar config: Configuration for client.
    :vartype config: ProvisioningServiceClientConfiguration

    :ivar device_enrollment: DeviceEnrollment operations
    :vartype device_enrollment: microsoft.azure.management.provisioningservices.operations.DeviceEnrollmentOperations
    :ivar device_enrollment_group: DeviceEnrollmentGroup operations
    :vartype device_enrollment_group: microsoft.azure.management.provisioningservices.operations.DeviceEnrollmentGroupOperations
    :ivar registration_state: RegistrationState operations
    :vartype registration_state: microsoft.azure.management.provisioningservices.operations.RegistrationStateOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = ProvisioningServiceClientConfiguration(credentials, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-09-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.device_enrollment = DeviceEnrollmentOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.device_enrollment_group = DeviceEnrollmentGroupOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.registration_state = RegistrationStateOperations(
            self._client, self.config, self._serialize, self._deserialize)
