import tkinter as tk

# Classes that run the ROI
class Property():
    def __init__(self, income, tax, insure, fees, tot_invest, util = 0):
        self.income = income
        self.tax = tax
        self.insure = insure
        self.util = util
        self.fees = fees
        self.tot_invest = tot_invest
    
    def __repr__(self):
        return f'<Property | {self.income} | {self.tot_invest}>'

class ROI_calculator():
    def __init__(self):
        pass

    def __repr__(self):
        return f'<ROI_calculator | {self.property.income} | {self.property.tot_invest} | {self.cash_on_cash_roi*100}%>'
    
    def req_num_input(self, query):
        if query == 'income':
            input_return = input(f'How much {query} do you expect to get from this property?')
            while not input_return.isdigit():
                input_return = input(f'That is not a valid input.  How much {query} do you expect to get from this property?  Use only numbers. No commas, No dollar signs')
                
        elif query in {'tax', 'insurance', 'fees'}:
            input_return = input(f'How much do you pay monthly for {query}?')
            while not input_return.isdigit():
                input_return = input(f'That is not a valid input. How much do you pay monthly for {query}?  Use only numbers. No commas, No dollar signs')
        elif query == 'total investment':
            input_return = input(f'How much is your {query}?')
            while not input_return.isdigit():
                input_return = input(f'That is not a valid input. How much is your {query}?  Use only numbers. No commas, No dollar signs')
        return int(input_return)
    
    def _calc_cash_on_cash_roi(self):
        self.tot_expense = self.property.tax + self.property.insure + self.property.util + self.property.fees
        self.montly_cashflow = self.property.income - self.tot_expense
        self.yearly_cashflow = self.montly_cashflow * 12
        self.cash_on_cash_roi = self.yearly_cashflow / self.property.tot_invest
        #print(f'Your ROI is {self.cash_on_cash_roi * 100}% with a montly cashflow of {self.montly_cashflow}, and an initial investment of {self.property.tot_invest}')
    
    def create_property(self):
        income = self.req_num_input('income')
        tax = self.req_num_input('tax')
        insure = self.req_num_input('insurance')
        fees = self.req_num_input('fees')
        tot_invest = self.req_num_input('total investment')
        self.property = Property(income, tax, insure, fees, tot_invest)
        self._calc_cash_on_cash_roi()
         
    def edit_property(self):
        input_return = input('Which propery would you like to edit?')
        while input_return not in {'income', 'tax', 'insurance', 'fees', 'investment'}:
            input_return = input("That is not a valid input.  Which propery would you like to edit? (income/tax/insurance/fees/investment)")
        if input_return == 'income':
            self.property.income = self.req_num_input('income')
        elif input_return == 'tax':
            self.property.tax = self.req_num_input('tax')
        elif input_return == 'insurance':
            self.property.insure = self.req_num_input('insurance')
        elif input_return == 'fees':
            self.property.fees = self.req_num_input('fees')
        elif input_return == 'investment':
            self.property.tot_invest = self.req_num_input('total investment')
        self._calc_cash_on_cash_roi()


# This does executes the CLI ROI
def calculate_roi():
    print('Welcome to my ROI Calculator! Good luck on your investment!')
    calculator = ROI_calculator()
    calculator.create_property()
    while True:
        desire = input(f'Would you like to edit your current calculation, start a new cacluation, or quit? (E/S/Q)')
        while desire[0].lower() not in {'e','s','q'}:
            desire = input(f'That was not a valid input.  Would you like to edit your current calculation, start a new cacluation, or quit? Use only E, S, or Q)')
        if desire[0].lower() == 'e':
            calculator.edit_property()
        elif desire[0].lower() == 's':
            calculator.create_property()
        elif desire[0].lower() == 'q':
            print('Thank you for using my calculator!  Goodbye!')
            break
        else:
            print('SOMETHING WENT VERY WRONG!')
            break





