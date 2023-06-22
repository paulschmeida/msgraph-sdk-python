from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_set

@dataclass
class SharingInvitation(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The email address provided for the recipient of the sharing invitation. Read-only.
    email: Optional[str] = None
    # Provides information about who sent the invitation that created this permission, if that information is available. Read-only.
    invited_by: Optional[identity_set.IdentitySet] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The redeemedBy property
    redeemed_by: Optional[str] = None
    # If true the recipient of the invitation needs to sign in in order to access the shared item. Read-only.
    sign_in_required: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharingInvitation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharingInvitation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SharingInvitation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_set

        from . import identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "invitedBy": lambda n : setattr(self, 'invited_by', n.get_object_value(identity_set.IdentitySet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "redeemedBy": lambda n : setattr(self, 'redeemed_by', n.get_str_value()),
            "signInRequired": lambda n : setattr(self, 'sign_in_required', n.get_bool_value()),
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
        writer.write_str_value("email", self.email)
        writer.write_object_value("invitedBy", self.invited_by)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("redeemedBy", self.redeemed_by)
        writer.write_bool_value("signInRequired", self.sign_in_required)
        writer.write_additional_data_value(self.additional_data)
    

