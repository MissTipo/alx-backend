import kue from 'kue';
const push_notification_code = kue.createQueue({
  redis: {
    host: 'localhost',
    port: '6479'
  }
});
const obj = { phoneNumber: '12343', message: 'hello World' }
const job = push_notification_code.create('push_notification_code', obj).save((err) => {
  if (err) {
    console.log('Notification job failed', err);
  } else {
    console.log('Notification job created:', job.id)

    job.on('complete', () => {
      queue.shutdown()(500, (err) => {
        console.log('Kue shutdown:', err || 'completed')
        process.exit(0);
      });
    });

    job.on('failed', () => {
      queue.shutdown()(500, (err) => {
        console.log('Kue shutdown:', err || 'completed')
        process.exit(1)
      });
    })
  }
});

