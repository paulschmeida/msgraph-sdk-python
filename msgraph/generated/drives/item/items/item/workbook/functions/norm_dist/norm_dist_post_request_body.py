from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

@dataclass
class Norm_DistPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The cumulative property
    cumulative: Optional[json.Json] = None
    # The mean property
    mean: Optional[json.Json] = None
    # The standardDev property
    standard_dev: Optional[json.Json] = None
    # The x property
    x: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Norm_DistPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Norm_DistPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Norm_DistPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "cumulative": lambda n : setattr(self, 'cumulative', n.get_object_value(json.Json)),
            "mean": lambda n : setattr(self, 'mean', n.get_object_value(json.Json)),
            "standardDev": lambda n : setattr(self, 'standard_dev', n.get_object_value(json.Json)),
            "x": lambda n : setattr(self, 'x', n.get_object_value(json.Json)),
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
        writer.write_object_value("cumulative", self.cumulative)
        writer.write_object_value("mean", self.mean)
        writer.write_object_value("standardDev", self.standard_dev)
        writer.write_object_value("x", self.x)
        writer.write_additional_data_value(self.additional_data)
    

