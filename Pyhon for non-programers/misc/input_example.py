dateacenter_list = ['NYC', 'SFO', 'LON', 'AMS', 'TOR', 'SGP', ]
hostname_list = ['timmy', 'bobby', 'sally', 'jimmy', 'lucy', 'linda']
name = input('What is your name?').title()
datacenter = input('What datacenere do you want to work on?').upper()
hostname = input('What is the hostname you would like to reach?')

if datacenter in dateacenter_list and hostname in hostname_list:
    print(f' Great work {name}, you are now connected to {hostname} in {datacenter} datacenter!')
elif datacenter in dateacenter_list and hostname not in hostname_list:
        print(f'Sorry {name}, the hostname {hostname} is not recognized. Please try again.')
elif datacenter not in dateacenter_list and hostname in hostname_list:
        print(f'Sorry {name}, the datacenter {datacenter} is not recognized. Please try again.')
else:
    print(f'Sorry {name}, the datacenter {datacenter} or {hostname} is not recognized. Please try again.')   