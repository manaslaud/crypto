import hmac
import hashlib
import time
def generate_mac(algorithm, key: bytes, message: bytes) -> str:
    return hmac.new(key, message, algorithm).hexdigest()
def measure_time(algorithm, key, message):
    start_time = time.time()
    mac = generate_mac(algorithm, key, message)
    end_time = time.time()
    return mac, end_time - start_time
key = b'secret_key'
message_sizes = [100, 500, 1000, 5000, 10000]
algorithms = {'SHA-1': hashlib.sha1, 'SHA-256': hashlib.sha256}
for algo_name, algo_func in algorithms.items():
    print(f"\n{algo_name} MAC Time Measurements:")
    for size in message_sizes:
        message = b'A' * size
        mac, time_taken = measure_time(algo_func, key, message)
        print(f"Message Size: {size} bytes, Time: {time_taken:.6f} sec")