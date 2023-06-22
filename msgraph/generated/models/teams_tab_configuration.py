from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class TeamsTabConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Url used for rendering tab contents in Teams. Required.
    content_url: Optional[str] = None
    # Identifier for the entity hosted by the tab provider.
    entity_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Url called by Teams client when a Tab is removed using the Teams Client.
    remove_url: Optional[str] = None
    # Url for showing tab contents outside of Teams.
    website_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamsTabConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamsTabConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamsTabConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "contentUrl": lambda n : setattr(self, 'content_url', n.get_str_value()),
            "entityId": lambda n : setattr(self, 'entity_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "removeUrl": lambda n : setattr(self, 'remove_url', n.get_str_value()),
            "websiteUrl": lambda n : setattr(self, 'website_url', n.get_str_value()),
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
        writer.write_str_value("contentUrl", self.content_url)
        writer.write_str_value("entityId", self.entity_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("removeUrl", self.remove_url)
        writer.write_str_value("websiteUrl", self.website_url)
        writer.write_additional_data_value(self.additional_data)
    

