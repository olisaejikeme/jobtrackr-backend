from enum import Enum


class ApplicationStatus(str, Enum):
    APPLIED = 'APPLIED'
    INTERVIEW = 'INTERVIEW'
    OFFER = 'OFFER'
    REJECTED = 'REJECTED'