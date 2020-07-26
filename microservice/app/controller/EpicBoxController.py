import epicbox

epicbox.configure(
    profiles=[
        epicbox.Profile('python', 'python:3.6.5-alpine')
    ]
)


class ResponseWrapper:
    def __init__(self, exit_code: int, stdout: bytes, stderr: bytes, duration: float, timeout: bool,
                 oom_killed: bool):
        self.exit_code = exit_code
        self.output: str = stdout.decode("ascii")
        self.stderr: bytes = stderr.decode("ascii")
        self.duration: bytes = duration
        self.timeout: float = timeout
        self.oom_killed: bool = oom_killed


def getProcessResponse(content: bytes):
    files = [{'name': 'main.py', 'content': content}]
    limits = {'cputime': 1, 'memory': 64}
    result = epicbox.run('python', 'python3 main.py', files=files, limits=limits)
    return ResponseWrapper(**result)
