from __future__ import annotations
from dataclasses import dataclass, field
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import call_recording_status, event_message_detail, identity_set

from . import event_message_detail

@dataclass
class CallRecordingEventMessageDetail(event_message_detail.EventMessageDetail):
    odata_type = "#microsoft.graph.callRecordingEventMessageDetail"
    # Unique identifier of the call.
    call_id: Optional[str] = None
    # Display name for the call recording.
    call_recording_display_name: Optional[str] = None
    # Duration of the call recording.
    call_recording_duration: Optional[timedelta] = None
    # Status of the call recording. Possible values are: success, failure, initial, chunkFinished, unknownFutureValue.
    call_recording_status: Optional[call_recording_status.CallRecordingStatus] = None
    # Call recording URL.
    call_recording_url: Optional[str] = None
    # Initiator of the event.
    initiator: Optional[identity_set.IdentitySet] = None
    # Organizer of the meeting.
    meeting_organizer: Optional[identity_set.IdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CallRecordingEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CallRecordingEventMessageDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CallRecordingEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import call_recording_status, event_message_detail, identity_set

        from . import call_recording_status, event_message_detail, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "callId": lambda n : setattr(self, 'call_id', n.get_str_value()),
            "callRecordingDisplayName": lambda n : setattr(self, 'call_recording_display_name', n.get_str_value()),
            "callRecordingDuration": lambda n : setattr(self, 'call_recording_duration', n.get_timedelta_value()),
            "callRecordingStatus": lambda n : setattr(self, 'call_recording_status', n.get_enum_value(call_recording_status.CallRecordingStatus)),
            "callRecordingUrl": lambda n : setattr(self, 'call_recording_url', n.get_str_value()),
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(identity_set.IdentitySet)),
            "meetingOrganizer": lambda n : setattr(self, 'meeting_organizer', n.get_object_value(identity_set.IdentitySet)),
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
        writer.write_str_value("callId", self.call_id)
        writer.write_str_value("callRecordingDisplayName", self.call_recording_display_name)
        writer.write_timedelta_value("callRecordingDuration", self.call_recording_duration)
        writer.write_enum_value("callRecordingStatus", self.call_recording_status)
        writer.write_str_value("callRecordingUrl", self.call_recording_url)
        writer.write_object_value("initiator", self.initiator)
        writer.write_object_value("meetingOrganizer", self.meeting_organizer)
    

