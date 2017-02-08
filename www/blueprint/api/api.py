# -*- coding: utf-8 -*-


from datetime import datetime, date
from collections import namedtuple

from bson.objectid import ObjectId
from bson.errors import InvalidId

from flask import Blueprint, jsonify, request, session

from app import app


api_page = Blueprint('api_page',
                     __name__)


CATEGORIES = app.config['ARTICLE_CATEGORIES']
Spider = namedtuple('Spider', ['id', 'source'])


@api_page.route('/vote', methods=['POST'])
def vote():
    from model import get_article, vote_article

    if 'uid' not in session:
        return jsonify(err=1,
                       msg='no uid')

    try:
        aid = request.form['aid']
    except KeyError:
        return jsonify(err=2,
                       msg='no aid')

    try:
        aid = ObjectId(aid)
    except InvalidId:
        return jsonify(err=3,
                       msg='invalid aid')

    a = get_article(aid)

    if a:
        vote_article(a)
        return jsonify(err=0,
                       aid=str(aid))
    else:
        return jsonify(err=4,
                       msg='no article')


@api_page.route('/day', methods=['POST'])
def get_entries_byday():
    from model import get_begin_day, get_entries, get_before_day, get_after_day
    day = request.form.get('day',
                           None)
    try:
        day_entry = date(*(int(_) for _ in day.split('-')))
    except ValueError:
        return jsonify(err=1,
                       msg='invalid day')

    day_begin = get_begin_day()

    if day_begin is None or day_entry is None:
        return jsonify(err=1,
                       msg='no articles')

    if not day_begin <= day_entry <= datetime.utcnow().date():
        return jsonify(err=1,
                       msg='no articles')

    entries = get_entries(day_entry)

    day_before = get_before_day(day_entry)
    if day_before is not None:
        day_before = day_before.strftime('%Y-%m-%d')
    day_after = get_after_day(day_entry)
    if day_after is not None:
        day_after = day_after.strftime('%Y-%m-%d')

    return jsonify(err=0,
                   day_before=day_before,
                   day_after=day_after,
                   data=entries)


@api_page.route('/categories', methods=['GET'])
def categories():
    return jsonify(err=0,
                   data=list(CATEGORIES))


@api_page.route('/entries', methods=['POST'])
def get_entries_byspider():
    from model import get_spiders, get_last_aid, get_first_aid, \
        get_entries_next, get_entries_pre, get_entries_spider

    spid = request.form.get('spid',
                            None)
    if spid is None:
        return jsonify(err=1,
                       msg='no spider id')

    spiders = get_spiders()
    if spid not in spiders:
        return jsonify(err=2,
                       msg='invalid spider id')

    lastaid = get_last_aid(spid)
    firstaid = get_first_aid(spid)
    aid = request.args.get('aid',
                           None) or request.form.get('aid',
                                                     None)
    if aid:
        try:
            aid = ObjectId(aid)
        except InvalidId:
            return jsonify(err=3,
                           msg='invalid aid')

        if not firstaid <= aid <= lastaid:
            return jsonify(err=4,
                           msg='aid not found')

        q = request.form.get('q',
                             None)
        if q == 'p':
            entries = get_entries_pre(spid,
                                      aid)
        else:
            entries = get_entries_next(spid,
                                       aid)

    else:
        entries = get_entries_spider(spid)

    if entries:
        return jsonify(err=0,
                       spider=Spider(spid,
                                     spiders[spid]),
                       entries=entries)
    else:
        return jsonify(err=5,
                       msg='no article found')


@api_page.route('/spiders', methods=['GET'])
def spiders():
    from model import get_spiders

    spiders = get_spiders()
    entries = [Spider(spid, name) for spid, name in spiders.items()]
    return jsonify(err=0,
                   entries=entries)