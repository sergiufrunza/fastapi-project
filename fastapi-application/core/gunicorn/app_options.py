from .logger import GunicornLoger


def get_app_options(
        host: str,
        port: int,
        workers: int,
        timeout: int,
        loglevel: str,

) -> dict:
    return {
        "accesslog": "-",
        "errorlog": "-",
        "loglevel": loglevel,
        "logger_class": GunicornLoger,
        "bind": f"{host}:{port}",
        "workers": workers,
        "timeout": timeout,
        "worker_class": "uvicorn.workers.UvicornWorker",
    }