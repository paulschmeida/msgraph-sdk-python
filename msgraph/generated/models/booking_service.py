from __future__ import annotations
from dataclasses import dataclass, field
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import booking_price_type, booking_question_assignment, booking_reminder, booking_scheduling_policy, entity, location

from . import entity

@dataclass
class BookingService(entity.Entity):
    """
    Represents a particular service offered by a booking business.
    """
    # Additional information that is sent to the customer when an appointment is confirmed.
    additional_information: Optional[str] = None
    # Contains the set of custom questions associated with a particular service.
    custom_questions: Optional[List[booking_question_assignment.BookingQuestionAssignment]] = None
    # The default length of the service, represented in numbers of days, hours, minutes, and seconds. For example, P11D23H59M59.999999999999S.
    default_duration: Optional[timedelta] = None
    # The default physical location for the service.
    default_location: Optional[location.Location] = None
    # The default monetary price for the service.
    default_price: Optional[float] = None
    # Represents the type of pricing of a booking service.
    default_price_type: Optional[booking_price_type.BookingPriceType] = None
    # The default set of reminders for an appointment of this service. The value of this property is available only when reading this bookingService by its ID.
    default_reminders: Optional[List[booking_reminder.BookingReminder]] = None
    # A text description for the service.
    description: Optional[str] = None
    # A service name.
    display_name: Optional[str] = None
    # True if the URL to join the appointment anonymously (anonymousJoinWebUrl) will be generated for the appointment booked for this service.
    is_anonymous_join_enabled: Optional[bool] = None
    # True means this service is not available to customers for booking.
    is_hidden_from_customers: Optional[bool] = None
    # True indicates that the appointments for the service will be held online. Default value is false.
    is_location_online: Optional[bool] = None
    # The language of the self-service booking page.
    language_tag: Optional[str] = None
    # The maximum number of customers allowed in a service. If maximumAttendeesCount of the service is greater than 1, pass valid customer IDs while creating or updating an appointment. To create a customer, use the Create bookingCustomer operation.
    maximum_attendees_count: Optional[int] = None
    # Additional information about this service.
    notes: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The time to buffer after an appointment for this service ends, and before the next customer appointment can be booked.
    post_buffer: Optional[timedelta] = None
    # The time to buffer before an appointment for this service can start.
    pre_buffer: Optional[timedelta] = None
    # The set of policies that determine how appointments for this type of service should be created and managed.
    scheduling_policy: Optional[booking_scheduling_policy.BookingSchedulingPolicy] = None
    # True indicates SMS notifications can be sent to the customers for the appointment of the service. Default value is false.
    sms_notifications_enabled: Optional[bool] = None
    # Represents those staff members who provide this service.
    staff_member_ids: Optional[List[str]] = None
    # The URL a customer uses to access the service.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingService:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BookingService
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BookingService()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import booking_price_type, booking_question_assignment, booking_reminder, booking_scheduling_policy, entity, location

        from . import booking_price_type, booking_question_assignment, booking_reminder, booking_scheduling_policy, entity, location

        fields: Dict[str, Callable[[Any], None]] = {
            "additionalInformation": lambda n : setattr(self, 'additional_information', n.get_str_value()),
            "customQuestions": lambda n : setattr(self, 'custom_questions', n.get_collection_of_object_values(booking_question_assignment.BookingQuestionAssignment)),
            "defaultDuration": lambda n : setattr(self, 'default_duration', n.get_timedelta_value()),
            "defaultLocation": lambda n : setattr(self, 'default_location', n.get_object_value(location.Location)),
            "defaultPrice": lambda n : setattr(self, 'default_price', n.get_float_value()),
            "defaultPriceType": lambda n : setattr(self, 'default_price_type', n.get_enum_value(booking_price_type.BookingPriceType)),
            "defaultReminders": lambda n : setattr(self, 'default_reminders', n.get_collection_of_object_values(booking_reminder.BookingReminder)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isAnonymousJoinEnabled": lambda n : setattr(self, 'is_anonymous_join_enabled', n.get_bool_value()),
            "isHiddenFromCustomers": lambda n : setattr(self, 'is_hidden_from_customers', n.get_bool_value()),
            "isLocationOnline": lambda n : setattr(self, 'is_location_online', n.get_bool_value()),
            "languageTag": lambda n : setattr(self, 'language_tag', n.get_str_value()),
            "maximumAttendeesCount": lambda n : setattr(self, 'maximum_attendees_count', n.get_int_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "postBuffer": lambda n : setattr(self, 'post_buffer', n.get_timedelta_value()),
            "preBuffer": lambda n : setattr(self, 'pre_buffer', n.get_timedelta_value()),
            "schedulingPolicy": lambda n : setattr(self, 'scheduling_policy', n.get_object_value(booking_scheduling_policy.BookingSchedulingPolicy)),
            "smsNotificationsEnabled": lambda n : setattr(self, 'sms_notifications_enabled', n.get_bool_value()),
            "staffMemberIds": lambda n : setattr(self, 'staff_member_ids', n.get_collection_of_primitive_values(str)),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_str_value("additionalInformation", self.additional_information)
        writer.write_collection_of_object_values("customQuestions", self.custom_questions)
        writer.write_timedelta_value("defaultDuration", self.default_duration)
        writer.write_object_value("defaultLocation", self.default_location)
        writer.write_float_value("defaultPrice", self.default_price)
        writer.write_enum_value("defaultPriceType", self.default_price_type)
        writer.write_collection_of_object_values("defaultReminders", self.default_reminders)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isAnonymousJoinEnabled", self.is_anonymous_join_enabled)
        writer.write_bool_value("isHiddenFromCustomers", self.is_hidden_from_customers)
        writer.write_bool_value("isLocationOnline", self.is_location_online)
        writer.write_str_value("languageTag", self.language_tag)
        writer.write_int_value("maximumAttendeesCount", self.maximum_attendees_count)
        writer.write_str_value("notes", self.notes)
        writer.write_timedelta_value("postBuffer", self.post_buffer)
        writer.write_timedelta_value("preBuffer", self.pre_buffer)
        writer.write_object_value("schedulingPolicy", self.scheduling_policy)
        writer.write_bool_value("smsNotificationsEnabled", self.sms_notifications_enabled)
        writer.write_collection_of_primitive_values("staffMemberIds", self.staff_member_ids)
    

