import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='**',username='**',password='**',port='**')
sftp_client=ssh.open_sftp()


sftp_client.put('Taşınacak dosyanın yolu', 'taşınacak yer')
sftp_client.close()
ssh.close()


