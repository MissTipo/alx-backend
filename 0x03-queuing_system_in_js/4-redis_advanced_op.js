import redis from 'redis';
const client = redis.createClient(6479);


client.on('connect', () => {
  console.log('Redis client connected');
});
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.hset('HolbertonSchools', 'portland', '50', redis.print);
client.hset('HolbertonSchools', 'Seattle', '80', redis.print);
client.hset('HolbertonSchools', 'New York', '20', redis.print);
client.hset('HolbertonSchools', 'Bogota', '20', redis.print);
client.hset('HolbertonSchools', 'Cali', '40', redis.print);
client.hset('HolbertonSchools', 'Paris', '2', redis.print);

client.hgetall('HolbertonSchools', (err, value) => {
  if (err) throw err;
  console.log(value);
});

client.quit();
