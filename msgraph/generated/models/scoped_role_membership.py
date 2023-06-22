from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, identity

from . import entity

@dataclass
class ScopedRoleMembership(entity.Entity):
    # Unique identifier for the administrative unit that the directory role is scoped to
    administrative_unit_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Unique identifier for the directory role that the member is in.
    role_id: Optional[str] = None
    # The roleMemberInfo property
    role_member_info: Optional[identity.Identity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ScopedRoleMembership:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ScopedRoleMembership
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ScopedRoleMembership()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, identity

        from . import entity, identity

        fields: Dict[str, Callable[[Any], None]] = {
            "administrativeUnitId": lambda n : setattr(self, 'administrative_unit_id', n.get_str_value()),
            "roleId": lambda n : setattr(self, 'role_id', n.get_str_value()),
            "roleMemberInfo": lambda n : setattr(self, 'role_member_info', n.get_object_value(identity.Identity)),
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
        writer.write_str_value("administrativeUnitId", self.administrative_unit_id)
        writer.write_str_value("roleId", self.role_id)
        writer.write_object_value("roleMemberInfo", self.role_member_info)
    

