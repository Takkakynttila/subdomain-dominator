import requests as rq

data = open('subdomains.lst') #read a list of subdomains for brute forcing
subdomains = data.readlines()

subdomains_cleaned = []

for line in subdomains: # clean of row-changes
    text = line.split('\n')
    subdomains_cleaned.append(text[0])
print(len(subdomains_cleaned))

print('I\'m your friendly neighbourhood subdomain scanner!\n Please insert a domain you\'d like to scan!') #text ui
domain = input('>>>')
discovered_subdomains = []
prog_bar = "[]" #trying to create a progress bar with meager results

counter = 0
for subdomain in subdomains_cleaned:
    counter += 1
    if counter % 100 == 0:
        print(prog_bar)
        prog_bar += '[]'
    url = f"http://{subdomain}.{domain}" #parse url
    try:
        rq.get(url)
    except rq.ConnectionError: #if connection error, no subdomain and pass
        pass
    else:
        print('>>> Subdomain discovered!: ' + url) #else print subdomain and append to list
        discovered_subdomains.append(url)
print(discovered_subdomains)
        
