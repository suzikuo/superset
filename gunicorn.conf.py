import multiprocessing

workers = 2 * multiprocessing.cpu_count() + 1
worker_class = "gevent"
worker_connections = 1000
timeout = 120
bind = "0.0.0.0:8088"
limit_request_line = 0
limit_request_field_size = 0
statsd_host = "localhost:8125"
preload_app = True

