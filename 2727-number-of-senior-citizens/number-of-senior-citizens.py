class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors = 0 # we'll use this variable to keep track of the citizens

        # the problem tells us that the 12th and 13th character denote the age
        # so if we check chars 12:13 we can get the age
        # 
        for person in details:
            # we can slice the string, and turn them into ints
            # to get 12 and 13, we do 11:13, because arrays are 0 index, and the end point, in our case 13, is exclusive,
            # so go up to 13, but dont include it. this is how you get 11 and 12. start is inclusive.
            if int(person[11:13]) > 60:
                seniors += 1
        
        return seniors
            