from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase(
    "prince_music",
    user="admin2",
    password="password",
    host="localhost",
    port=5432,
)


class BaseModel(Model):
    class Meta:
        database = db


class Album(BaseModel):
    title = CharField()
    release_date = DateField()
    genre = CharField()
    record_label = CharField()


class Single(BaseModel):
    title = CharField()
    release_date = DateField()
    genre = CharField()
    record_label = CharField()


db.connect()

app = Flask(__name__)

from playhouse.shortcuts import model_to_dict, dict_to_model


@app.route("/albums", methods=["GET", "POST"])
@app.route("/albums/<int:id>", methods=["GET", "PUT", "DELETE"])
def album_endpoint(id=None):
    if request.method == "GET":
        if id:
            return jsonify(model_to_dict(Album.get(Album.id == id)))
        else:
            album_list = [model_to_dict(album) for album in Album.select()]
            return jsonify(album_list)

    if request.method == "PUT":
        body = request.get_json()
        Album.update(**body).where(Album.id == id).execute()
        return f"Album {id} has been updated."

    if request.method == "POST":
        data = request.get_json()
        new_album = dict_to_model(Album, data)
        new_album.save()
        return jsonify({"success": True})

    if request.method == "DELETE":
        Album.delete().where(Album.id == id).execute()
        return f"Album {id} has been deleted."


@app.route("/singles", methods=["GET", "POST"])
@app.route("/singles/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_endpoint(id=None):
    if request.method == "GET":
        if id:
            return jsonify(model_to_dict(Single.get(Single.id == id)))
        else:
            single_list = [model_to_dict(single) for single in Single.select()]
            return jsonify(single_list)

    if request.method == "PUT":
        body = request.get_json()
        Single.update(**body).where(Single.id == id).execute()
        return f"Single {id} has been updated."

    if request.method == "POST":
        data = request.get_json()
        new_single = dict_to_model(Single, data)
        new_single.save()
        return jsonify({"success": True})

    if request.method == "DELETE":
        Single.delete().where(Single.id == id).execute()
        return f"Single {id} has been deleted."


if __name__ == "__main__":
    app.run(debug=True, port=5050)
from flask import Flask, request, jsonify
from peewee import *

db = PostgresqlDatabase(
    "prince_music", user="admin2", password="", host="localhost", port=5432
)


class BaseModel(Model):
    class Meta:
        database = db


class Album(BaseModel):
    title = CharField()
    release_date = DateField()
    genre = CharField()
    record_label = CharField()


class Single(BaseModel):
    title = CharField()
    release_date = DateField()
    genre = CharField()
    record_label = CharField()


db.connect()

app = Flask(__name__)


@app.route("/albums", methods=["GET", "POST"])
@app.route("/albums/<int:id>", methods=["GET", "PUT", "DELETE"])
def album_endpoint(id=None):
    if request.method == "GET":
        if id:
            return jsonify(model_to_dict(Album.get(Album.id == id)))
        else:
            album_list = [model_to_dict(album) for album in Album.select()]
            return jsonify(album_list)

    if request.method == "PUT":
        body = request.get_json()
        Album.update(**body).where(Album.id == id).execute()
        return f"Album {id} has been updated."

    if request.method == "POST":
        data = request.get_json()
        new_album = Album.create(**data)
        return jsonify(model_to_dict(new_album))

    if request.method == "DELETE":
        Album.delete().where(Album.id == id).execute()
        return f"Album {id} has been deleted."


@app.route("/singles", methods=["GET", "POST"])
@app.route("/singles/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_endpoint(id=None):
    if request.method == "GET":
        if id:
            return jsonify(model_to_dict(Single.get(Single.id == id)))
        else:
            single_list = [model_to_dict(single) for single in Single.select()]
            return jsonify(single_list)

    if request.method == "PUT":
        body = request.get_json()
        Single.update(**body).where(Single.id == id).execute()
        return f"Single {id} has been updated."

    if request.method == "POST":
        data = request.get_json()
        new_single = Single.create(**data)
        return jsonify(model_to_dict(new_single))

    if request.method == "DELETE":
        Single.delete().where(Single.id == id).execute()
        return f"Single {id} has been deleted."


if __name__ == "__main__":
    app.run(debug=True, port=5050)
