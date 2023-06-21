from dataclasses import dataclass


@dataclass
class InteractionHistoryRecord:
    interaction_type: int #enum
    interaction_object: int #user
    interaction_subject: int #user
    day: int

