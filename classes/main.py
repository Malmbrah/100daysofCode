#How to create a class - all classes should have PascalCase; MyCase. UserInput
class User:
    #Kommer til å bli callet hver gang vi lager et nytt objekt
    def __init__(self, user_id, username):
        #Dette betyr at objektet man lager (self) setter sin id til å være lik user_id man sender inn når man lager objektet
        self.id = user_id
        self.username = username
        #Den er alltid null hvis man lager en ny bruker
        self.followers = 0
        self.following = 0

    #En metode trenger ALLTID en self for å vite hvilket objekt som kalte på den
    #Hvis en User følger en annen bruker
    def follow(self, user):
        #Den brukeren vi følger sine followers går opp
        user.followers += 1
        #De du følger går også opp
        self.following += 1



#How to add attributes - Man lager altså en ny variabel som legger inn i user_1
"""
user_1.id = "001"
user_1.username = "Jonte"

Istedenfor å gjøre slik her, så kan man gjøre:
"""
user_1 = User("001", "Jonathan")
user_2 = User("002", "Live")

user_1.follow(user_2)
