import falcon

from pft.models import Note
from marshmallow import Schema, fields


class NoteSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    content = fields.Str()


class NotesResource:
    def on_get(self, req, resp):
        notes = req.context.db.query(Note).all()
        result = []
        for n in notes:
            result.append(n.asdict())
        resp.media = result

    def on_post(self, req, resp):
        note_data = NoteSchema().load(req.media)
        if note_data.errors:
            resp.media = note_data.errors
            resp.status = falcon.HTTP_BAD_REQUEST
            return

        note = Note().fromdict(note_data.data)

        req.context.db.add(note)
        req.context.db.commit()


class NoteDetails:
    def on_get(self, req, resp, obj_id):
        note = req.context.db.query(Note).get(obj_id)
        if not note:
            raise falcon.HTTPNotFound()
        resp.media = note.asdict()


def register(app: falcon.API, sub_path=''):
    app.add_route(sub_path + '/note', NotesResource())
    app.add_route(sub_path + '/note/{obj_id:int}', NoteDetails())
