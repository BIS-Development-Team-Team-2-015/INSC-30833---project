#Exports data to txt file for broker
    def exportData(self):
        self.writeIT(
            str(self.clientName.get()),
            str(self.clientEmail.get()),
            str(self.clientPhone.get()),
            str(self.departDate.get()),
            str(self.departAirport.get()),
            str(self.destinationAirport.get()),
            str(self.passengerNum.get()),
            str(self.flightPrice.get()))

        export = Tk()
        export.title('Quote Inquiry')
        Label(export, text = 'Thank you for your inquiry. A broker will be reaching out shortly.', font=("Times", 30)).grid(row = 2, column = 2, sticky = W)
        export.mainloop()

    def writeIT(self, clientName, clientEmail, clientPhone, departDate, departAirport, destinationAirport, passengerNum, flightPrice):
        file = open('Quote Inquiry.txt', 'a+')
        file.write( '\n' + 'Client Name' +  ' ' + clientName + '\n' +
        'Email' + ' ' + clientEmail + '\n' +
        'Phone' + ' ' + clientPhone + '\n' +
        'Date' + ' ' + departDate + '\n' +
        'Departure Airport' + ' ' + departAirport + '\n' +
        'Destination Airport' + ' ' + destinationAirport + '\n' +
        'Number of Passengers' + ' ' + passengerNum + '\n' +
        'Quoted Flight Price' + ' ' + flightPrice + '\n')
        file.close()