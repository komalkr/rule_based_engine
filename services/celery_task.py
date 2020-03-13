from celery import task
import datetime
import random

@task()
def cron_min_scheduler(x,y):
    try:
        # crone task
        from db.mongod import insert_one
        campaign = ['swiggy','netflix','zomato','expedia'],
        metrix = ['impression','clicks','install','spend']
        now = datetime.datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        insert_one(collection="campaign", record={'campaign':random.choice[campaign],'metrix':random.choice[metrix],"value":random.randint(0,100),"date_time":dt_string })
        print("campaign record has been inserted !!")

    except Exception as e:
        print("Exception occured cron_scheduler :: {0}".format(str(e)))

@task()
def cron_scheduler(x,y):
    try:
        # crone task will run for every 15 min
        from db.mongod import find
        res_list = find(collection='campaign',query_params={"campaign":"swiggy", "metrix":{"$and":['clicks','install']}})
        clicks, install = 0,0
        for item in res_list:
            if item.get('clicks'):
                clicks +=item['clicks']
            elif item.get("install"):
                install +=item['install']

        if clicks >=5000 and install >=100:
            from services.mail import send_mail
            send_mail(email="thekumar@outlook.com",email_to="komalkumar57@gmail.com",email_sub="campaign is stop",password="xxxxxx",name="xyz",rule='swiggy',campaign='swiggy',schedule="current_date",condition="your_condition",action="action")

        print("data has been inserted !!")

    except Exception as e:
        print("Exception occured cron_scheduler :: {0}".format(str(e)))

@task()
def cron_hour_scheduler(x,y):
    try:
        # crone task
        print("crone will work :: for every time : {} {}".format(x,y))
        from db.mongod import insert_one

        insert_one(collection="campaign", record={"date_added":datetime.datetime.now() })
        print("data has been inserted !!")

    except Exception as e:
        print("Exception occured cron_scheduler :: {0}".format(str(e)))

@task()
def cron_midnight_scheduler(x,y):
    try:
        # crone task
        print("crone will work :: for every time : {} {}".format(x,y))
        from db.mongod import insert_one

        insert_one(collection="campaign", record={"date_added":datetime.datetime.now() })
        print("data has been inserted !!")

    except Exception as e:
        print("Exception occured cron_scheduler :: {0}".format(str(e)))