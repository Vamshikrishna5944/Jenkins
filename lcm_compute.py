def compute_lcm(x, y):

   if x > y:
       max = x
   else:
       max = y

   while(True):
       if((max % x == 0) and (max % y == 0)):
           lcm = max
           break
       greater += 1

   return lcm