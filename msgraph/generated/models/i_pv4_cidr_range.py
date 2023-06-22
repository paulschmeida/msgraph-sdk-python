from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import ip_range

from . import ip_range

@dataclass
class IPv4CidrRange(ip_range.IpRange):
    odata_type = "#microsoft.graph.iPv4CidrRange"
    # IPv4 address in CIDR notation. Not nullable.
    cidr_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IPv4CidrRange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IPv4CidrRange
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IPv4CidrRange()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import ip_range

        from . import ip_range

        fields: Dict[str, Callable[[Any], None]] = {
            "cidrAddress": lambda n : setattr(self, 'cidr_address', n.get_str_value()),
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
        writer.write_str_value("cidrAddress", self.cidr_address)
    

