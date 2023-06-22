from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_export_job_localization_type, device_management_report_file_format, device_management_report_status, entity

from . import entity

@dataclass
class DeviceManagementExportJob(entity.Entity):
    """
    Entity representing a job to export a report
    """
    # Time that the exported report expires
    expiration_date_time: Optional[datetime] = None
    # Filters applied on the report
    filter: Optional[str] = None
    # Possible values for the file format of a report
    format: Optional[device_management_report_file_format.DeviceManagementReportFileFormat] = None
    # Configures how the requested export job is localized
    localization_type: Optional[device_management_export_job_localization_type.DeviceManagementExportJobLocalizationType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Name of the report
    report_name: Optional[str] = None
    # Time that the exported report was requested
    request_date_time: Optional[datetime] = None
    # Columns selected from the report
    select: Optional[List[str]] = None
    # A snapshot is an identifiable subset of the dataset represented by the ReportName. A sessionId or CachedReportConfiguration id can be used here. If a sessionId is specified, Filter, Select, and OrderBy are applied to the data represented by the sessionId. Filter, Select, and OrderBy cannot be specified together with a CachedReportConfiguration id.
    snapshot_id: Optional[str] = None
    # Possible statuses associated with a generated report
    status: Optional[device_management_report_status.DeviceManagementReportStatus] = None
    # Temporary location of the exported report
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementExportJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementExportJob
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementExportJob()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_export_job_localization_type, device_management_report_file_format, device_management_report_status, entity

        from . import device_management_export_job_localization_type, device_management_report_file_format, device_management_report_status, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "filter": lambda n : setattr(self, 'filter', n.get_str_value()),
            "format": lambda n : setattr(self, 'format', n.get_enum_value(device_management_report_file_format.DeviceManagementReportFileFormat)),
            "localizationType": lambda n : setattr(self, 'localization_type', n.get_enum_value(device_management_export_job_localization_type.DeviceManagementExportJobLocalizationType)),
            "reportName": lambda n : setattr(self, 'report_name', n.get_str_value()),
            "requestDateTime": lambda n : setattr(self, 'request_date_time', n.get_datetime_value()),
            "select": lambda n : setattr(self, 'select', n.get_collection_of_primitive_values(str)),
            "snapshotId": lambda n : setattr(self, 'snapshot_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(device_management_report_status.DeviceManagementReportStatus)),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("filter", self.filter)
        writer.write_enum_value("format", self.format)
        writer.write_enum_value("localizationType", self.localization_type)
        writer.write_str_value("reportName", self.report_name)
        writer.write_datetime_value("requestDateTime", self.request_date_time)
        writer.write_collection_of_primitive_values("select", self.select)
        writer.write_str_value("snapshotId", self.snapshot_id)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("url", self.url)
    

