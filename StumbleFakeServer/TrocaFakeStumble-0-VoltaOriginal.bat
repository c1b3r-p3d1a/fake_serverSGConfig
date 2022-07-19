if exist C:\Windows\System32\drivers\etc\hosts.original (
	del C:\Windows\System32\drivers\etc\hosts
	copy C:\Windows\System32\drivers\etc\hosts.original C:\Windows\System32\drivers\etc\hosts
)

ipconfig /flushdns