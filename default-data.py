import pymongo
import random
import datetime
from bson.objectid import ObjectId
import re

# Connection String
conn = pymongo.MongoClient("mongodb://mongoserver:27017/", username='root', password='rootpassword')
#conn = pymongo.MongoClient("mongodb://devops.skan.ai:8806/", username='admin', password='rootpassword')
print('connected')

# conn = pymongo.MongoClient("mongodb://cpxnext-cloud.skan.ai:8810/", username='admin', password="xCjpzz#\'>?xp:b6!")

SkanDB = conn["SkanDB"]
activities_db = conn["activities_db"]
applications_db = conn["applications_db"]
cases_db = conn["cases_db"]
discovery_preferences_db = conn["discovery_preferences_db"]
general_preferences_db = conn["general_preferences_db"]
lookups_db = conn["lookups_db"]
metrics_db = conn["metrics_db"]
personas_db = conn["personas_db"]
processes_db = conn["processes_db"]
raw_events_db = conn["raw_events_db"]
users_db = conn["users_db"]


def insertDefaultAuth():
    db = conn["SkanDB"]
    col = db["Auth"]

    col.delete_many({})
    default_auth = {
        "user": "admin@skan.ai",
        "password_hash": "24f80e59aa4904bf147e080ac509ba55e0ce292f2daf502a3eb72530767dbc3e9d3da4531623a7c49c2733f6d1913b1c47248317943e976490fd73c8f8177a99",
        "failed_attempt_count": 0,
        "is_captcha_required": False,
        "last_failed_attempt": datetime.datetime.now()
    }
    col.insert_one(default_auth)


def insertDefaultTeam():
    db = conn["SkanDB"]
    col = db["Teams"]

    col.delete_many({})
    default_team = {
        "status": "Active",
        "name": "Skan Support",
        "email": "admin@skan.ai",
        "role": "admin",
        "process": [],
        "invite_timestamp": datetime.datetime.now(),
        "uuid": "44725b1bc97b436483453853ac885711",
        "is_SSO_user": False
    }
    col.insert_one(default_team)


def insertDefaultVaPreferences():
    db = conn["general_preferences_db"]
    col = db["va_preferences"]

    col.delete_many({})
    default_va_preferences = {
        "initial_command": "resume",
        "lastest_build_number": "20200524",
        "latest_version": "1.3.1.1",
        "configs": {
            "is_automation_enabled": False,
            "automation": "",
            "ocr_inclusions": "",
            "inclusions": "",
            "is_anonymize": False
        },
        "data_sync_thresholds": {
            "memory": -1,
            "network": -1,
            "cpu": -1,
            "disk_i/o": -1,
            "image_count": 10
        },
        "intervals": {
            "performance": 1,
            "sync": 2,
            "automation": 1,
            "polling": 60000
        },
        "path": {
            "local": "skan\\Log",
            "remote": "/datadrive/data"
        },
        "created_by": "skan-admin",
        "created_on": datetime.datetime.utcnow(),
        "modified_by": "skan-admin",
        "modified_on": datetime.datetime.utcnow(),
        "schema_version": 1
    }
    col.insert_one(default_va_preferences)


def insertDefaultSftpSettings():
    db = conn["general_preferences_db"]
    col = db["sftp_settings"]

    default_sftp_settings = {
        "hostaddress": "cpxnext-gw.skan.ai",
        "username": "rcloneskan",
        "has_private_key": True,
        "password": None,
        "private_key": "",
        "sftp_name": "SFTP_config_for_process_1",
        "created_by": "skan-admin",
        "created_on": datetime.datetime.utcnow(),
        "modified_by": "skan-admin",
        "modified_on": datetime.datetime.utcnow(),
        "schema_version": 1
    }
    col.insert_one(default_sftp_settings)


def insertDefaultPipelinePreferences():
    db = conn["general_preferences_db"]
    col = db["pipeline_preferences"]

    default_sftp_settings = {
        "type": "Lorem",
        "preferences": {
            "activity_rediscovery": {
                "return_with_cleanup": ""
            },
            "gateway_params": {
                "tar_last_modify_time": 100,
                "batch_size_for_read_log": 100,
                "template": {
                    "match_threshold": 0.75,
                    "resize_match_threshold": 0.70
                },
                "masking": {
                    "enable_masking": True,
                    "kernel_size": [0.74]
                }
            },
            "server_params": {
                "process_delivery_schedule": 60,
                "variant_cache_schedule": 60,
                "global_schedule": 60
            }
        },
        "created_by": "skan-admin",
        "created_on": datetime.datetime.utcnow(),
        "modified_by": "skan-admin",
        "modified_on": datetime.datetime.utcnow(),
        "schema_version": 1
    }
    col.insert_one(default_sftp_settings)


insertDefaultAuth()
insertDefaultTeam()
insertDefaultVaPreferences()
insertDefaultSftpSettings()
insertDefaultPipelinePreferences()
