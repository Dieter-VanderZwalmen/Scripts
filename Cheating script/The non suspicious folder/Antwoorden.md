
### 1. Create a oneliner which shows the amount of currently revoked certificates in the Terena SSL CA revocation list. Do not create temporary files. The CRL can be found at http://crl.tcs.terena.org/TERENASSLCA.crl.

### Tip: '-' (no quotes) specified as a filename means STDOUT. The answer should be more or less 4960

```sh
curl http://crl.3.digicert.com/TERENASSLCA3.crl | openssl crl -inform DER -text -noout | grep 'Revocation Date' | wc –l
```
~~
### 2. Your very curious it-enabled grandmother likes to see how you solved some of the lab exercises on leia. She gave you her public key id_rsa.pub. Which command allows her to login to your ssh account without entering credentials?

- 1) Copy the content of your it-enabled grandmothers id_rsa.pub file in your ~/.ssh/authorized_keys file.

- 2) Let your grandmother log in with the following command

```sh
ssh user@leia.uclllabs.be -p 22345 -i "/path/to/your grandmothers identity_file"
```
~~
### 3. Create a onliner which sends one icmp echo packet to 127.0.0.1 for every pdf downloaded from the following folder: /documenten/echo/08-09/. The required info can be found in the apache logfile: apache_google.log. The output from your command should look like this (nothing else): 

```

64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.044 ms  
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.037 ms  
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.035 ms 
... 
64 bytes from 127.0.0.1: icmp_seq=29 ttl=64 time=0.057 ms

```

```
ping -c $(grep -P '/documenten/echo/08-09/.*\.pdf' | wc -l) 127.0.0.1
```


~~
### 4. Create a oneliner which lists the top 3 most used passwords in the ftp brute force attack captured in ftp_bruteforce.pcap. Use a suitable sniffer filter which only displays whats really needed to get the output below

```sh
tshark -r Cnw2_ftp_bruteforce.pcap -Y "ftp.request.command==PASS" -T fields -e ftp.request.arg | sort | uniq -c | sort -rn | head -3 | awk '{print $2}'
```
~~
### 5. Perform a network capture while surfing to http://debbie.vlan77.be/nw2/test.html. Write a wireshark filter that will show only HTTP POST requests to the server debbie. Filter out any other traffic, also from other servers or clients

```sh

1) tshark -r filename -Y "http.request.method == POST"
2) (Upload .pcap of .pcapng met een HTTP post naar leia)
3) tshark -r filename -Y "http.request.method == POST"

```
~~
### 6. Try to find out which TCP ports are open on debbie without being logged in to the server itself. Use your virtual machine. Try to determine which services are running on these ports, but don't scan too fast because the allmighty KHLeuven firewall might detect that you are up to something evil and block your IP or even kick you off the network.

```sh
nc -zv -w 1 leia.uclllabs.be 1-65535 2>&1 |grep -v refused | awk '{print $4}'
```

### On server debbie, use the list of logged in users to print only the username that has been logged in to the server for the longest time. (Hint: use “perl -ne”

```sh
who | awk '{print $3 “ “ $4 " " $1}' | sort -n | awk '{print $3}' | head –1 
```
~~
### 8. It is always a good idea to make (secure) backups of your data and store them on a different location. Use 'tar' to compress the contents of your entire home directory on leia, encrypt the result with openssl and send the output file to your windows computer. Choose a strong encryption algorithm. (Use 2 one-liners, one on leia and one on windows) 

```sh
Tar -cvf backupfile /home/LDAP/r-nr   

Tar -cvf output(backup) input(data) | openssl enc -des(encrypty algoritme) -in file(backup) -out file(encbackup)
```
~~
### 9. On server leia, list all TCP ports on which a daemon is currently listening for connections. Only show the ports you can connect to using IPv4. Also hide all port numbers that have one or more repeating digits.

