from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

@dataclass
class ProfilePhoto(entity.Entity):
    # The height of the photo. Read-only.
    height: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The width of the photo. Read-only.
    width: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProfilePhoto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProfilePhoto
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ProfilePhoto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "height": lambda n : setattr(self, 'height', n.get_int_value()),
            "width": lambda n : setattr(self, 'width', n.get_int_value()),
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
        writer.write_int_value("height", self.height)
        writer.write_int_value("width", self.width)
    

