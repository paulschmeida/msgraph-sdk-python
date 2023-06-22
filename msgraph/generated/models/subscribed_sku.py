from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import entity, license_units_detail, service_plan_info

from . import entity

@dataclass
class SubscribedSku(entity.Entity):
    # The accountId property
    account_id: Optional[str] = None
    # The accountName property
    account_name: Optional[str] = None
    # For example, 'User' or 'Company'.
    applies_to: Optional[str] = None
    # Possible values are: Enabled, Warning, Suspended, Deleted, LockedOut. The capabilityStatus is Enabled if the prepaidUnits property has at least 1 unit that is enabled, and LockedOut if the customer cancelled their subscription.
    capability_status: Optional[str] = None
    # The number of licenses that have been assigned.
    consumed_units: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Information about the number and status of prepaid licenses.
    prepaid_units: Optional[license_units_detail.LicenseUnitsDetail] = None
    # Information about the service plans that are available with the SKU. Not nullable
    service_plans: Optional[List[service_plan_info.ServicePlanInfo]] = None
    # The unique identifier (GUID) for the service SKU.
    sku_id: Optional[UUID] = None
    # The SKU part number; for example: 'AAD_PREMIUM' or 'RMSBASIC'. To get a list of commercial subscriptions that an organization has acquired, see List subscribedSkus.
    sku_part_number: Optional[str] = None
    # The subscriptionIds property
    subscription_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubscribedSku:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SubscribedSku
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SubscribedSku()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, license_units_detail, service_plan_info

        from . import entity, license_units_detail, service_plan_info

        fields: Dict[str, Callable[[Any], None]] = {
            "accountId": lambda n : setattr(self, 'account_id', n.get_str_value()),
            "accountName": lambda n : setattr(self, 'account_name', n.get_str_value()),
            "appliesTo": lambda n : setattr(self, 'applies_to', n.get_str_value()),
            "capabilityStatus": lambda n : setattr(self, 'capability_status', n.get_str_value()),
            "consumedUnits": lambda n : setattr(self, 'consumed_units', n.get_int_value()),
            "prepaidUnits": lambda n : setattr(self, 'prepaid_units', n.get_object_value(license_units_detail.LicenseUnitsDetail)),
            "servicePlans": lambda n : setattr(self, 'service_plans', n.get_collection_of_object_values(service_plan_info.ServicePlanInfo)),
            "skuId": lambda n : setattr(self, 'sku_id', n.get_uuid_value()),
            "skuPartNumber": lambda n : setattr(self, 'sku_part_number', n.get_str_value()),
            "subscriptionIds": lambda n : setattr(self, 'subscription_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("accountId", self.account_id)
        writer.write_str_value("accountName", self.account_name)
        writer.write_str_value("appliesTo", self.applies_to)
        writer.write_str_value("capabilityStatus", self.capability_status)
        writer.write_int_value("consumedUnits", self.consumed_units)
        writer.write_object_value("prepaidUnits", self.prepaid_units)
        writer.write_collection_of_object_values("servicePlans", self.service_plans)
        writer.write_uuid_value("skuId", self.sku_id)
        writer.write_str_value("skuPartNumber", self.sku_part_number)
        writer.write_collection_of_primitive_values("subscriptionIds", self.subscription_ids)
    