```sh
netstat -lt4n | awk '{print $4}' | grep :.* | sed 's/.*://' | sed -e '/\(.\).*\1/d'
```
~~
### 10. An ftp brute force attack was captured using wireshark in the following file: ftp_bruteforce.pcap. You want to know if the attack was successful, i.e. if the attacker found a working username and password combination. Use a suitable tshark oneliner to display all possible successful login attempts in the following format:

```

USER    bob
PASS    verysecure

```

```sh

echo "USER" $(tshark -r Cnw2_ftp_bruteforce.pcap  -Y "tcp.srcport== 
$(tshark -r Cnw2_ftp_bruteforce.pcap -Y "ftp.response.code==230" -T fields -e "tcp.dstport")
and ftp.request.command==USER" -T fields -e ftp.request.arg) &&  echo "PASS" $(tshark -r Cnw2_ftp_bruteforce.pcap  -Y "tcp.srcport== 
$(tshark -r Cnw2_ftp_bruteforce.pcap -Y "ftp.response.code==230" -T fields -e "tcp.dstport")
and ftp.request.command==PASS" -T fields -e ftp.request.arg)


```

~~
### 11. Companies like Google and Microsoft make heavily use of the X.509 subjectAltName extension. KHLeuven also uses this extension to add an alternative name *.khleuven.be to the common name (khleuven.be) of the cerificate. Create a oneliner which calculates the amount of DNS Subject Alternate Names used in the SSL certificate of gmail.be

```sh

echo | openssl s_client -connect www.gmail.com:443 2>/dev/null | openssl x509 -text -noout | grep -o 'DNS:' | wc -l

```
~~
### 12. Create a oneliner which lists all palindromes with exactly 4 letters in a dictionary.

```sh

cat dutch | grep -P '^(.)(.)\2\1$'

```
~~
### 13.  Show the permissions of only your homedirectory, without using any pipes. The solution must be generic: It should work from any location and without specifying your exact username

```sh
ls –ld /home
```
~~
### 14.  Bob needs to send a text file through an encrypted tunnel to Alice. Both already agreed on a shared secret 'mysecret' using the Diffie Hellman algorithm. Alice wants to display the contents of the file directly on her screen in stead of storing it locally and then opening it. Use a suitable encryption algorithm. The data is sent over a medium which only allows ASCII text.Alice is logged in on debbie and Bob on the virtual machine.

```sh

Alice@leia ~ $nc -l 10000 | openssl enc -a -d   -aes-128-cbc -k pass:secret

Bob@laptop ~ $cat file | openssl enc -a -aes-128-cbc -k pass:secret | nc leia 10000

```
~~
### 15. Some subdirectory of /tmp contains a bunch of movies. However their extension is wrong. The extension should be .avi in stead of .jpg. Copy these files to your homedirectory and correct their extensions in one line. (tip: basename)

- 1) cd /tmp
- 2) cp -r movies ~
- 3) cd 
- 4) cd movies
- 5) for f in *.jpg; do mv "$f" "$(basename "$f" .jpg).avi"; done
~~
### 16. Create a onliner which relies on the command ping to do a fully automatic icmp traceroute. Limit the amount of hops to 10. The output should look like this:

```
193.191.187.62 khleuven-vrrp.access.leuven.belnet.net ... 209.85.250.163 wi-in-f94.1e100.net 
```

```sh
traceroute -I www.facebook.be -m 10
```
~~
### 17. A simulated phone is running at http://darthvader.uclllabs.be/nw2/phone/. Create a oneliner to bruteforce the pincode. Tip: pincode range: 1200-1300. 

```sh
for i in {1200..1300}; do if wget -q   http://darthvader.uclllabs.be/nw2/phone/ --http-user=admin --http-password=$i; then echo $i; break; fi;done;
```
~~
### 18. You just received your pem encoded certificate from you CA. Now you have 2 files: cert.pem en cert.key. Use the command chmodto set the appropriate permissions.

```sh
chmod 600 cert.key;  chmod 644 cert.pem
```
~~
### 19. Create a linux CLI oneliner to extract the DNS servers and their destination ports of the DNS replies in the sip_dump.pcap file. (gebruik vervanging)

