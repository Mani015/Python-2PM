# Update():


bikes={100000:'bullet',900000:'apache',160000:'pulsar',120000:'FZ',60000:'TVS Xl super',90000:'splendor'}
print(bikes)
# {100000: 'bullet', 900000: 'apache', 160000: 'pulsar', 120000: 'FZ', 60000: 'TVS Xl super', 90000: 'splendor'}
bikes.update({52000:'mastero'})
print(bikes)
# {100000: 'bullet', 900000: 'apache', 160000: 'pulsar', 120000: 'FZ', 60000: 'TVS Xl super', 90000: 'splendor', 52000: 'mastero'}

bikes.update({120000:'fazer',180000:'R15'})
print(bikes)
# {100000: 'bullet', 900000: 'apache', 160000: 'pulsar', 120000: 'fazer', 60000: 'TVS Xl super', 90000: 'splendor', 52000: 'mastero', 180000: 'R15'}