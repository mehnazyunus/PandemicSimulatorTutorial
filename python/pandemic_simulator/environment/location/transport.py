from dataclasses import dataclass

from ..interfaces import BusinessLocationState, ContactRate, EssentialBusinessBaseLocation, SimTime, SimTimeTuple, LocationRule, globals, BaseLocation

__all__ = ['Transport', 'TransportState']

@dataclass
class TransportState(BusinessLocationState):
    contact_rate: ContactRate = ContactRate(1, 10, 10, 0.5, 0.3, 0.3)
    visitor_time: SimTimeTuple(hours=tuple(range(7, 22)), week_days=tuple(range(0, 7)))
    open_time: SimTimeTuple = SimTimeTuple(hours=tuple(range(0, 24)), week_days=tuple(range(0, 6)))

class Transport(EssentialBusinessBaseLocation[TransportState]):
    state_type = TransportState