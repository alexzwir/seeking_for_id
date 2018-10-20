"""
A ideia desse script é checar se os usuário que tentaram se cadastrar no site, efetivamente conseguiram ou não. Com isso, teremos três passos:
- Procurar pelo CPF da chamada da API (definida na tabela com atributo -> )
- Retirar e guardar em uma lista.
- Comparar com a base de usuário do site.

The ideia of this project is to search for as specific user ID(CPF) and see if this user it's an register user.


"""

api_request = {"headers":{"Content-Type":"application\/json","client_id":"dcebc3db-22ef-388b-b4d6-f0637751c622","Authorization":"Basic ZGNlYmMzZGItMjJlZi0zODhiLWI0ZDYtZjA2Mzc3NTFjNjIyOmQzYzhlOWNlLTE3NjctM2EzZS05NjBjLTg2ZjkxY2I3NDBkZg=="},"body":"{\"query\": \"mutation{ login( input:{ clientMutationId:\\\"102\\\", username: \\\"03350169872\\\", challenge: \\\"$2a$05$mLgU7bQLjoCZu3WBEiCBIu4XsbyXMjAuiMOOJ83kNYcPxsi1HWE7S\\\"  })  { clientMutationId, accessToken }}\",\"variables\":\"\"}"}

users_usename = []
if type(api_request) == dict:
    print("This variable it's an dictionary.")
    for k,v in api_request.items():
        type_of_k = type(k)
        type_of_v = type(v)
        print("This type {} has the key: {}".format(type_of_k,k))
        print("This type {} has the value: {}".format(type_of_v,v))
        if "username" in v:
            print("We have an username!")
            first_position=v.find("username")
            print("The right position of the string is: {}".format(first_position))
            print(v[62:74])
            print("The cpf is: {}.".format(v[74:85]))
            users_usename.append(v[74:85])
print(users_usename)



            
            
