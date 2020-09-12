import requests
import sys

link = "https://vidstreaming.io/goto.php?url=aHR0cHM6LyAdeqwrwedffryretgsdFrsftrsvfsfsr9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL2Zlc3RpdmUtYXZlbnVlLTI4ODgwMS9VSkU4WU9fNlpUUlMvMjNhXzE1OTk3NTkzOTgxNDQ3OTcubXA0"
file_name = "download.mp4"
with open(file_name, "wb") as f:
        print("Downloading %s" % file_name)
        response = requests.get(link, stream=True,allow_redirects=True)
        total_length = response.headers.get('content-length')

        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=100000):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('█' * done, ' ' * (50-done)) )    
                sys.stdout.flush()
