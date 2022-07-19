if not exist C:\Windows\System32\drivers\etc\hosts.original (
	copy C:\Windows\System32\drivers\etc\hosts C:\Windows\System32\drivers\etc\hosts.original
)
del C:\Windows\System32\drivers\etc\hosts
cd /d "%~dp0"
copy hosts.stumble3TorneiosAmigos C:\Windows\System32\drivers\etc\hosts

ipconfig /flushdns