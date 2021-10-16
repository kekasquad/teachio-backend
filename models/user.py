from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class User(models.Model):
    """ User model
    """

    id = fields.BigIntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    name = fields.CharField(max_length=50, null=True)
    password_hash = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    class PydanticMeta:
        exclude = ['password_hash']


User_Pydantic = pydantic_model_creator(User, name='User')
UserIn_Pydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)
