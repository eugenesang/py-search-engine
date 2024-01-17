const { readFileSync, writeFile } = require('fs');

function cleanJob(job) {
    const { _id, createdAt } = job;

    const fieldsToDelete = [
        'images', 'documents', 'likes', 'summarized', 'postedBy', '__v', 'updatedAt'
    ]

    for (let field of fieldsToDelete) {
        delete (job[field])
    }

    return {
        ...job, _id: _id.$oid, createdAt: createdAt.$date
    }
}

const data = JSON.parse(readFileSync('../raw-data/jobs.json', {
    encoding: 'utf-8'
})).map(job => cleanJob(job));

writeFile('../raw-data/cleanJobs.json', JSON.stringify(data, null, 4), { encoding: 'utf-8' }, (error) => {
    if (error) {
        console.error(error);
    }
})