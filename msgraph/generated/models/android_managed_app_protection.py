from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import managed_app_policy_deployment_summary, managed_mobile_app, targeted_managed_app_protection

from . import targeted_managed_app_protection

@dataclass
class AndroidManagedAppProtection(targeted_managed_app_protection.TargetedManagedAppProtection):
    odata_type = "#microsoft.graph.androidManagedAppProtection"
    # List of apps to which the policy is deployed.
    apps: Optional[List[managed_mobile_app.ManagedMobileApp]] = None
    # Friendly name of the preferred custom browser to open weblink on Android. When this property is configured, ManagedBrowserToOpenLinksRequired should be true.
    custom_browser_display_name: Optional[str] = None
    # Unique identifier of the preferred custom browser to open weblink on Android. When this property is configured, ManagedBrowserToOpenLinksRequired should be true.
    custom_browser_package_id: Optional[str] = None
    # Count of apps to which the current policy is deployed.
    deployed_app_count: Optional[int] = None
    # Navigation property to deployment summary of the configuration.
    deployment_summary: Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary] = None
    # When this setting is enabled, app level encryption is disabled if device level encryption is enabled
    disable_app_encryption_if_device_encryption_is_enabled: Optional[bool] = None
    # Indicates whether application data for managed apps should be encrypted
    encrypt_app_data: Optional[bool] = None
    # Define the oldest required Android security patch level a user can have to gain secure access to the app.
    minimum_required_patch_version: Optional[str] = None
    # Define the oldest recommended Android security patch level a user can have for secure access to the app.
    minimum_warning_patch_version: Optional[str] = None
    # Indicates whether a managed user can take screen captures of managed apps
    screen_capture_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedAppProtection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidManagedAppProtection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import managed_app_policy_deployment_summary, managed_mobile_app, targeted_managed_app_protection

        from . import managed_app_policy_deployment_summary, managed_mobile_app, targeted_managed_app_protection

        fields: Dict[str, Callable[[Any], None]] = {
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(managed_mobile_app.ManagedMobileApp)),
            "customBrowserDisplayName": lambda n : setattr(self, 'custom_browser_display_name', n.get_str_value()),
            "customBrowserPackageId": lambda n : setattr(self, 'custom_browser_package_id', n.get_str_value()),
            "deployedAppCount": lambda n : setattr(self, 'deployed_app_count', n.get_int_value()),
            "deploymentSummary": lambda n : setattr(self, 'deployment_summary', n.get_object_value(managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary)),
            "disableAppEncryptionIfDeviceEncryptionIsEnabled": lambda n : setattr(self, 'disable_app_encryption_if_device_encryption_is_enabled', n.get_bool_value()),
            "encryptAppData": lambda n : setattr(self, 'encrypt_app_data', n.get_bool_value()),
            "minimumRequiredPatchVersion": lambda n : setattr(self, 'minimum_required_patch_version', n.get_str_value()),
            "minimumWarningPatchVersion": lambda n : setattr(self, 'minimum_warning_patch_version', n.get_str_value()),
            "screenCaptureBlocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("apps", self.apps)
        writer.write_str_value("customBrowserDisplayName", self.custom_browser_display_name)
        writer.write_str_value("customBrowserPackageId", self.custom_browser_package_id)
        writer.write_int_value("deployedAppCount", self.deployed_app_count)
        writer.write_object_value("deploymentSummary", self.deployment_summary)
        writer.write_bool_value("disableAppEncryptionIfDeviceEncryptionIsEnabled", self.disable_app_encryption_if_device_encryption_is_enabled)
        writer.write_bool_value("encryptAppData", self.encrypt_app_data)
        writer.write_str_value("minimumRequiredPatchVersion", self.minimum_required_patch_version)
        writer.write_str_value("minimumWarningPatchVersion", self.minimum_warning_patch_version)
        writer.write_bool_value("screenCaptureBlocked", self.screen_capture_blocked)
    

