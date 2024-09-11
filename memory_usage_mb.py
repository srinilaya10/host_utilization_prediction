import psutil
import time
import csv

def bytes_to_mb(bytes):
    return bytes / (1024 ** 2)

def log_memory_usage(interval, duration, output_file):
    end_time = time.time() + duration
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = [
            'timestamp',
            'total_memory_mb',
            'available_memory_mb',
            'used_memory_mb',
            'percent_memory'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        while time.time() < end_time:
            memory_info = psutil.virtual_memory()
            writer.writerow({
                'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
                'total_memory_mb': f"{bytes_to_mb(memory_info.total):.2f}",
                'available_memory_mb': f"{bytes_to_mb(memory_info.available):.2f}",
                'used_memory_mb': f"{bytes_to_mb(memory_info.used):.2f}",
                'percent_memory': f"{memory_info.percent:.2f}"
            })

            time.sleep(interval)

if __name__ == "__main__":
    log_memory_usage(5, 12 * 60 * 60, 'memory_usage.csv')  # Log memory usage every minute for 10 hours