def tab2(calculator):

    def back():
        for frame in root.winfo_children():
            frame.destroy()
        tab1(calculator)

    frame2 = tk.Frame(root)
    frame2.pack()

    label2 = tk.Label(frame2,text='Your ROI is:', font = ('Times',25))
    label2.grid(row=0, column=0)
    roi_label = tk.Label(frame2,text=f'{calculator.cash_on_cash_roi*100}%', font = ('Times',50))
    roi_label.grid(row=1,column=0)

    detail_frame = tk.Frame(frame2)
    detail_frame.grid(row=2,column=0)
    income = tk.Label(detail_frame, text = 'Monthly Income:')
    income.grid(row = 0, column = 0)
    income_tot = tk.Label(detail_frame, text = f'{calculator.property.income}', font=('Times', 14))
    income_tot.grid(row=1,column=0)

    costs = tk.Label(detail_frame, text = 'Monthly Costs:')
    costs.grid(row = 0, column = 2)
    income_tot = tk.Label(detail_frame, text = f'{calculator.tot_expense}', font=('Times', 14))
    income_tot.grid(row=1,column=2)

    takehome = tk.Label(detail_frame, text = 'Monthly Costs:')
    takehome.grid(row = 0, column = 3)
    takehome_tot = tk.Label(detail_frame, text = f'{calculator.montly_cashflow}', font=('Times', 14))
    takehome_tot.grid(row=1,column=3)



    but2 = tk.Button(frame2, text='Edit', font = ('Times',20, 'bold', 'italic'), command =back)
    but2.grid(row=3, column=0)

# NORMAL TEXT SIZE! I AM SICK OF ADJUSTING EACH BY HAND! 
nt = 14

# THIS IS HOW I EDITED THE TEXTBOXES ON THE BLACKJACK APP! p1_cards WAS A BOXES NAME!
# p1_cards.delete(1.0,"end")
# p1_cards.insert(1.0, p1_box)

def tab1(defaults=None):

    def forwards():
        income = int(income_entry.get())
        tax = int(tax_entry.get())
        insure = int(insure_entry.get())
        util = int(util_entry.get())
        fees = int(fees_entry.get())
        tot_invest = int(tot_invest_entry.get())

        calculator = ROI_calculator()
        calculator.property = Property(income, tax, insure, fees, tot_invest, util = util)
        calculator._calc_cash_on_cash_roi()

        for frame in root.winfo_children():
            frame.destroy()
        tab2(calculator)    

    frame = tk.Frame(root)
    frame.pack(pady=20)
    
    header_label = tk.Label(frame, text = 'ROI Calculator', font = ('Times', 25))
    header_label.grid(row=0, column = 0)

    data_entry_frame = tk.LabelFrame(frame, text="Financial Inputs")
    data_entry_frame.grid(row=1,column=0,padx=20,pady=5)
    
    income = tk.Label(data_entry_frame,text="Income", font = ('Times',nt))
    income.grid(row=0, column=0)
    income_entry = tk.Entry(data_entry_frame)
    income_entry.grid(row=1, column=0)

    tax = tk.Label(data_entry_frame,text="Tax", font = ('Times',nt))
    tax.grid(row=0, column=2)
    tax_entry = tk.Entry(data_entry_frame)
    tax_entry.grid(row=1, column=2)

    insure = tk.Label(data_entry_frame,text="Insurance", font = ('Times',nt))
    insure.grid(row=0, column=3)
    insure_entry = tk.Entry(data_entry_frame)
    insure_entry.grid(row=1, column=3)

    util = tk.Label(data_entry_frame,text="Utilities", font = ('Times',nt))
    util.grid(row=3, column=0)
    util_entry = tk.Entry(data_entry_frame)
    util_entry.grid(row=4, column=0)

    fees = tk.Label(data_entry_frame,text="Fees", font = ('Times',nt))
    fees.grid(row=3, column=2)
    fees_entry = tk.Entry(data_entry_frame)
    fees_entry.grid(row=4, column=2)

    tot_invest = tk.Label(data_entry_frame,text="Total Investment", font = ('Times',nt))
    tot_invest.grid(row=3, column=3)
    tot_invest_entry = tk.Entry(data_entry_frame)
    tot_invest_entry.grid(row=4, column=3)

    # THIS IS FOR INSERTING DATA BACK INTO BOXES ONCE IN CALC SCREEN!
    if defaults != None:
        income_entry.insert(0, defaults.property.income)
        tax_entry.insert(0, defaults.property.tax)
        insure_entry.insert(0, defaults.property.insure)
        util_entry.insert(0, defaults.property.util)
        fees_entry.insert(0, defaults.property.fees)
        tot_invest_entry.insert(0, defaults.property.tot_invest)

    for widget in data_entry_frame.winfo_children():
        widget.grid_configure(padx=10,pady=5)
    
    # Cool! You can do math in the font size line!
    info_text = tk.Label(frame, text = "Please only enter whole numbers, and do not use any commas or dollar signs!", font = ('Times', nt-2), padx=20, pady=10)
    info_text.grid(row=2,column=0)

    but1 = tk.Button(frame, text='Calculate', font = ('Times',20, 'bold','italic'), command=forwards)
    but1.grid(row=3, column=0)


root = tk.Tk()
root.title('ROI Calculator')
# root.minsize(height = 500, width = 900)

tab1()

root.mainloop()