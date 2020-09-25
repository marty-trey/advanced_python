#  list of dicts
stocks = [
    {
        "name": "TMUS",
        "closing": "200.00",
        "date": "2020-12-30",
    },
    {
        "name": "TMUS",
        "closing": "220.00",
        "date": "2020-12-31",
    },
    {
        "name": "MSFT",
        "closing": "100.00",
        "date": "2020-12-30",
    },
    {
        "name": "MSFT",
        "closing": "110.00",
        "date": "2020-12-31",
    }
]


# TODO CONVERT THE ABOVE TO THE BELOW
output_dict = {}  # Create empty dictionary to hold out output
for s in stocks:  # Loop through all the stocks in the list
    print(s)
    name = s["name"]
    del s['name']
    if name not in output_dict:
        output_dict[name]=[]
    output_dict[name].append(s)

    
#    del s["name"] #remove name from dict

print(output_dict)

# GOAL dict of lists of dicts
expected_output = {
    "TMUS": [
        {
            "closing": "200.00",
            "date": "2020-12-30",
        },
        {
            "closing": "220.00",
            "date": "2020-12-31",
        }
    ],

    "MSFT": [
        {
            "closing": "100.00",
            "date": "2020-12-30",
        },
        {
            "closing": "110.00",
            "date": "2020-12-31",
        }
    ]
}
