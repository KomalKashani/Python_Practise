
import google.generativeai as genai

class NlpModel:
    def get_model(self):
        # Enter gemini key here in api_key = 
        genai.configure(api_key='**********************')
        model = genai.GenerativeModel("gemini-pro")
        return model

class NlpApp(NlpModel):
    def __init__(self):
        self.__database={}
        self.__first_menu()

    def __first_menu(self):
        first_input=input("""
         Hi! How would you like to proceed?

            1. Not a member? Register
            2. Already a member? Login
            3. Bhai galti se aa gaya kia? Exit
        """)

        if first_input == '1':
            self.__register()
        elif first_input == '2':
            self.__login()
        else:
            exit()

    def __second_menu(self):
        second_input=input("""
         Hi! How would you like to proceed?

            1. Sentiment Analysis
            2. Language Transilation
            3. Language Detection
            4. you want to exit
        """)

        if second_input =='1':
            self.__sentiment_analysis()
        elif second_input == '2':
            self.__language_transilation()
        elif second_input == '3':
            self.__language_detection()
        else:
            exit()

    def __login(self):
        email=input("Enter your email: ")
        password=input("Enter your password: ")
        if email in self.__database:
            if password == self.__database[email][1]:
                print("Login Successfully")
                self.__second_menu()
            else:
                print('Plz enter correct password')
                self.__login()
        else:
            print("Plz register first your email id is not exist.")
            self.__first_menu()

        
    def __register(self):
        name=input("Enter your name: ")
        email=input("Enter your email: ")
        password=input("Enter your password: ")
        if email in self.__database:
            print("Email is already exist plz try with another email")
            self.__first_menu()
        else:
            self.__database[email]=[name,password]
            print("Registered Successfully")
            self.__first_menu()

    def __sentiment_analysis(self):
        user_text=input("Enter your text: ")
        model=super().get_model()
        response = model.generate_content(f"Give me the sentiment of this sentence: {user_text}")
        results = response.text
        print(results)
        self.__second_menu()
        
    def __language_transilation(self):
        user_text=input("Enter your text: ")
        model=super().get_model()
        response = model.generate_content(f"Give me hindi transilation of this sentence: {user_text}")
        result=response.text
        print(result)
        self.__second_menu()
        
    def __language_detection(self):
        user_text=input("Enter your text: ")
        model=super().get_model()
        response=model.generate_content(f"Detect the language of this sentence: {user_text}")
        results=response.text
        print(results)
        self.__second_menu()
nlp=NlpApp()
    