import flask
import psycopg2
import psycopg2.extras

from app import app
from instance import config


def get_connection():
    if not hasattr(flask.g, 'dbconn'):
        flask.g.dbconn = psycopg2.connect(
            database=config.DB_NAME, host=config.DB_HOST,
            user=config.DB_USER, password=config.DB_PASS)
    return flask.g.dbconn


def get_cursor():
    return get_connection().cursor(
        cursor_factory=psycopg2.extras.DictCursor)


def query_one(sql, **params):
    with get_cursor() as cur:
        cur.execute(sql, params)
        return dict(cur.fetchone())


def query_all(sql, **params):
    with get_cursor() as cur:
        cur.execute(sql, params)
        result = []
        for row in cur.fetchall():
            result.append(dict(row))
        return result


def _rollback_db(sender, exception, **extra):
    if hasattr(flask.g, 'dbconn'):
        conn = flask.g.dbconn
        conn.rollback()
        conn.close()
        delattr(flask.g, 'dbconn')


def _commit_db(sender, response):
    if hasattr(flask.g, 'dbconn'):
        conn = flask.g.dbconn
        conn.commit()
        conn.close()
        delattr(flask.g, 'dbconn')


def insert(sql, **params):
    with get_cursor() as cur:
        cur.execute(sql, params)
        id = get_cursor().lastrowid #forever return 0
        return id


flask.got_request_exception.connect(_rollback_db, app)
flask.request_finished.connect(_commit_db, app)
