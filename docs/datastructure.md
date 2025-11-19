#Data structure for Project-Bank

1. General
2. User data
3. Bank-Account data


##1. General
All data is stored within ./data in .JSON-files. The specified structure can be found beneath for each type of data. This document will most likely be updated as more data is added.


##2. User data
User data is stored in a monolithic file consisting of one key-pair value for each user where the key is their userID and the value is a nested dictionary with their user information. It is constructed as follows:
`{
    user_id : {
        first_name : string,
        last_name : string,
        middle_name : string,
        personal_number : string,
        join_date : string,
        user_id : string
        bank_accounts : [
            accountID(string),
            accountID(string),
            ...
        ],
        password : string //will be hashed
    }
}`


##3. Bank-Account data
The data for bank-accounts is stored seperately in ./data/bank_accounts. Also this is a monolithic file with key-value pairs where the key is the **userID** and the value is a nested dictionary with all the different values stored.

`{
    user_id : {
        account_id : {
            account_id : string,
            account_type : string,
            account_name : string,
            balance : float,
            currency : string,
            date_created : string,
            user_id : string,
            transactions : [
                {
                    amount : float,
                    date : string,
                    from_acc : string,
                    to_acc : string
                }
            ]
        }
    }
}`