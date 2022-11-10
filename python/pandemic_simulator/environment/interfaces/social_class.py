from dataclasses import dataclass

__all__ = ['SocialClass']

@dataclass(frozen=True)
class SocialClass:
    social_class:int
