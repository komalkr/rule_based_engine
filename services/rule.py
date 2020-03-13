from db.mongod import insert_one

def addrule(rule,campaign,schedule,condition,action):
    try:

        data = {"rule" : rule, "campaign" : campaign, "schedule" : schedule, "condition" :condition,
                "action" : action}
        result =insert_one(collection="rule",record=data )
        return str(result)
    except Exception as e:
        result = str(e)
    return result