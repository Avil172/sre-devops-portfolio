from pyrundeck import Rundeck

rundeck = Rundeck('https://rundeck.rdnamespace.organization.com',
                  token='1OCQTO1PyT7xSDWfri7SmSrd1inJFzU2',
                 )

RUNDECK_JOB_ID='3c14cec5-dfd6-447d-b316-ff3dc4fba862'
run = rundeck.run_job(RUNDECK_JOB_ID, options={'LANDSCAPE': 'dev02'})

running_jobs = rundeck.get_executions_for_job(job_id=RUNDECK_JOB_ID, status='running')

for job in running_jobs['executions']:
  print("%s is running" % job['id'])
