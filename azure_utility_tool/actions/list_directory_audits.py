"""
Author(s):
    Miguel Alex Cantu (miguel.can2@gmail.com)
Date: 02/21/2020
Description:
    This action will return a dictionary of audit logs for the past day,
    indexed by the UPN of the user who initiated the activity recorded
"""
import datetime

from azure_utility_tool.graph_endpoints import DIRECTORYAUDIT_LIST
from azure_utility_tool.utils import paginate

def list_directory_audits(parsed_args, config, app):
    """
    This action will return a dictionary of audit logs for the past day,
    indexed by the ID of the record.
    """
    audit_entries = []
    date = datetime.datetime.today()
    yesterday = date - datetime.timedelta(days=1)
    paginate(
            DIRECTORYAUDIT_LIST.format(
                yesterday.year,
                yesterday.month,
                yesterday.day),
            audit_entries,
            'value',
            parsed_args,
            config,
            app,
            std_output=False)
    audit_logs = {}
    for entry in audit_entries:
        audit_logs[entry["id"]] = entry
    return audit_logs
