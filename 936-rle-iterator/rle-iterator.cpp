class RLEIterator {
private:
    vector<int> enc;
public:
    RLEIterator(vector<int>& encoding) {
        this->enc = encoding;
    }
    
    int next(int n) {
        int idx = 0;
            while (n>0 && idx < enc.size()){
                int temp = this->enc[idx] - n;
                if(temp>=0) {
                    enc[idx]-=n;
                    return enc[idx + 1];
                }
                n-=enc[idx];
                enc[idx] = 0;
                idx+=2;
            }
        return -1;
    }
};

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator* obj = new RLEIterator(encoding);
 * int param_1 = obj->next(n);
 */