https://play.instruqt.com/embed/redhat/tracks/getting-started-servicenow-automation?token=em_5ktpLJWtzpbqcDyM

~~~
{
  "msg": [
    "INC0013465",
    "Compliance Check Failed sending to Troubleshooting Aproval Node"
  ],
  "_ansible_verbose_always": true,
  "_ansible_no_log": null,
  "changed": false,
  "failed_when_result": true
}
~~~

~~~
{
  "changed": true,
  "commands": [
    "banner login @\nSome new Banner Text\n@"
  ],
  "invocation": {
    "module_args": {
      "text": "Some new Banner Text",
      "banner": "login",
      "multiline_delimiter": "@",
      "state": "present"
    }
~~~




~~~
{
  "changed": true,
  "invocation": {
    "module_args": {
      "name": "Troubleshoot-Approval",
      "workflow_job_id": 41,
      "action": "approve",
      "controller_host": "student23.qc7s7.example.opentlc.com",
      "controller_username": "admin",
      "controller_password": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
      "validate_certs": false,
      "controller_oauthtoken": "",
      "timeout": 10,
      "interval": 1,
      "request_timeout": null,
      "controller_config_file": null
    }
~~~


Closed
~~~
{
  "changed": true,
  "record": {
    "parent": "",
    "made_sla": "true",
    "caused_by": "",
    "watch_list": "",
    "upon_reject": "cancel",
    "sys_updated_on": "2024-02-02 20:03:29",
    "child_incidents": "0",
    "origin_table": "",
    "task_effective_number": "INC0013465",
    "approval_history": "",
    "skills": "",
    "number": "INC0013465",
    "resolved_by": "f04f503e874842505d60da083cbb3591",
    "sys_updated_by": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    "opened_by": "f04f503e874842505d60da083cbb3591",
    "user_input": "",
    "sys_created_on": "2024-02-02 19:52:37",
    "sys_domain": "global",
    "state": "closed",
    "route_reason": "",
    "sys_created_by": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    "knowledge": "false",
    "order": "",
    "calendar_stc": "649",
    "closed_at": "2024-02-02 20:03:29",
    "cmdb_ci": "",
    "contract": "",
    "impact": "low",
    "active": "false",
    "work_notes_list": "",
    "business_service": "",
    "business_impact": "",
    "priority": "5",
    "sys_domain_path": "/",
    "rfc": "",
    "time_worked": "",
    "expected_start": "",
    "opened_at": "2024-02-02 19:52:37",
    "business_duration": "1970-01-01 00:10:49",
    "group_list": "",
    "work_end": "",
    "caller_id": "",
    "reopened_time": "",
    "resolved_at": "2024-02-02 20:03:26",
    "approval_set": "",
    "subcategory": "",
    "work_notes": "",
    "universal_request": "",
    "short_description": "Banner on Rtr CSR 1000v has been updated, marking resolved",
    "close_code": "Solved (Permanently)",
    "correlation_display": "",
~~~
Verify Banner on the Cisco Router
~~~
[student@ansible-1 network-demos-repo]$ ssh rtr1
Warning: Permanently added 'rtr1' (RSA) to the list of known hosts.

Some new Banner Text



rtr1#
~~~