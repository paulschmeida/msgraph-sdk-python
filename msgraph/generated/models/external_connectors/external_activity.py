from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import external_activity_result, external_activity_type, identity
    from .. import entity

from .. import entity

@dataclass
class ExternalActivity(entity.Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents an identity used to identify who is responsible for the activity.
    performed_by: Optional[identity.Identity] = None
    # The date and time when the particular activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    start_date_time: Optional[datetime] = None
    # The type property
    type: Optional[external_activity_type.ExternalActivityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExternalActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExternalActivity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.externalActivityResult".casefold():
            from . import external_activity_result

            return external_activity_result.ExternalActivityResult()
        return ExternalActivity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import external_activity_result, external_activity_type, identity
        from .. import entity

        from . import external_activity_result, external_activity_type, identity
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "performedBy": lambda n : setattr(self, 'performed_by', n.get_object_value(identity.Identity)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(external_activity_type.ExternalActivityType)),
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
        writer.write_object_value("performedBy", self.performed_by)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("type", self.type)
    

