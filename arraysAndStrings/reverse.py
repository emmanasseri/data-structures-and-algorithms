class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        #abcde
        a=int(len(s)/2)         #gets halfway point
        b=len(s)-1              #gets end index
        for i in range(0,a):    #for the first half of the length of the string
            s[i],s[b]=s[b],s[i] #swap the character at the index with the character it mirrors
            b-=1                #move the index back one
        print(s)                #print the string to display that it mirrored correctly
            

test = Solution
stringTest = ["h","e","l","l","o"] 
test().reverseString(stringTest)