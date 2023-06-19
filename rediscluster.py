from rediscluster import RedisCluster

startup_nodes = [
    {"host": "127.0.0.1", "port": "7000"},
    {"host": "127.0.0.1", "port": "7001"},
    {"host": "127.0.0.1", "port": "7002"}
]
redis_cluster = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

# Set a key-value pair
redis_cluster.set("mykey", "myvalue")

# Get the value for a key
value = redis_cluster.get("mykey")
print(value)

# Increment a counter
redis_cluster.incr("counter")

# Perform a multi-key operation using pipelines
pipeline = redis_cluster.pipeline()
pipeline.set("key1", "value1")
pipeline.set("key2", "value2")
pipeline.get("key1")
pipeline.get("key2")
results = pipeline.execute()
print(results)

# Delete a key
redis_cluster.delete("mykey")
