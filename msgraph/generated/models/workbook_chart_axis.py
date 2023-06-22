from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, json, workbook_chart_axis_format, workbook_chart_axis_title, workbook_chart_gridlines

from . import entity

@dataclass
class WorkbookChartAxis(entity.Entity):
    # Represents the formatting of a chart object, which includes line and font formatting. Read-only.
    format: Optional[workbook_chart_axis_format.WorkbookChartAxisFormat] = None
    # Returns a gridlines object that represents the major gridlines for the specified axis. Read-only.
    major_gridlines: Optional[workbook_chart_gridlines.WorkbookChartGridlines] = None
    # Represents the interval between two major tick marks. Can be set to a numeric value or an empty string.  The returned value is always a number.
    major_unit: Optional[json.Json] = None
    # Represents the maximum value on the value axis.  Can be set to a numeric value or an empty string (for automatic axis values).  The returned value is always a number.
    maximum: Optional[json.Json] = None
    # Represents the minimum value on the value axis. Can be set to a numeric value or an empty string (for automatic axis values).  The returned value is always a number.
    minimum: Optional[json.Json] = None
    # Returns a Gridlines object that represents the minor gridlines for the specified axis. Read-only.
    minor_gridlines: Optional[workbook_chart_gridlines.WorkbookChartGridlines] = None
    # Represents the interval between two minor tick marks. 'Can be set to a numeric value or an empty string (for automatic axis values). The returned value is always a number.
    minor_unit: Optional[json.Json] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the axis title. Read-only.
    title: Optional[workbook_chart_axis_title.WorkbookChartAxisTitle] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookChartAxis:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartAxis
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkbookChartAxis()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, json, workbook_chart_axis_format, workbook_chart_axis_title, workbook_chart_gridlines

        from . import entity, json, workbook_chart_axis_format, workbook_chart_axis_title, workbook_chart_gridlines

        fields: Dict[str, Callable[[Any], None]] = {
            "format": lambda n : setattr(self, 'format', n.get_object_value(workbook_chart_axis_format.WorkbookChartAxisFormat)),
            "majorGridlines": lambda n : setattr(self, 'major_gridlines', n.get_object_value(workbook_chart_gridlines.WorkbookChartGridlines)),
            "majorUnit": lambda n : setattr(self, 'major_unit', n.get_object_value(json.Json)),
            "maximum": lambda n : setattr(self, 'maximum', n.get_object_value(json.Json)),
            "minimum": lambda n : setattr(self, 'minimum', n.get_object_value(json.Json)),
            "minorGridlines": lambda n : setattr(self, 'minor_gridlines', n.get_object_value(workbook_chart_gridlines.WorkbookChartGridlines)),
            "minorUnit": lambda n : setattr(self, 'minor_unit', n.get_object_value(json.Json)),
            "title": lambda n : setattr(self, 'title', n.get_object_value(workbook_chart_axis_title.WorkbookChartAxisTitle)),
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
        writer.write_object_value("format", self.format)
        writer.write_object_value("majorGridlines", self.major_gridlines)
        writer.write_object_value("majorUnit", self.major_unit)
        writer.write_object_value("maximum", self.maximum)
        writer.write_object_value("minimum", self.minimum)
        writer.write_object_value("minorGridlines", self.minor_gridlines)
        writer.write_object_value("minorUnit", self.minor_unit)
        writer.write_object_value("title", self.title)
    

