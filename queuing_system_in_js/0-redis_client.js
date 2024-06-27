import redis from 'redis';

console.log('Starting Redis client...');

const client = redis.createClient({
  host: '127.0.0.1',
  port: 6379
});

client.on('ready', () => {
  console.log('Redis client ready to use');
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('reconnecting', () => {
  console.log('Redis client reconnecting to the server');
});

client.on('end', () => {
  console.log('Redis client connection closed');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

process.stdin.resume();
