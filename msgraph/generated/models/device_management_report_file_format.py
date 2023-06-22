from enum import Enum

class DeviceManagementReportFileFormat(str, Enum):
    # CSV Format
    Csv = "csv",
    # PDF Format
    Pdf = "pdf",
    # JSON Format
    Json = "json",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

