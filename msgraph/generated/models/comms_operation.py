from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import add_large_gallery_view_operation, cancel_media_processing_operation, entity, invite_participants_operation, mute_participant_operation, operation_status, play_prompt_operation, record_operation, result_info, start_hold_music_operation, stop_hold_music_operation, subscribe_to_tone_operation, unmute_participant_operation, update_recording_status_operation

from . import entity

@dataclass
class CommsOperation(entity.Entity):
    # Unique Client Context string. Max limit is 256 chars.
    client_context: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The result information. Read-only.
    result_info: Optional[result_info.ResultInfo] = None
    # The status property
    status: Optional[operation_status.OperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CommsOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CommsOperation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addLargeGalleryViewOperation".casefold():
            from . import add_large_gallery_view_operation

            return add_large_gallery_view_operation.AddLargeGalleryViewOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cancelMediaProcessingOperation".casefold():
            from . import cancel_media_processing_operation

            return cancel_media_processing_operation.CancelMediaProcessingOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inviteParticipantsOperation".casefold():
            from . import invite_participants_operation

            return invite_participants_operation.InviteParticipantsOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.muteParticipantOperation".casefold():
            from . import mute_participant_operation

            return mute_participant_operation.MuteParticipantOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.playPromptOperation".casefold():
            from . import play_prompt_operation

            return play_prompt_operation.PlayPromptOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.recordOperation".casefold():
            from . import record_operation

            return record_operation.RecordOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.startHoldMusicOperation".casefold():
            from . import start_hold_music_operation

            return start_hold_music_operation.StartHoldMusicOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.stopHoldMusicOperation".casefold():
            from . import stop_hold_music_operation

            return stop_hold_music_operation.StopHoldMusicOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.subscribeToToneOperation".casefold():
            from . import subscribe_to_tone_operation

            return subscribe_to_tone_operation.SubscribeToToneOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unmuteParticipantOperation".casefold():
            from . import unmute_participant_operation

            return unmute_participant_operation.UnmuteParticipantOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.updateRecordingStatusOperation".casefold():
            from . import update_recording_status_operation

            return update_recording_status_operation.UpdateRecordingStatusOperation()
        return CommsOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import add_large_gallery_view_operation, cancel_media_processing_operation, entity, invite_participants_operation, mute_participant_operation, operation_status, play_prompt_operation, record_operation, result_info, start_hold_music_operation, stop_hold_music_operation, subscribe_to_tone_operation, unmute_participant_operation, update_recording_status_operation

        from . import add_large_gallery_view_operation, cancel_media_processing_operation, entity, invite_participants_operation, mute_participant_operation, operation_status, play_prompt_operation, record_operation, result_info, start_hold_music_operation, stop_hold_music_operation, subscribe_to_tone_operation, unmute_participant_operation, update_recording_status_operation

        fields: Dict[str, Callable[[Any], None]] = {
            "clientContext": lambda n : setattr(self, 'client_context', n.get_str_value()),
            "resultInfo": lambda n : setattr(self, 'result_info', n.get_object_value(result_info.ResultInfo)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(operation_status.OperationStatus)),
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
        writer.write_str_value("clientContext", self.client_context)
        writer.write_object_value("resultInfo", self.result_info)
        writer.write_enum_value("status", self.status)
    

