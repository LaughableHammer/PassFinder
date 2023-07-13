# Used https://www.youtube.com/watch?v=3NEzo3CfbPg for inspiration


from dataclasses import dataclass


@dataclass
class User:
    """Defines a user"""

    user_id: int
    username: str
    password: str