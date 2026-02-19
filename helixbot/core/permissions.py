from dataclasses import dataclass, field


@dataclass(slots=True)
class PermissionContext:
    guild_id: int
    user_id: int
    role_ids: set[int] = field(default_factory=set)


class PermissionEngine:
    def __init__(self) -> None:
        self._role_permissions: dict[int, set[str]] = {}
        self._user_overrides: dict[tuple[int, int], set[str]] = {}

    def grant_role_permission(self, role_id: int, permission: str) -> None:
        self._role_permissions.setdefault(role_id, set()).add(permission)

    def grant_user_override(self, guild_id: int, user_id: int, permission: str) -> None:
        self._user_overrides.setdefault((guild_id, user_id), set()).add(permission)

    def check(self, context: PermissionContext, permission: str) -> bool:
        if permission in self._user_overrides.get((context.guild_id, context.user_id), set()):
            return True
        return any(permission in self._role_permissions.get(role_id, set()) for role_id in context.role_ids)
