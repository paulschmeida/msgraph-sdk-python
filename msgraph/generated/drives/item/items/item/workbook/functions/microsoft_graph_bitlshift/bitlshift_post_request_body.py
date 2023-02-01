from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')

class BitlshiftPostRequestBody(AdditionalDataHolder, Parsable):
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
        Instantiates a new bitlshiftPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The number property
        self._number: Optional[json.Json] = None
        # The shiftAmount property
        self._shift_amount: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BitlshiftPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BitlshiftPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BitlshiftPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "number": lambda n : setattr(self, 'number', n.get_object_value(json.Json)),
            "shiftAmount": lambda n : setattr(self, 'shift_amount', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def number(self,) -> Optional[json.Json]:
        """
        Gets the number property value. The number property
        Returns: Optional[json.Json]
        """
        return self._number
    
    @number.setter
    def number(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the number property value. The number property
        Args:
            value: Value to set for the number property.
        """
        self._number = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("number", self.number)
        writer.write_object_value("shiftAmount", self.shift_amount)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def shift_amount(self,) -> Optional[json.Json]:
        """
        Gets the shiftAmount property value. The shiftAmount property
        Returns: Optional[json.Json]
        """
        return self._shift_amount
    
    @shift_amount.setter
    def shift_amount(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the shiftAmount property value. The shiftAmount property
        Args:
            value: Value to set for the shift_amount property.
        """
        self._shift_amount = value
    

