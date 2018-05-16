from flask import Blueprint, request, redirect, jsonify, url_for
from dashbash.dashboard.models import Notes, Tags, NotesTags
from dashbash.database import Session

blue_print_name = 'dashboard'
blue_print_prefix = '/dashboard'

dashboard_blueprint = Blueprint(blue_print_name, __name__, url_prefix=blue_print_prefix)


@dashboard_blueprint.route('/')
def show_user_dashboard():
    # It accepts the name of the function as its first argument and any number of keyword arguments,
    # each corresponding to a variable part of the URL rule.
    # Unknown variable parts are appended to the URL as query parameters.
    return redirect(url_for('home.home_page'))


@dashboard_blueprint.route('/note', methods=['POST', 'GET'])
def insert_note():

    if request.method == 'POST':
        if 'title' in request.json:
            try:
                rec_note = Notes(title=request.json['title'], content=request.json['content'])
                Session.add(rec_note)
                Session.commit()

                tag_list = request.json['tags']

                for tag in tag_list:

                    rec_tag = Tags(tag=tag)
                    Session.add(rec_tag)
                    Session.commit()

                    rec_note_tags = NotesTags(tagId=rec_tag.tId, noteId=rec_note.nId)
                    rec_note.tags.append(rec_note_tags)
                    Session.add(rec_note_tags)
                    Session.commit()

            except KeyError:
                if 'content' not in request.json:
                    return jsonify({"status": "error", "msg": "Content Missing"}), 400
                elif 'tags' not in request.json:
                    return jsonify({"status": "error", "msg": "Tags Missing"}), 400

            return jsonify({"status": "success", "msg": "Note Inserted"}), 200
        else:
            return jsonify({"status": "error", "msg": "Note title required"}), 400

    elif request.method == 'GET':
        all_notes = Session.query(Notes).all()
        notes = []
        for note in all_notes:
            tag_name = []
            for tag in note.tags:
                tag_name.append(Session.query(Tags).filter_by(tId=tag.tagId).all())

            note_json = {"title": note.title, "tags": tag_name}
            notes.append(note_json)

        return jsonify({"status": "success", "data": notes}), 200

    else:
        return jsonify({"status": "error", "msg": "Unsupported method"}), 403
