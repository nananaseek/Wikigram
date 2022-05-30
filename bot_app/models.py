from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Language(models.Model):
    id = fields.IntField(pk=True)
    user_id = fields.IntField(max_length=32)
    language = fields.CharField(max_length=16)


Language_Pydantic = pydantic_model_creator(Language, name="Language")
LanguageIn_Pydantic = pydantic_model_creator(Language, name="LanguageIn", exclude_readonly=True)