```
tshark -r vervanging.pcap -Y "dns" -T fields -e ip.src -e udp.dstport | sort -n | uniq
```
~~
### 20. Ontcijfer de volgende boodschap: RGUgcHVudGVuIG9wIGRlemUgdnJhYWcgemlqbiBhbCBiaW5uZW4uCg== (deze boodschap staat in het bestand /home/logs/secret

```sh
cat /home/logs/secret | echo ' RGUgcHVudGVuIG9wIGRlemUgdnJhYWcgemlqbiBhbCBiaW5uZW4uCg== ' | openssl enc -a –d
```
~~
### 21. What linux command with options should be used to perform a scan to the server debbie.vlan77.be with the following requirements: Use only the IP address of the server Don’t randomize the scanned ports  List only open TCP ports

```sh
nmap 193.191.177.1
```
~~
### 22. Create a CLI oneliner using openssl to retrieve the certificate of the server facebook.com and to display only it’s fingerprint and public key

```sh

echo | openssl s_client -connect wiki.uclllabs.be:443 2>/dev/null | openssl x509 -fingerprint -serial -pubkey  -noout

echo | openssl s_client -connect www.facebook.com:443 2>/dev/null | openssl x509 -noout -fingerprint -serial -pubkey

```
~~
### 23. As a web server administrator you have been asked to give your manager a linux CLI oneliner to extract the 5 IP adresses that contacted the web server the most. The apache log is located in /home/log. Create a correct oneliner. The output should look something like this: (count IPs)  

```sh

cat /home/logs/apache_google.log | awk '{print$1}' | sort | uniq -c | sort -rn | head -5 

```
~~
### 24. Create a linux CLI oneliner to extract the source ports of the DNS requests in the sip_dump.pcap file. (vervanging.pcap)

```sh

tshark -r vervanging.pcap -Y "dns" -T fields -e udp.dstport | sort -n | uniq | sort -n 

```
~~
### 25. Create a linux CLI oneliner to download and decode the encoded file “encoded.text” on http://debbie.vlan77.be/nw2/encoded

```sh
wget -q -O - http://debbie.vlan77.be/nw2/encoded | base64 -d (dit is maar een probeersel)
```
~~
### 26. What linux command with options should be used to perform a scan to the server debbie.vlan77.be with the following requirements:Work in progressTCP connect scan Service scan (banner grabbing)

```sh
nmap -sV --script=banner 193.191.177.1 (script ding is google werk... verwacht dit niet op het examen)
```
~~
### 28.  Create a linux CLI oneliner to extract an overview of the different FTP usernames in the file ftp_bruteforce.pcap.

```sh
tshark -r Cnw2_ftp_bruteforce.pcap -Y "ftp.request.command == USER" -T fields -e ftp.request.arg | sort| uniq
```
~~
### 29.  Create a oneliner to show ‘Time = 15:44:25 (11/10/1901)’ with the current time and date. 

```sh
echo "Time = $(date '+%X (%x)')"
```
~~
### 30. Create a CLI oneliner to match all words with 14, 15 and 16 unique letters. The output shoud look like: 

```
Words with 14 letters: bedrijfsomvang ... Words with 15 letters: ... 
```

```sh
for foo in 14 15 16; do echo "Words with $foo letters:" $(grep -vP '(.).*\1' /usr/share/dict/dutch | grep -P "^.{$foo}$");done
```

~~
### 31. What linux command with options should be used to perform a scan with the following requirements: Scan all systems in 193.191.187.12/25 Exclude 192.191.187.1 and 192.191.187.2 

```
nmap 193.191.177.1-61 --exclude 193.191.177.37,193.191.177.40
```
~~
### 32. Create a CLI oneliner using openssl to retrieve the certificate of the server www.facebook.be and to encrypt the text “CNW2 RULES” with it’s public key. 

- Tekst moet CNW2 RULES zijn

