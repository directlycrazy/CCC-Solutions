#include <bits/stdc++.h> 
using namespace std; 

#define ll long long

//calculates the total walking time for a given position
ll calculate_time(ll pos, ll N, vector<vector<ll>> friends) {

    ll time = 0; 

    for(int i = 0; i < N; i++) {
        time += (max(abs(pos - friends[i][0]) - friends[i][2], (ll)0) * friends[i][1]); 
    }

    return time; 
}


int main() {

    ios_base::sync_with_stdio(false); 
    cin.tie(0); 

    ll N; 
    cin >> N; 

    //stores friends
    vector<vector<ll>> friends(N, vector<ll>(3)); 

    //left and right bounds for binary search
    ll left = 1000000000; 
    ll right = 0; 
    
    // update friends array and update the furthest left and right bounds
    for(int i = 0; i < N; i++) {
        cin >> friends[i][0] >> friends[i][1] >> friends[i][2]; 

        right = max(right, friends[i][0]); 
        left = min(left, friends[i][0]); 
    }

    // calculate starting mid point
    ll mid = (right + left) / 2; 
    
    // perform binary search to find smallest value
    while(true) {
        ll left_time = calculate_time(mid-1, N, friends); 
        ll right_time = calculate_time(mid+1, N, friends); 
        ll cur_time = calculate_time(mid, N, friends); 

        if(left_time < cur_time) {
            right = mid; 
            mid = (mid + left) / 2; 
        } else if(right_time < cur_time) {
            left = mid; 
            mid = (right + mid) /2; 
        } else {
            cout << cur_time; 
            break; 
        }

    }
    
    return 0; 
}
