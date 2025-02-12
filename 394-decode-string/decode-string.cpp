class Solution {
public:
    string decodeString(string s) {
        stack<int> br;
        int size = s.size(), idx = 0;

        while(idx<size){
            if(s[idx] == '[') br.push(idx);
            if(s[idx] == ']') {
                // cout<<(s[br.top()-1] - '0')<<endl;
                int top = br.top(), step = 0, num = 1, c = top-1;
                while(c>=0&&isdigit(s[c])){
                    step+=num*(s[c] - '0');
                    c--;num*=10;
                }
                string sub = s.substr(top+1, idx-top-1);
                
                string tmp1 = s.substr(0, c+1), tmp2 = s.substr(idx+1, size-idx);
                for(int i = 0;i<step;i++) tmp1+=sub;
                s= tmp1+tmp2;
                idx = c+1;
                // cout<<tmp1<<endl;
                size = s.size();
                br.pop();
            }
            idx++;
        }

        return s;
    }
};