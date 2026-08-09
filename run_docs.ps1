Start-Job {
    Start-Sleep -Seconds 1
    Start-Process "http://127.0.0.1:8000/"
} | Out-Null

.\.venv-docs\Scripts\python.exe -m mkdocs serve