import redis from 'redis';
const client = redis.createClient(6479);


client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print)
}
function displaySchoolValue(schoolName) {
  client.get(schoolName, redis.print)
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
client.quit();
