from telegram import Chat, User

from elisa import OWNER_ID


def user_can_promote(chat: Chat, user: User, bot_id: int) -> bool:
    if (
        user.id in int(OWNER_ID)
    ):
        return True
    return chat.get_member(user.id).can_promote_members


def user_can_ban(chat: Chat, user: User, bot_id: int) -> bool:
    return chat.get_member(user.id).can_restrict_members


def user_can_pin(chat: Chat, user: User, bot_id: int) -> bool:
    return chat.get_member(user.id).can_pin_messages


def user_can_invite(chat: Chat, user: User, bot_id: int) -> bool:
    return chat.get_member(user.id).can_invite_users


def user_can_changeinfo(chat: Chat, user: User, bot_id: int) -> bool:
    return chat.get_member(user.id).can_change_info


def user_can_delete(chat: Chat, user: User, bot_id: int) -> bool:
    return chat.get_member(user.id).can_delete_messages
