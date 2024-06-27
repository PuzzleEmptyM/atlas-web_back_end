function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobInfo) => {
    const newJob = queue.create('push_notification_code_3', jobInfo);

    newJob
      .on('enqueue', () => {
        console.log(`Notification job created: ${newJob.id}`);
      })
      .on('complete', () => {
        console.log(`Notification job ${newJob.id} completed`);
      })
      .on('failed', (error) => {
        console.log(`Notification job ${newJob.id} failed: ${error}`);
      })
      .on('progress', (progress) => {
        console.log(`Notification job ${newJob.id} ${progress}% complete`);
      });
    newJob.save();
  });
}

export default createPushNotificationsJobs;
