#Data structure for Project-Bank

1. General
2. User data
3. Bank-Account data
4. Account-Cards data

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
            is_locked: boolean,
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
            ],
            card_connected: boolean,
            card_number: string
        }
    }
}`

##4. Account-Cards data
The data for accounts-cards is stored seperately in ./data/accounts-cards. Also this is a monolithic file with key-value pairs where the key is the **userID** and the value is a nested dictionary with all the different values stored.
How and what data will be stored:
{
  "user_id": {
    "card_number": {
      "account_id": string,
      "card_number": string,
      "cardholder_first_name" : string,
      "cardholder_last_name": string,
      "cardholder_middle_name": string,
      "expiration_date": string //only year and month,
      "security_code": string,
      "PIN_code": "string //will be hashed"
    }
  }
}