from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API
from tkinter import font
class NLPApp:
    def __init__(self):

        # create db object
        self.dbo = Database()

        # create api object
        self.apio = API()


        # log in ka gui load karna
        self.root = Tk()
        self.root.title("NLPApp")
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#283747')

        self.login_gui()

        # to stream gui on screen
        self.root.mainloop()

    def login_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='#283747', fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana', 24, 'bold'))

        label1 = Label(self.root, text='Enter Email', bg='#283747', fg='white')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter password', bg='#283747', fg='white')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root, text='Login', width=20, height=1, command=self.perform_login)
        login_btn.pack(pady=(30, 10))

        label3 = Label(self.root, text='Not a member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Register Now', width=20, height=1, command=self.register_gui)
        redirect_btn.pack(pady=(30, 10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#283747', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter name')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter password', bg='#283747', fg='white')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='Register', width=20, height=1, command=self.perform_registration)
        register_btn.pack(pady=(30, 10))

        label3 = Label(self.root, text='Already a member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login Now', command=self.login_gui)
        redirect_btn.pack(pady=(30, 10))


    def clear(self):
         # clear the existing gui
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        # fetch data from gui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name, email, password)
        if response:
            messagebox.showinfo('success', 'Registration Successful.You can login now')
        else:
            messagebox.showerror('Error!!,Email already exists')

    def perform_login(self):
         email = self.email_input.get()
         password = self.password_input.get()
         response = self.dbo.search(email, password)

         if response:
             messagebox.showinfo('success.Login successful')
             self.home_gui()
         else:
             messagebox.showerror('Error,Incorrect Email/Password')

    def home_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#283747', fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana', 24, 'bold'))

        sentiment_btn = Button(self.root, text='sentiment Analysis', width=50, height=3, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='Name Entity Recognition', width=50, height=3, command=self.ner_gui)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion Prediction', width=50, height=3, command=self.emotion_gui)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Logout', width=50, height=3, command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='#283747', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#283747', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=100)
        self.sentiment_input.pack(pady=(20, 10), ipady=10)

        sentiment_btn = Button(self.root, text='Analyze Sentiment', width=40, height=2, command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, bg='#283747', fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        txt = ''
        for i in result['sentiment']:
            txt = txt + i + ' -> ' + str(result['sentiment'][i]) + '\n'

        print(txt)
        self.sentiment_result['text'] = txt


    def ner_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='#283747', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Named Entity Recognition', bg='#283747', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.ner_input = Entry(self.root, width=100)
        self.ner_input.pack(pady=(20, 10), ipady=10)

        ner_btn = Button(self.root, text='recognize Named Entity', width=40, height=2, command=self.do_Named_Entity_Recognition)
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, bg='#283747', fg='white')
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_Named_Entity_Recognition(self):
        text = self.ner_input.get()
        result = self.apio.ner_Recognition(text)

        # Create a variable to store the formatted result
        formatted_result = ""

        # Format the header with bold
        formatted_result += "{:<20} {:<20} {:<20}\n".format(
            'Name', 'Category', 'Confidence Score'
        )

        # Iterate through entities and format information
        for index, entity in enumerate(result['entities']):
            name = entity['name']
            category = entity['category']
            confidence_score = entity['confidence_score']

            # Format the information
            formatted_result += "{:<20} {:<20} {:<20}\n".format(name, category, confidence_score)


        # Create a fixed-width font
        fixed_width_font = font.Font(family="Courier", size=10)  # Adjust size as needed

        # Update a label or text widget with the formatted result using fixed-width font
        self.ner_result['text'] = formatted_result
        self.ner_result['font'] = fixed_width_font  # Set the font


    def emotion_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='#283747', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Emotion Analysis', bg='#283747', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.emotion_input = Entry(self.root, width=100)
        self.emotion_input.pack(pady=(20, 10), ipady=10)

        # Update the button command to call do_emotion_analysis
        emotion_btn = Button(self.root, text='Analyze emotion', width=40, height=2, command=self.do_emotion_analysis)
        emotion_btn.pack(pady=(10, 10))

        self.emotion_result = Label(self.root, bg='#283747', fg='white')
        self.emotion_result.pack(pady=(10, 10))
        self.emotion_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_emotion_analysis(self):
        text = self.emotion_input.get()
        result = self.apio.emotion_analysis(text)

        txt = ''
        for i in result['emotion']:
            txt = txt + i + ' -> ' + str(result['emotion'][i]) + '\n'

        print(txt)
        self.emotion_result['text'] = txt

        print(result)




















nlp = NLPApp()

