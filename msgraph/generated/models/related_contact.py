from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import contact_relationship

@dataclass
class RelatedContact(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Indicates whether the user has been consented to access student data.
    access_consent: Optional[bool] = None
    # Name of the contact. Required.
    display_name: Optional[str] = None
    # Primary email address of the contact. Required.
    email_address: Optional[str] = None
    # Mobile phone number of the contact.
    mobile_phone: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The relationship property
    relationship: Optional[contact_relationship.ContactRelationship] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RelatedContact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RelatedContact
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RelatedContact()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import contact_relationship

        from . import contact_relationship

        fields: Dict[str, Callable[[Any], None]] = {
            "accessConsent": lambda n : setattr(self, 'access_consent', n.get_bool_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "mobilePhone": lambda n : setattr(self, 'mobile_phone', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "relationship": lambda n : setattr(self, 'relationship', n.get_enum_value(contact_relationship.ContactRelationship)),
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
        writer.write_bool_value("accessConsent", self.access_consent)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_str_value("mobilePhone", self.mobile_phone)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("relationship", self.relationship)
        writer.write_additional_data_value(self.additional_data)
    

