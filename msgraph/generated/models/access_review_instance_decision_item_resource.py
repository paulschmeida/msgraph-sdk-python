from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_instance_decision_item_access_package_assignment_policy_resource, access_review_instance_decision_item_azure_role_resource, access_review_instance_decision_item_service_principal_resource

@dataclass
class AccessReviewInstanceDecisionItemResource(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Display name of the resource
    display_name: Optional[str] = None
    # Identifier of the resource
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Type of resource. Types include: Group, ServicePrincipal, DirectoryRole, AzureRole, AccessPackageAssignmentPolicy.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewInstanceDecisionItemResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewInstanceDecisionItemResource
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource".casefold():
            from . import access_review_instance_decision_item_access_package_assignment_policy_resource

            return access_review_instance_decision_item_access_package_assignment_policy_resource.AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewInstanceDecisionItemAzureRoleResource".casefold():
            from . import access_review_instance_decision_item_azure_role_resource

            return access_review_instance_decision_item_azure_role_resource.AccessReviewInstanceDecisionItemAzureRoleResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewInstanceDecisionItemServicePrincipalResource".casefold():
            from . import access_review_instance_decision_item_service_principal_resource

            return access_review_instance_decision_item_service_principal_resource.AccessReviewInstanceDecisionItemServicePrincipalResource()
        return AccessReviewInstanceDecisionItemResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_instance_decision_item_access_package_assignment_policy_resource, access_review_instance_decision_item_azure_role_resource, access_review_instance_decision_item_service_principal_resource

        from . import access_review_instance_decision_item_access_package_assignment_policy_resource, access_review_instance_decision_item_azure_role_resource, access_review_instance_decision_item_service_principal_resource

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

