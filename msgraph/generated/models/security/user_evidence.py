from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert_evidence, user_account

from . import alert_evidence

@dataclass
class UserEvidence(alert_evidence.AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = None
    # The user account details.
    user_account: Optional[user_account.UserAccount] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserEvidence
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import alert_evidence, user_account

        from . import alert_evidence, user_account

        fields: Dict[str, Callable[[Any], None]] = {
            "userAccount": lambda n : setattr(self, 'user_account', n.get_object_value(user_account.UserAccount)),
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
        writer.write_object_value("userAccount", self.user_account)
    

