from functions.search_jobs import search_job

job_search_results = search_job('book review')

for job in job_search_results:
    print(job)