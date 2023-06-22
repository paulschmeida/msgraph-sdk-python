from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import endpoint, user_feedback
    from .. import identity_set

from . import endpoint

@dataclass
class ParticipantEndpoint(endpoint.Endpoint):
    odata_type = "#microsoft.graph.callRecords.participantEndpoint"
    # CPU number of cores used by the media endpoint.
    cpu_cores_count: Optional[int] = None
    # CPU name used by the media endpoint.
    cpu_name: Optional[str] = None
    # CPU processor speed used by the media endpoint.
    cpu_processor_speed_in_mhz: Optional[int] = None
    # The feedback provided by the user of this endpoint about the quality of the session.
    feedback: Optional[user_feedback.UserFeedback] = None
    # Identity associated with the endpoint.
    identity: Optional[identity_set.IdentitySet] = None
    # Name of the device used by the media endpoint.
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ParticipantEndpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ParticipantEndpoint
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ParticipantEndpoint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import endpoint, user_feedback
        from .. import identity_set

        from . import endpoint, user_feedback
        from .. import identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "cpuCoresCount": lambda n : setattr(self, 'cpu_cores_count', n.get_int_value()),
            "cpuName": lambda n : setattr(self, 'cpu_name', n.get_str_value()),
            "cpuProcessorSpeedInMhz": lambda n : setattr(self, 'cpu_processor_speed_in_mhz', n.get_int_value()),
            "feedback": lambda n : setattr(self, 'feedback', n.get_object_value(user_feedback.UserFeedback)),
            "identity": lambda n : setattr(self, 'identity', n.get_object_value(identity_set.IdentitySet)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_int_value("cpuCoresCount", self.cpu_cores_count)
        writer.write_str_value("cpuName", self.cpu_name)
        writer.write_int_value("cpuProcessorSpeedInMhz", self.cpu_processor_speed_in_mhz)
        writer.write_object_value("feedback", self.feedback)
        writer.write_object_value("identity", self.identity)
        writer.write_str_value("name", self.name)
    

