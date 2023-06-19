import redis

# Connect to Redis
redis_client = redis.Redis()

# Function to fetch data from cache or source
def get_data(key):
    # Check if the data is already cached
    cached_data = redis_client.get(key)
    
    if cached_data is not None:
        # Data exists in cache, return it
        print("Retrieving data from cache...")
        return cached_data.decode()
    else:
        # Data doesn't exist in cache, fetch it from the source
        print("Fetching data from the source...")
        # Simulating the source data retrieval
        source_data = "Data from the source"
        
        # Store the data in cache for future use
        redis_client.set(key, source_data)
        # Set an expiration time for the cached data (e.g., 1 hour)
        redis_client.expire(key, 3600)
        
        return source_data

# Example usage
data_1 = get_data("key_1")
print(data_1)

data_2 = get_data("key_2")
print(data_2)

# Fetching the same data again
data_1_cached = get_data("key_1")
print(data_1_cached)
