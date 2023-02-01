from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')

class EffectPostRequestBody(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new effectPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The nominalRate property
        self._nominal_rate: Optional[json.Json] = None
        # The npery property
        self._npery: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EffectPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EffectPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EffectPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "nominalRate": lambda n : setattr(self, 'nominal_rate', n.get_object_value(json.Json)),
            "npery": lambda n : setattr(self, 'npery', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def nominal_rate(self,) -> Optional[json.Json]:
        """
        Gets the nominalRate property value. The nominalRate property
        Returns: Optional[json.Json]
        """
        return self._nominal_rate
    
    @nominal_rate.setter
    def nominal_rate(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the nominalRate property value. The nominalRate property
        Args:
            value: Value to set for the nominal_rate property.
        """
        self._nominal_rate = value
    
    @property
    def npery(self,) -> Optional[json.Json]:
        """
        Gets the npery property value. The npery property
        Returns: Optional[json.Json]
        """
        return self._npery
    
    @npery.setter
    def npery(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the npery property value. The npery property
        Args:
            value: Value to set for the npery property.
        """
        self._npery = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("nominalRate", self.nominal_rate)
        writer.write_object_value("npery", self.npery)
        writer.write_additional_data_value(self.additional_data)
    

