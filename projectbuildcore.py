global expenses
expenses=[]
monthly_allowance=float(input('enter monthly allowance:'))
savingsgoal=monthly_allowance*0.2

def add_expenses(expenses):
         amount=float(input('enter amount:'))
         category=input('enter category')
         description=input('enter description')
         expense={'amount':amount,'category':category,'description':description}
         expenses.append(expense)
         print('expense added successfully')
def view_expenses():
    for i in expenses:
          print(i)
def search_expenses():
          category=input('enter category to search')
          for i in expenses:
                if i['category']==category:
                      print('expense for the selected category=',i)
def delete_expense():
          description=input('enter description of expense to delete')
          for i in expenses:
                if i['description']==description:
                      expenses.remove(i)
                      print('expense deleted successfully')
                      break
                else:
                      print('expense not found')
def total_expenses():
       global total
       total=0
       for i in expenses:
                total+=i['amount']
       print('total expenses=',total)
def set_monthly_budget(total):
          global remaining_budget
          budget=float(input('enter budget:'))
          remaining_budget=budget-total
          if total>budget:
                    print('Alert! You have exceeded your budget')
          else:
                    print('you are within your budget')
                    print('remaining budget:', remaining_budget)
def savings_goal(monthly_allowance, total,savingsgoal,remaining_budget):
          savings=monthly_allowance-total+remaining_budget
          if savings==savingsgoal:
                print('you have saved as per your goal & savings:',savings)
          elif savings>savingsgoal:
                print('congratulations! you are saving more than your goal & your savings:',savings)
          else:
                print('BETTER LUCK NEXT TIME!')



while True:
    print(' MONTHLY PERSONAL EXPENSE TRACKER')
    print('1.add expense')
    print('2.view expenses')
    print('3.search expenses')
    print('4.delete expense')
    print('5.total expenses')
    print('6.set monthly budget')
    print('7.savings goal')
    print('8.exit')
    choice=int(input('enter your choice'))
    if choice==1:
          add_expenses(expenses)
    elif choice==2:
          view_expenses()
    elif choice==3:
          search_expenses()
    elif choice==4:
          delete_expense()
    elif choice==5:
          total_expenses()
    elif choice==6:
          set_monthly_budget(total)
    elif choice==7:
          savings_goal(monthly_allowance,total,savingsgoal,remaining_budget)
    elif choice==8:
          print('exiting the program')
          break
    else:
            print('invalid choice')

    
        
        


    

    
          
          
           
        
    