Def fact_rec(n):
  If n==0 or n==1:
    Return 1
  Else:
     Return n*fact_rec(n-1)
Number = int(input(“Enter a value :”))
Res = fact_rec(number)
Print(“The factorial of {} is{}.”.format(number, res))