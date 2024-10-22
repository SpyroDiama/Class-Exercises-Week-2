#ask the user an amount of an invoice 
#ask the user about the VAT percentage
#calculate the invoice with the VAT included
#print the total payment 


invoice = int(input("Type The Invoice Ammount:"))  #Random invoice number from user input

vat = int(input("Type The VAT Ammount:"))/100      #Random vat amount from user input 

total_ammount = invoice + invoice * vat            #Invoice + invoice with the vat multiplication 

print("Total Payment After VAT Is:", total_ammount)  #Show the total ammount to the user 




 


