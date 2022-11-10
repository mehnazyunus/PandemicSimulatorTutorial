# Confidential, Copyright 2020, Sony Corporation of America, All rights reserved.
from dataclasses import dataclass

__all__ = ['LocationID', 'PersonID', 'SocialClass']


@dataclass(frozen=True)
class LocationID:
    name: str


@dataclass(frozen=True)
class PersonID:
    name: str
    age: int

@dataclass(frozen=True)
class SocialClass:
    social_class:int
