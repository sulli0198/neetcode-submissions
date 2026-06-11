class Solution:
    def groupAnagrams(self, strs):
        result = {}

        for i in strs:
            key = tuple(sorted(i))
            if key in result:
                result[key].append(i)
            else:
                result[key] = [i]
        return list(result.values())    

        
        

        
                    


        
        

                    
                


        