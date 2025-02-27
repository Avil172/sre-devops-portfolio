import json
import requests
from pyrundeck import Rundeck

rundeck_url = 'https://rundeck.rdnamespace.organization.com'
rundeck = Rundeck('https://rundeck.rdnamespace.organization.com',
              token='1OCQTO1PyT7xSDWfri7SmSrd1inJFzU2',
                 )

def checkbundles(host):
    RUNDECK_JOB_ID='b9cea68d-16f6-441d-b09b-8e6ed3237e39'
    run = rundeck.run_job(RUNDECK_JOB_ID, options={'Nodes': host})

    running_jobs = rundeck.get_executions_for_job(job_id=RUNDECK_JOB_ID, status='running')

    for job in running_jobs['executions']:
        job_id=job['id']
        return(f"{statuscheck(job_id)}\n{rundeck_url}/execution/show/{job_id}")

def systemcheck(host):
    RUNDECK_JOB_ID='b88f60d3-9c31-4bb1-a963-afc0e65cf89a'
    run = rundeck.run_job(RUNDECK_JOB_ID, options={'Nodes': host})

    running_jobs = rundeck.get_executions_for_job(job_id=RUNDECK_JOB_ID, status='running')

    for job in running_jobs['executions']:
        job_id=job['id']
        return(f"{statuscheck(job_id)}\n{rundeck_url}/execution/show/{job_id}")

def putinservice(host):
    RUNDECK_JOB_ID='8ecb16c1-0948-482b-bfcf-3eb7607e40a9'
    run = rundeck.run_job(RUNDECK_JOB_ID, options={'put_in_service': 'Yes', 'Nodes': host})

    running_jobs = rundeck.get_executions_for_job(job_id=RUNDECK_JOB_ID, status='running')

    for job in running_jobs['executions']:
        job_id=job['id']
        return(f"{statuscheck(job_id)}\n{rundeck_url}/execution/show/{job_id}")

def restart(host):
    RUNDECK_JOB_ID='8ecb16c1-0948-482b-bfcf-3eb7607e40a9'
    run = rundeck.run_job(RUNDECK_JOB_ID, options={'restart_service': 'Yes', 'Nodes': host})

    running_jobs = rundeck.get_executions_for_job(job_id=RUNDECK_JOB_ID, status='running')

    for job in running_jobs['executions']:
        job_id=job['id']
        return(f"{statuscheck(job_id)}\n{rundeck_url}/execution/show/{job_id}")

def statuscheck(jobid):
    r=requests.get(f"{rundeck_url}/api/11/execution/{jobid}/state?authtoken=1OCQTO1PyT7xSDWfri7SmSrd1inJFzU2", headers={"Accept": "application/json"})
    x=r.content.decode("utf-8")
    z=json.loads(x)
    y=z['executionState']
    return(f"job is {y}")