```sh

# Encrypt:

echo set key | openssl s_client -connect www.facebook.be:443 2>/dev/null | openssl x509 -pubkey -noout | echo "CNW2 RULES"| head -3| tail -2 | openssl enc -des -k key -out text

# Decrypt 

echo set key | openssl s_client -connect www.facebook.be:443 2>/dev/null | openssl x509 -pubkey -noout | echo "CNW2 RULES"| head -3| tail -2 | openssl enc -d   -des -k key -in text

echo | openssl s_client -connect wiki.anuclllabs.be:443 2>/dev/null | openssl x509 -noout -pubkey > public.pem

echo "Let's make CNW2 great again" | openssl rsautl -encrypt -pubin -inkey public.pem -out CNW2.encrypted

```
~~
### 33. Create a CLI oneliner to find a match between different rsa private key files and their companion crt files. The output should look something like: 

alfa.key matches to beta.crt 

```sh

# (eerste een paar genereren)

openssl req -x509 -sha256 -newkey rsa:2048 -keyout tombola_uclllabs_be.key -out tombola_uclllabs_be.crt -days 365 -nodes -subj "/C=BE/ST=/L=/O=UC Leuven/CN=tombola.uclllabs.be"

for key in $(ls -1 *.key); do for crt in $(ls -1 *.crt); do if [[ $(openssl rsa -in $key -noout -modulus | md5sum) == $(openssl x509 -in $crt -noout -modulus | md5sum) ]]; then echo $key matches $crt;fi ;done;done

for key in $(ls *.key); do for cert in $(ls *.pem); do [[ $(openssl rsa -in $key -noout -modulus | md5sum) == $(openssl x509 -in $cert -noout -modulus | md5sum) ]] && echo $key matches to $cert;done;done

```
~~
### 34.  Create a linux CLI oneliner to extract the top 3 SIP methods in sip_dump.pcap.

```sh
tshark –r sip_dump.pcap  -Y “ftp” -T fields –e sip.request.method == SIP | sort | uniq –c | sort –rn | head –3 | awk ‘{print$2}’
```
~~
### 37.  What Linux ssh command do you use to bind your local port 3000 to a web server on port 4444 on the network of the ssh server.

```sh
ssh -p 22345 username@leia.uclllabs.be -L 3000:IP_web_server:4444
```
~~
### 38.  Create a regular expression to match all words in a dictionary with 5 unique letters. 

```sh
cat /usr/share/dict/dutch | grep -P '^[a-zA-Z]{5}$'| grep -vP '(.).*\1'
```
~~
### 39. Use tshark to create an overview and an amount of the different response codes of FTP in the file ftp_bruteforece.pcap.

```sh
tshark -r Cnw2_ftp_bruteforce.pcap -Y "ftp.response.code" -T fields -e ftp.response.code | sort | uniq -c 
```
~~
40
Create a CLI oneliner to match all words with 14, 15 or 16 unique letters. The output should
look like:
for foo in 14 15 16; do echo "Words with $foo letters:" $(grep -vP '(.).*\1' /usr/share/dict/
dutch | grep -P "^.{$foo}$");done
~~
41
Create a linux CLI oneliner to extract an overview of the different FTP usernames in the file
ftp_bruteforce.pcap. Only the commands tshark and sort are allowed.
tshark -r ftp_bruteforce.pcap -Y 'ftp.request.command == USER' -T fields -e ftp.request.arg |
sort -u
~~
43
Create a oneliner to show ‘Time = 15:44:25 (11/10/1901)' or 'Time = 15:44:25 (11-10-
1901)’ each time with the current time and date
date '+Time = %X (%x)'
~~
44
Create a linux CLI oneliner to decode the following string
‘RGUgcHVudGVuIG9wIGRlemUgdnJhYWcgemlqbiBhbCBiaW5uZW4uCg==’. (/home/logs/secret)
cat /home/logs/secret | openssl enc -a -d
~~
45
Create a CLI oneliner using openssl to retrieve the certificate of the server wiki.uclllabs.be
and to display only it’s fingerprint, serial and public key.
echo | openssl s_client -connect wiki.uclllabs.be:443 2>/dev/null | openssl x509 -noout -fingerprint -serial -pubkey


