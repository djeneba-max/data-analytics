sales_data = [
('Marcus Webb', 'East', 4250.00),
('Priya Sharma', 'West', 5875.50),
('DeShawn Carter', 'East', 3100.75),
('LaTonya Rivers', 'South', 6420.00),
('Bob Nguyen', 'West', 4980.25),
]

for record in sales_data: 
    print(f'{record[0]} ({record[1]}): ${record[2]:.2f}')
      
    if record[2] > 5000:
        print('^ Top performer!')
        
# or
#for name, region, sales in sales_data:
    #print(f'{name} ({region}): ${sales:,.2f}')