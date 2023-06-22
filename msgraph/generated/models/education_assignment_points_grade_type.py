from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_assignment_grade_type

from . import education_assignment_grade_type

@dataclass
class EducationAssignmentPointsGradeType(education_assignment_grade_type.EducationAssignmentGradeType):
    odata_type = "#microsoft.graph.educationAssignmentPointsGradeType"
    # Max points possible for this assignment.
    max_points: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationAssignmentPointsGradeType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationAssignmentPointsGradeType
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EducationAssignmentPointsGradeType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_assignment_grade_type

        from . import education_assignment_grade_type

        fields: Dict[str, Callable[[Any], None]] = {
            "maxPoints": lambda n : setattr(self, 'max_points', n.get_float_value()),
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
        writer.write_float_value("maxPoints", self.max_points)
    

