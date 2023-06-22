from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import managed_app_data_encryption_type, managed_app_policy_deployment_summary, managed_mobile_app, targeted_managed_app_protection

from . import targeted_managed_app_protection

@dataclass
class IosManagedAppProtection(targeted_managed_app_protection.TargetedManagedAppProtection):
    odata_type = "#microsoft.graph.iosManagedAppProtection"
    # Represents the level to which app data is encrypted for managed apps
    app_data_encryption_type: Optional[managed_app_data_encryption_type.ManagedAppDataEncryptionType] = None
    # List of apps to which the policy is deployed.
    apps: Optional[List[managed_mobile_app.ManagedMobileApp]] = None
    # A custom browser protocol to open weblink on iOS. When this property is configured, ManagedBrowserToOpenLinksRequired should be true.
    custom_browser_protocol: Optional[str] = None
    # Count of apps to which the current policy is deployed.
    deployed_app_count: Optional[int] = None
    # Navigation property to deployment summary of the configuration.
    deployment_summary: Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary] = None
    # Indicates whether use of the FaceID is allowed in place of a pin if PinRequired is set to True.
    face_id_blocked: Optional[bool] = None
    # Versions less than the specified version will block the managed app from accessing company data.
    minimum_required_sdk_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosManagedAppProtection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IosManagedAppProtection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import managed_app_data_encryption_type, managed_app_policy_deployment_summary, managed_mobile_app, targeted_managed_app_protection

        from . import managed_app_data_encryption_type, managed_app_policy_deployment_summary, managed_mobile_app, targeted_managed_app_protection

        fields: Dict[str, Callable[[Any], None]] = {
            "appDataEncryptionType": lambda n : setattr(self, 'app_data_encryption_type', n.get_enum_value(managed_app_data_encryption_type.ManagedAppDataEncryptionType)),
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(managed_mobile_app.ManagedMobileApp)),
            "customBrowserProtocol": lambda n : setattr(self, 'custom_browser_protocol', n.get_str_value()),
            "deployedAppCount": lambda n : setattr(self, 'deployed_app_count', n.get_int_value()),
            "deploymentSummary": lambda n : setattr(self, 'deployment_summary', n.get_object_value(managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary)),
            "faceIdBlocked": lambda n : setattr(self, 'face_id_blocked', n.get_bool_value()),
            "minimumRequiredSdkVersion": lambda n : setattr(self, 'minimum_required_sdk_version', n.get_str_value()),
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
        writer.write_enum_value("appDataEncryptionType", self.app_data_encryption_type)
        writer.write_collection_of_object_values("apps", self.apps)
        writer.write_str_value("customBrowserProtocol", self.custom_browser_protocol)
        writer.write_int_value("deployedAppCount", self.deployed_app_count)
        writer.write_object_value("deploymentSummary", self.deployment_summary)
        writer.write_bool_value("faceIdBlocked", self.face_id_blocked)
        writer.write_str_value("minimumRequiredSdkVersion", self.minimum_required_sdk_version)
    

