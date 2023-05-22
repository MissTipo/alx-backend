import redis from 'redis';
const client = redis.createClient(6479);


client.on('connect', () => {
  console.log('Redis client connected');
});
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});
client.quit();
