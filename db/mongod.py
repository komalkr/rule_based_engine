from pymongo import MongoClient
from bson import json_util
import json

def get_db_connection(code= None):
        client = MongoClient('mongodb://localhost:27018/tyroo')
        _db = client['tyroo']
        if code and code in _db.collection_names():
                db =  _db[code]
        else:
                db = _db[code]
        return db



def insert_one(collection=None,record=None):
        try:
                if collection and record :
                        result = get_db_connection(code=collection).insert_one(record)
                        print('celery after insert to db :: {0}'.format(result))
        except Exception as e:
                print("Execption occured while inserting to db :: {0}".format(e))

def find(collection=None, query_params={}, sort_params=None,limit =None):
        try:
                result = None
                if collection:
                        result = list(get_db_connection(code=collection).find(query_params))
        except Exception as e:
                print("Execption occured while fetching from db :: {0}".format(e))
        return result


def find_one(collection=None, query_params={}, projection_params={}, sort_params=None,limit =None):
        try:
                if collection and query_params :
                        result = get_db_connection(code=collection).find_one(query_params)
        except Exception as e:
                print("Execption occured while fetching from db :: {0}".format(e))
        return json.dumps(result, default=json_util.default)
#
# def unique_index(db_name= None , collection=None, query_params={}, projection_params={}, sort_params=None,limit =None):
#         try:
#                 if db_name and collection and query_params :
#                         print('celery before fetching to db :: {0}'.format(query_params))
#                         result = get_db_connection(config=ENVIRONMENT.MONGO_CONFIG,code=collection).create_index([(query_params)], unique=True)
#                         print('celery after insert to db :: {0}'.format(result))
#         except Exception as e:
#                 print("Execption occured while fetching from db :: {0}".format(e))
#
# def get_index(db_name= None , collection=None, query_params={}):
#         try:
#                 if db_name and collection and query_params :
#                         print('celery before fetching to db :: {0}'.format(query_params))
#                         result = get_db_connection(config=ENVIRONMENT.MONGO_CONFIG,code=collection).index_information()
#                         print('celery after insert to db :: {0}'.format(result))
#         except Exception as e:
#                 print("Execption occured while fetching from db :: {0}".format(e))
#
#
def update_one(collection=None, query_params={}, update_params={}, upsert=False):
        result = get_db_connection(code=collection).update_one(query_params, update_params, upsert=upsert)
        return result.modified_count

def aggregate_one(collection=None, query_params={}, update_params={}, upsert=False):
        aggregate_data= [{ '$addFields': update_params}]
        result = get_db_connection(code=collection).aggregate(aggregate_data)
        return result.modified_count

def aggregation(collection=None, pipeline=[], update_params={}, upsert=False):
        result = get_db_connection(code=collection).aggregate(pipeline)
        return list(result)

def count_records(collection=None, query_params=None):
        return get_db_connection(code=collection).find(query_params).count()

def distinct_query(collection =None,query_string="",proj_query ={}):
        dist_query = get_db_connection(code=collection).distinct(query_string,proj_query)
        return json.dumps(dist_query, default=json_util.default)
