class Parking():
    def __init__(self, tickets = [], parkingSpaces = [], currentTicket = {'paid': 'true'}):
        self.tickets = tickets
        self.tickets = ['ticket' for i in range(250)]
        self.parkingSpaces = parkingSpaces
        self.parkingSpaces = ['space' for i in range(250)]
        self.currentTicket = currentTicket

    def takeTicket(self):
        self.tickets.pop()
        self.parkingSpaces.pop()
        self.currentTicket['paid'] = 'false'
        print(f'There are now {len(self.tickets)} tickets and {len(self.parkingSpaces)} parking spaces remaining')
    
    def payForParking(self, leave = ''):
        self.leave = leave
        while True:
            if self.currentTicket['paid'] == 'false':
                paid = str(input('Please input "$20" to pay for your parking.'))
                if paid == '$20':
                    self.currentTicket['paid'] = 'true'
                    self.tickets.append('ticket')
                    self.parkingSpaces.append('space')
                    # print(f'There are now {len(self.tickets)} tickets and {len(self.parkingSpaces)} parking spaces remaining')
                    print('Your ticket has been paid and you have 15 min to leave.')
                    break
                else: 
                    print('You have input a different value than is needed. Please try again.')
    
    def leaveGarage(self):
        if self.currentTicket['paid'] != 'true':
            print('You must pay for your ticket before leaving the garage')
            while True:
                if self.currentTicket['paid'] == 'false':
                    paid = str(input('Please input "$20" to pay for your parking.'))
                    if paid == '$20':
                        self.currentTicket['paid'] = 'true'
                        self.tickets.append('ticket')
                        self.parkingSpaces.append('space')
                        # print(f'There are now {len(self.tickets)} tickets and {len(self.parkingSpaces)} parking spaces remaining')
                        print('Thank you have a nice day!')
                        break
                    else: 
                        print('You have input a different value than is needed. Please try again.')
        else:
            print('Have a nice day!')    

# matt_parking = Parking()
# print(len(matt_parking.parkingSpaces))
# print(len(matt_parking.tickets))

# matt_parking.takeTicket()
# print(len(matt_parking.parkingSpaces))
# print(len(matt_parking.tickets))


# matt_parking.leaveGarage()
