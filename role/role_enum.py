from enum import Enum

class UserRole(str , Enum) :
    CUSTOMER = "customer"
    ADMIN = "admin"
    AGENT = "agent"

#perticketan
class TicketPriority(str , Enum) :
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"

class TicketStatus(str , Enum) :
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    WAITING_FOR_CUSTOMER = "waiting_for_customer"
    RESOLVED = "resolved"
    CLOSED = "closed"
