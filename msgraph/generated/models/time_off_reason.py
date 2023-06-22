from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import change_tracked_entity, time_off_reason_icon_type

from . import change_tracked_entity

@dataclass
class TimeOffReason(change_tracked_entity.ChangeTrackedEntity):
    odata_type = "#microsoft.graph.timeOffReason"
    # The name of the timeOffReason. Required.
    display_name: Optional[str] = None
    # Supported icon types are: none, car, calendar, running, plane, firstAid, doctor, notWorking, clock, juryDuty, globe, cup, phone, weather, umbrella, piggyBank, dog, cake, trafficCone, pin, sunny. Required.
    icon_type: Optional[time_off_reason_icon_type.TimeOffReasonIconType] = None
    # Indicates whether the timeOffReason can be used when creating new entities or updating existing ones. Required.
    is_active: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TimeOffReason:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TimeOffReason
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TimeOffReason()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import change_tracked_entity, time_off_reason_icon_type

        from . import change_tracked_entity, time_off_reason_icon_type

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "iconType": lambda n : setattr(self, 'icon_type', n.get_enum_value(time_off_reason_icon_type.TimeOffReasonIconType)),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("iconType", self.icon_type)
        writer.write_bool_value("isActive", self.is_active)
    

