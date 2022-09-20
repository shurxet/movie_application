from marshmallow import Schema, fields


class AuthUserSchema(Schema):
    id = fields.Int()
    email = fields.Str(required=True)
    password = fields.Str(required=True)


class AuthRegistrationRequest(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)
