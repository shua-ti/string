class Solution {
    NestedInteger parse(const string &s, int & pos)
    {
        if (s[pos] == '[')
            return parseList(s, pos);
        return parseNum(s, pos);
    }
    NestedInteger parseNum(const string &s, int & pos)
    {
        int num = 0;
        int sign = 1;
        if (s[pos] == '-'){
			 sign =-1;
			 pos ++;
		}
           
        for (;pos < s.size() && isdigit(s[pos]); pos ++)
            num = num * 10 + s[pos] - '0';
        return NestedInteger(sign * num);
    }
    NestedInteger parseList(const string &s, int &pos)
    {
        NestedInteger ni;
        while (s[pos] != ']')
        {
            pos ++;                   //skip [ or ,
            if (s[pos] == ']') break; //handle [] or [1,2,]
            ni.add(parse(s, pos));
        }
        pos ++;                       // skip ]
        return ni;
    }
public:
    NestedInteger deserialize(const string &s) {
        int pos = 0;//pos ALWAYS points to 1 position past the last parsed string;
                    //This is an invariance maintained across the entire program.
        return parse(s, pos);
    }
};