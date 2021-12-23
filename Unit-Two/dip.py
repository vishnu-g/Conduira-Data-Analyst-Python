def exchange(client:FileTransferClient, to_upload:bytes, to_download:str) -> bytes:
    client.upload(to_upload)
    return client.download(to_download)

if __name__ == '__main__':
    ftp = FTPClient('ftp.host.com')
    sftp = FTPSClient('sftp.host.com', 22)
    ftps = SFTPClient('ftps.host.com', 990, 'ftps_user', 'P@ssw0rd1!')
    s3 = S3Client('ftp.host.com')
    scp = SCPClient('ftp.host.com')

    for client in [ftp, sftp, ftps, s3, scp]:
        exchange(client, b'Hello', 'greeting.txt')