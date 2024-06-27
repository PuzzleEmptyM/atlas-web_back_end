import kue from 'kue';
import assert from 'assert';
import sinon from 'sinon';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', function() {
  let queue;
  let consoleSpy;

  beforeEach(function() {
    queue = kue.createQueue();
    queue.testMode.enter();
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(function() {
    queue.testMode.clear();
    queue.testMode.exit();
    consoleSpy.restore();
  });

  it('should display an error message if jobs is not an array', function() {
    assert.throws(() => createPushNotificationsJobs('not an array', queue), Error, 'Jobs is not an array');
  });

  it('should create two new jobs to the queue', function(done) {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    // Trigger the enqueue event manually for test mode
    queue.testMode.jobs.forEach(job => {
      job.emit('enqueue');
    });

    setImmediate(() => {
      try {
        assert.equal(queue.testMode.jobs.length, 2);

        const job1 = queue.testMode.jobs[0];
        const job2 = queue.testMode.jobs[1];

        assert.equal(job1.type, 'push_notification_code_3');
        assert.equal(job1.data.phoneNumber, '4153518780');
        assert.equal(job1.data.message, 'This is the code 1234 to verify your account');
        assert(consoleSpy.calledWith(`Notification job created: ${job1.id}`), `Expected log: Notification job created: ${job1.id}, but got: ${consoleSpy.args}`);

        assert.equal(job2.type, 'push_notification_code_3');
        assert.equal(job2.data.phoneNumber, '4153518781');
        assert.equal(job2.data.message, 'This is the code 4562 to verify your account');
        assert(consoleSpy.calledWith(`Notification job created: ${job2.id}`), `Expected log: Notification job created: ${job2.id}, but got: ${consoleSpy.args}`);

        done();
      } catch (error) {
        done(error);
      }
    });
  });
});
