# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""Profile object."""

from senlin.db import api as db_api
from senlin.objects import base
from senlin.objects import fields


@base.SenlinObjectRegistry.register
class Profile(base.SenlinObject, base.VersionedObjectDictCompat):
    """Senlin profile object."""

    fields = {
        'id': fields.UUIDField(),
        'name': fields.StringField(),
        'type': fields.StringField(),
        'context': fields.JsonField(),
        'spec': fields.JsonField(),
        'created_at': fields.DateTimeField(),
        'updated_at': fields.DateTimeField(nullable=True),
        'user': fields.StringField(),
        'project': fields.StringField(),
        'domain': fields.StringField(nullable=True),
        'permission': fields.StringField(nullable=True),
        'metadata': fields.JsonField(nullable=True),
    }

    @classmethod
    def create(cls, context, values):
        obj = db_api.profile_create(context, values)
        return cls._from_db_object(context, cls(context), obj)

    @classmethod
    def get(cls, context, profile_id, **kwargs):
        obj = db_api.profile_get(context, profile_id, **kwargs)
        return cls._from_db_object(context, cls(), obj)

    @classmethod
    def get_by_name(cls, context, name, **kwargs):
        obj = db_api.profile_get_by_name(context, name, **kwargs)
        return cls._from_db_object(context, cls(), obj)

    @classmethod
    def get_by_short_id(cls, context, short_id, **kwargs):
        obj = db_api.profile_get_by_short_id(context, short_id, **kwargs)
        return cls._from_db_object(context, cls(), obj)

    @classmethod
    def get_all(cls, context, **kwargs):
        objs = db_api.profile_get_all(context, **kwargs)
        return [cls._from_db_object(context, cls(), obj) for obj in objs]

    @classmethod
    def update(cls, context, obj_id, values):
        obj = db_api.profile_update(context, obj_id, values)
        return cls._from_db_object(context, cls(), obj)

    @classmethod
    def delete(cls, context, obj_id):
        db_api.profile_delete(context, obj_id)
